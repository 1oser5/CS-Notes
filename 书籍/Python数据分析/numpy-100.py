#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numpy-100.py
@Time    :   2019/10/15 09:53:19
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   numpy 100道基础题
'''

#1. Import the numpy package under the name np (★☆☆)
import numpy as np


#2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
np.show_config()

# 3. Create a null vector of size 10 (★☆☆)
z = np.zeros(10)
print(z)

#4. How to find the memory size of any array (★☆☆)
z = np.zeros((10, 10))
print("%d bytes"%(z.size * z.itemsize)) # size表示数组元素个数，itemsize表示元素字节数

#5. How to get the documentation of the numpy add function from the command line? (★☆☆)
'''  %run `python -c "import numpy; numpy.info(numpy.add)"` '''

#6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
z = np.zeros(10)
z[4] = 1
print(z)

#7. Create a vector with values ranging from 10 to 49 (★☆☆)
z = np.arange(10,50)
print(z)

#8. Reverse a vector (first element becomes last) (★☆☆)
z = np.arange(50)
z = z[::1]
print(z)

#9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
z = np.arange(9).reshape(3,3)
print(z)

#10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
z = np.nonzero([1,2,0,0,4,0])
print(z)

#11. Create a 3x3 identity matrix (★☆☆)
z = np.eye(3)
print(z)

#12. Create a 3x3x3 array with random values (★☆☆)
z = np.random.random((3,3,3))
print(z)