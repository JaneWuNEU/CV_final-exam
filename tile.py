# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:54:13 2018

@author: neu_1
"""
import cv2
import math
import os

class VideoProcess:
    def getVideoFPS(self,video):
        return math.ceil(video.get(cv2.CAP_PROP_FPS))
    #=========== resolution = width * height ================
    def getVideoResolution(self,video):
        frame_width = int(video.get(3))#cv2.CV_CAP_PROP_FRAME_WIDTH)
        frame_height = int(video.get(4))#cv2.CV_CAP_PROP_FRAME_HEIGHT)
        resolution = (frame_width,frame_height)
        return resolution
    
    def getImageResolution(self,image):
        image_height, image_width = image.shape[:2]# It returns a tuple of number of rows, columns and channels (if image is color):
        resolution = (image_width,image_height)
        return resolution 
        
    # this functiont is to divide the video into small chips, and duration of the chips is X seconds
    def divideVedioIntoSegment(self,video_path,duration=1):
        #print("video path==>",video_path)
        cap = cv2.VideoCapture(video_path)
        
        #==========get fps======= 
        fps = self.getVideoFPS(cap)
        
        #==========get resolution========
        resolution = self.getVideoResolution(cap)
        #  ==>the data must be transformed into int,
        # otherwise the function of cv2.VideoWriter will throw an exception

        
        print("fps of the video==>",fps,"resolution==>",resolution)
        
        if(cap.isOpened()):
           # create a pointer to a video file with the parameters including filename, fps,resolution
           # and this file will be written the frames from the video_path
           fourcc = cv2.VideoWriter_fourcc(*'XVID')
           chunkNum = 0
           chunkName = "F:\\project\\dataset\\vr\\Formated_Data\\Experiment_1\\video\\1-1-chunk/"+str(chunkNum)+".mp4"
           chunkPointer = cv2.VideoWriter(chunkName,fourcc,fps,resolution)
           
           success,frame = cap.read()
           count = 1
           while success:
               if count<=fps*duration: # the length of each segement is duration seconds.
                   chunkPointer.write(frame)
                   count=count+1
               else: 
                   chunkPointer.release()
                   chunkNum=chunkNum+1
                   chunkName = "F:\\project\\dataset\\vr\\Formated_Data\\Experiment_1\\video\\1-1-chunk/"+str(chunkNum)+".mp4"
                   #print("chunkName ",chunkName)
                   chunkPointer = cv2.VideoWriter(chunkName,fourcc,fps,resolution)
                   chunkPointer.write(frame)
                   count=2
               success,frame = cap.read()                   
               
           chunkPointer.release()
           cap.release()
           
        else:
            print("failure")
            
        '''
         divide the segment into rows*colums tiles, and they are indexed from the top to the bottom and the left to the right,
        tile = 
        T[0,0] T[0,1] ... T[0,11]
        T[1,0] T[1,1] ... T[1,11]
        T[11,0] T[11,1]   T[11,11]
        
        '''     

    def divideSegmentIntoTiles(self,segment_path = None,tiles_path = None,rows = 6,colums = 12):
            #1. get the location of the segment file
            segment_path = "F:\project/dataset/vr\\Formated_Data\\Experiment_1\\video\\1-1-segment/3.mp4"
            
            #2. depend on the name of the segment file to create a file to put all the tiles
            tile_file_path = segment_path.rpartition(".")[0]
            if(not os.path.isdir(tile_file_path)):
                os.mkdir(tile_file_path)
            
            #3. produce a series of VideoWriter Instances for different tiles
            # and the name of each tile is X.mp4, X stands for its index within the whole segment
            
            cap = cv2.VideoCapture(segment_path)         
            frame_res = self.getVideoResolution(cap)# 2560 * 1440
            video_fps = self.getVideoFPS(cap)       
            image_res = (int(frame_res[0]/colums),int(frame_res[1]/rows)) # int(2.3)===>2 int(1.9) = 1
            print("image resolution",image_res)
            image_width = image_res[0]
            image_height = image_res[1]
            
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            
            # the name of tiles
            #segmentPointer = cv2.VideoWriter(segment_path,fourcc,video_fps,frame_res)
            if (cap.isOpened()):
                success,frame = cap.read()
                if(success):
                    #frame = cv2.flip(frame,0)
                    
                    if success:#(cv2.imwrite(tile_file_path+"/0.jpg",frame)):
                        cv2.imwrite(tile_file_path+"/complete.jpg",frame)
                        # divide the frames
                        tile_frame = []
                        for r in range(0,rows):
                            for c in range(0,colums-1):
                                #img = frame[r*image_height:r*image_height+image_height,c*image_width:c*image_width+image_width]
                                img = frame[c*image_width:c*image_width+image_width,r*image_height:r*image_height+image_height]
                                tile_frame.append(img)
                                print(img.shape)
                            # the last colum needs to be processed in different ways
                            #img_last_col = frame[r*image_height:r*image_height+image_height,c*image_width:frame_res[0]-1]
                            img_last_col = frame[c*image_width:c*image_width:c*image_width+image_width,r*image_height:]
                            tile_frame.append(img_last_col)
                            print(img_last_col.shape)
                          
                        #save all the img
                        for i in range(0,len(tile_frame)):
                            #print(tile_file_path+"/%d.jpg"%i)
                            if(cv2.imwrite(tile_file_path+"/%d_tile.jpg"%i,tile_frame[i])):
                               #print("get a frame  ",i)
                               pass
                            else:
                                print("fail to get a frame tile")
                                
                            
                            
                            
                            
                            
                            
                            
                    else:
                        print("fail to get a frame")

                else:
                    print("fail to read frames")
            else:
                print("fail to open the videocapture")
            '''
            success,frame = 
            while
            tile_index = 0
            for r in range(0,rows):
                for c in range(0,colums-1):# 最后一列需要特殊处理
                    tile_name = tile_file_path+"/"+str(tile_index)+"_tile.mp4"
                    tile_index=tile_index+1
                    tile = cv2.VideoWriter(tile_name,fourcc,video_fps,image_res)
           ''' 
            
            
            
            
            
            
    def divdeImageIntoTiles(self,image_path,tiles_path,rows = 6,colums = 12):
            #image = cv2.imread(image_path)
            pass
        
video = VideoProcess()
#print(result)
#video.divideVedioIntoChips(video_path)
video.divideSegmentIntoTiles()
        