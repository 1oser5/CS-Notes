#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_empty.py
@Time    :   2019/12/06 15:58:13
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用一个符合正常结果接口的“空类型”来替代空值返回/抛出异常，以此来降低调用方处理结果的成本。
'''

# here put the import lib
import decimal

class CreateAccountError(Exception):
    pass

class Account(object):
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
    @classmethod
    def format_string(cls,s):
        try:
            username, balance = s.split(' ')
            balance = decimal.Decimal(float(balance))
        except:
            raise CreateAccountError('input must follow pattern "{ACCOUNT_NAME} {BALANCE}')
        if balance < 0:
            raise CreateAccountError('balance cant be negative')
        return cls(username,balance)

def count_total_balance(accout_list):
    result = 0
    for accout in accout_list:
        try:
            user = Account.format_string(accout)
        except CreateAccountError as e:
            pass
        else:
            result += user.balance
    return result

# use 空类型，这翻译不了，太🐂🍺了
class User(object):
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
    @classmethod
    def format_string(cls,s):
        try:
            username, balance = s.split(' ')
            balance = decimal.Decimal(float(balance))
        except ValueError:
            return NullUser()
        if balance < 0 :
            return NullUser()
        else:
            return cls(username, balance)
# 空类型，用来处理错误
class NullUser(object):
    def __init__(self):
        self.username = ''
        self.balance = 0
    @classmethod
    def format_string(self):
        raise NotImplementedError
def count_balance(accout_list):
    result = 0
    for account in accout_list:
        result += User.format_string(account).balance
    return result
if __name__ == '__main__':
    accounts_data = [
    'piglei 96.5',
    'cotton 21',
    'invalid_data',
    'roland $invalid_balance',
    'alfred -3',
]
print(count_total_balance(accounts_data))
print(count_balance(accounts_data))