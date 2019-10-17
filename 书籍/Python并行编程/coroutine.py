#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   coroutine.py
@Time    :   2019/10/17 18:29:19
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用协程实现有限状态机（finite state machine or  automaton，FSA）
'''

# here put the import lib
import asyncio
import time
from random import randint


@asyncio.coroutine
def StartState():
    print("Start State called \n")
    input_value = randint(0, 1)
    time.sleep(1)
    if (input_value == 0):
        result = yield from State2(input_value)
    else:
        result = yield from State1(input_value)
    print("Resume of the Transition : \nStart State calling " + result)

@asyncio.coroutine
def State1(transition_value):
    outputValue =  str("State 1 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from State3(input_value)
    else :
        result = yield from State2(input_value)
    result = "State 1 calling " + result
    return outputValue + str(result)

@asyncio.coroutine
def State2(transition_value):
    outputValue =  str("State 2 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State1(input_value)
    else :
        result = yield from State3(input_value)
    result = "State 2 calling " + result
    return outputValue + str(result)

@asyncio.coroutine
def State3(transition_value):
    outputValue = str("State 3 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State1(input_value)
    else :
        result = yield from EndState(input_value)
    result = "State 3 calling " + result
    return outputValue + str(result)

@asyncio.coroutine
def EndState(transition_value):
    outputValue = str("End State with transition value = %s \n" % transition_value)
    print("...Stop Computation...")
    return outputValue

if __name__ == "__main__":
    print("Finite State Machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())
    
