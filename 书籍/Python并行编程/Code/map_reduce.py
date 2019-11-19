#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   map_reduce.py
@Time    :   2019/10/22 13:40:20
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   对比 SCOOP 实现 MapReduce 和 Python 内置实现
'''

# here put the import lib
import operator
import time
import scoop

def simulateWorkload(inputData):
    time.sleep(0.01)
    return sum(inputData)

def CompareMapReduce():
    mapScoopTime = time.time()
    res = scoop.futures.mapReduce(
        simulateWorkload,
        operator.add,
        list([a] * a for a in range(1000)),
    )
    mapScoopTime = time.time() - mapScoopTime
    print("futures.map in SCOOP executed in {0:.3f}s with result:{1}".format(mapScoopTime, res))

    mapPythonTime = time.time()
    res = sum(map(simulateWorkload,list([a] * a for a in range(1000))))
    mapPythonTime = time.time() - mapPythonTime
    print("map in Python executed in {0:.3f}s with result : {1}".format(mapPythonTime, res))
if __name__ == '__main__':
    CompareMapReduce()