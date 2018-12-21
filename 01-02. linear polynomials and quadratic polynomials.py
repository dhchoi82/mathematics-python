#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 람다 함수
'''
Python에서는 람다식을 이용하여 함수를 선언할 수 있다.
람다식은
  lambda [매개변수들]: [표현식]
의 꼴로 사용한다.
람다식은 변수에 대입하여 이름 있는 함수로 사용하거나
익명함수로 사용할 수 있다.
'''
for a in (1, 3, 10, -2):
    print('(a, 3 * a + 1) =', (a, (lambda x: 3 * x + 1)(a))) # x에 대한 1차식

freeFall = lambda t: 4.9 * (t ** 2) # t에 대한 2차식
for b in range(0, 10, 2):
    print('Free fall distance at', b, 'seconds later:',\
        freeFall(b))

# turtle 그래픽
'''
turtle 라이브러리를 불러오면
이동하는 turtle 객체를 이용해서
흔적 그림을 그려볼 수 있다.

turtle.penup()을 실행하면
turtle 객체의 이동 시,
이동 흔적 그림이 그려지지 않는다.

turtle.pendown()을 실행하면
turtle 객체의 이동 시,
이동 흔적 그림이 그려진다.

turtle.setposition([2차원 좌표])를 실행하면
입력된 좌표로 turtle 객체가 이동한다.

turtle.dot()을 실행하면
turtle 객체의 위치에 점이 찍힌다.
'''
import turtle
turtle.penup()
turtle.setposition(-10, 0)
turtle.pendown()
turtle.setposition(300, 0)
turtle.penup()
turtle.setposition(0, -10)
turtle.pendown()
turtle.setposition(0, 300)

vy0 = 55
vx = lambda t: 28
vy = lambda t: vy0 - 9.8 * t # t에 대한 1차식
height0 = 0
sx = lambda t: vx(t) * t # t에 대한 1차식
height = lambda t: height0 + vy0 * t - 4.9 * (t ** 2) # t에 대한 2차식

turtle.penup()
turtle.setposition(0, height0)
turtle.pendown()
for t in range(10):
    turtle.setposition(sx(t), height(t)) # 포물선
    turtle.dot()

turtle.penup()
turtle.setposition(0, vy0)
turtle.pendown()
for t in range(10):
    turtle.setposition(sx(t), vy(t)) # 직선
    turtle.dot()

input()