# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:12:11 2018

@author: neu_1
"""

'''chapter 1 学习图像的基本操作 '''
from PIL import Image
import pylab
import numpy as np
pil_im = Image.open("./lena.tiff")

#把图像读到数组里
im = np.array(pil_im.convert("L"))
#新建一个图像
pylab.figure()
#pylab.gray() #该函数在这里并没有发挥作用
pylab.contour(im,origin = 'image')
pylab.axis('equal')
pylab.axis('off')
pylab.show()
x = pylab.ginput(3) #相当于getchar（）一样
print(x)