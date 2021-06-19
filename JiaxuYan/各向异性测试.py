#!/usr/bin pythonc
# -*- encoding: utf-8 -*-
'''
@Author  :   Celeste Young
@File    :   各向异性测试.py    
@Time    :   2021/5/10 14:35  
@E-mail  :   iamwxyoung@qq.com
@Tips    :   
'''
import cv2

from JiaxuYan.AnisotropicDiffusion import anisodiff2D

ani = anisodiff2D(1)
img = cv2.imread('png/area_twist_5°.png')
print(anisodiff2D.fit(ani, img))