## 原因
公司有一台 win-10 服务器，由于上面挂着特殊机房的 vpn，因此很多人都需要使用，但是由于是 win-10，并且远程连接数只支持一个，就会导致很奇怪的问题，某个人用着用着就被挤掉线了。或者要用之前得在钉钉问下有人在用对应服务器么，很是奇怪。因此需要类似的监听服务。

## 过程

在网上查找了一下，如果是手动的话，可以通过查看 事件查看器的日志来判断是否有用户进行了登录，win 有一个常用的日志事件机制，下面是几个比较常用的 日志id：

+ 4634：用户被注销
+ 4647: 用户发起注销
+ 4625: 帐户登录失败
+ 4648: 试图使用明确的凭证登录（可以用以查看远程登陆的相关信息，比如远程登陆的IP地址等）

也就是说我们需要监听的是 登入和登出两个id，也就是 4634 和 4648 两个id。

我们可以通过使用 Python 的 win32 库来调取一些 windows 的接口，使用 win32evtlog 模块来获得事件日志，首先要注意的一点是，windows日志分以下几个部分：

+ 应用程序: 对于的 Type = Application
+ 安全: Type = Security
+ setup: None
+ 系统: Type = System


用户远程登录的时候，日志将会打印在 安全日志 中。

对于如何捕获日志，在你下载对应 win32 的文件夹中有一个简单的 Demo

你可以通过再次 pip 安装来得知你之前安装的文件夹位置，我的是` C:\PythonXX\Lib\site-packages\win32\Demos `，运行其中的 `eventLogDemo.py` 就可以获得日志

为了防止找不到，我在下面贴上源码和对应注释
```python
import win32evtlogutil
# 读取日志主函数
def ReadLog(computer, logType="Application", dumpEachRecord = 0):
    # read the entire log back.
    h=win32evtlog.OpenEventLog(computer, logType)
    # 获得日志总长度
    numRecords = win32evtlog.GetNumberOfEventLogRecords(h)
#       print "There are %d records" % numRecords

    num=0
    while 1:
        # 一个 objects 是一个事件流，里面会有几个事件，但是数量不等
        objects = win32evtlog.ReadEventLog(h, win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        if not objects:
            break
        for object in objects:
            # get it for testing purposes, but dont print it.
            msg = win32evtlogutil.SafeFormatMessage(object, logType)
            if object.Sid is not None:
                try:
                    domain, user, typ = win32security.LookupAccountSid(computer, object.Sid)
                    sidDesc = "%s/%s" % (domain, user)
                except win32security.error:
                    sidDesc = str(object.Sid)
                user_desc = "Event associated with user %s" % (sidDesc,)
            else:
                user_desc = None
            if dumpEachRecord:
                print "Event record from %r generated at %s" % (object.SourceName, object.TimeGenerated.Format())
                if user_desc:
                    print user_desc
                try:
                    print msg
                except UnicodeError:
                    print "(unicode error printing message: repr() follows...)"
                    print repr(msg)

        num = num + len(objects)

    if numRecords == num:
        print "Successfully read all", numRecords, "records"
    else:
        print "Couldn't get all records - reported %d, but found %d" % (numRecords, num)
        print "(Note that some other app may have written records while we were running!)"
    win32evtlog.CloseEventLog(h)

def usage():
    print "Writes an event to the event log."
    print "-w : Dont write any test records."
    print "-r : Dont read the event log"
    print "-c : computerName : Process the log on the specified computer"
    print "-v : Verbose"
    print "-t : LogType - Use the specified log - default = 'Application'"


def test():
    # check if running on Windows NT, if not, display notice and terminate
    if win32api.GetVersion() & 0x80000000:
        print "This sample only runs on NT"
        return

    import sys, getopt
    opts, args = getopt.getopt(sys.argv[1:], "rwh?c:t:v")
    computer = None
    do_read = do_write = 1

    logType = "Application"
    verbose = 0

    if len(args)>0:
        print "Invalid args"
        usage()
        return 1
    for opt, val in opts:
        if opt == '-t':
            logType = val
        if opt == '-c':
            computer = val
        if opt in ['-h', '-?']:
            usage()
            return
        if opt=='-r':
            do_read = 0
        if opt=='-w':
            do_write = 0
        if opt=='-v':
            verbose = verbose + 1
    if do_write:
        ph=win32api.GetCurrentProcess()
        th = win32security.OpenProcessToken(ph,win32con.TOKEN_READ)
        my_sid = win32security.GetTokenInformation(th,win32security.TokenUser)[0]

        win32evtlogutil.ReportEvent(logType, 2,
            strings=["The message text for event 2","Another insert"],
            data = "Raw\0Data".encode("ascii"), sid = my_sid)
        win32evtlogutil.ReportEvent(logType, 1, eventType=win32evtlog.EVENTLOG_WARNING_TYPE,
            strings=["A warning","An even more dire warning"],
            data = "Raw\0Data".encode("ascii"), sid = my_sid)
        win32evtlogutil.ReportEvent(logType, 1, eventType=win32evtlog.EVENTLOG_INFORMATION_TYPE,
            strings=["An info","Too much info"],
            data = "Raw\0Data".encode("ascii"), sid = my_sid)
        print("Successfully wrote 3 records to the log")

    if do_read:
        # logType 就是日志类型，Demo默认为 Application，改为 Security 即可
        ReadLog(computer, logType, verbose > 0)

if __name__=='__main__':
    test()
```

相关的源码就不贴出来了，总的思路就是把上图的 `object` 对象的 EVentID 进行一个判断即可知道是什么事件。然后进行相应的通知即可。
