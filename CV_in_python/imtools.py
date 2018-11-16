# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:42:59 2018

@author: neu_1
"""

import os
from PIL import Image
from pylab import *
class ImageTools:
    def get_imlist(self,path):
       return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpeg")]

    def get_thumbnail(self,image,size):
        pass

    def get_image(self,path):
       pil_im =  Image.open(path)
       #pil_im.show()
       return pil_im
   
    '''
    box 为四元组（X0,X1,X2,X3）(X0,X1)表示左上角的起始点，（X2,X3）为右下角的终点
    The syntax is the following:
    cropped = img.crop( ( x, y, x + width , y + height ) )
    x and yare the top left coordinate on image;
    x + width and y + height are the width and height respectively of the region 
    that you want to crop starting at x and ypoint.
    Note: x + width and y + height are the bottom right coordinate of the cropped region.
    '''
    def crop_region(self,image,box):
        region = image.crop((500,120,600,330))
        #image.show()
        region.show()
        return region
         
    '''
    把region粘贴在image的box里,
    1.box的尺寸必须和region的尺寸相互匹配，否则会抛出异常
    2.这里的region直接粘贴在image，即会修改原图；而复制crop不会修改image
    '''
    def paste_region(self,image,region,box):
        image.paste(region,(0,0,100,210))
        image.show()

        
