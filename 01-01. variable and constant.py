#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 변수
'''
Python에서는 변수를 선언하여 사용할 수 있다.
변수 이름은 문자나 숫자로 이루어지는데,
변수 이름은 숫자나 '_' 이외의 특수문자로 시작할 수 없고,
이미 역할이 지정된 keyword는 변수 이름으로 사용할 수 없다.
'''
for a in (1, 3, 10, -2):
    print('a =', a)
    print('a × 3 + 1 =', a * 3 + 1, '\n')

# 상수
'''
Python에서 변수와 같은 이름을 갖는 상수를 선언하는 방법은
기본 문법으로는 제공되지 않는다.
관습적으로 대문자와 '_' 만으로 이루어진 변수는
상수로 취급하여,
처음 대입된 값 이외의 값을 다시 대입하지 않는다.
'''
PI = 3.14159265
for r in (0.1, 3, 15, 100):
    print('r =', r)
    print('PI * (r ** 2) =', PI * (r ** 2), '\n')

INCH_TO_CENTIMETER = 2.54
for centimeter in range(1, 11):
    print(centimeter, 'cm ==',\
        centimeter * INCH_TO_CENTIMETER, 'in\n')