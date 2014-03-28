'''
Created on 27 Mar 2014

@author: kwekuq
'''
# The motive of this class is to provide an interface of creating a picture or a video using a raspberry pi camera module
#!/usr/bin/python
# Filename: Picture.py
#from CamModPy import Picture
import Picture
import Video
import ToolBox
pic = None;
vid = None;
toolInstruc = None
#This enables the user to get hold of the picture class
#This makes it easy to get hold of all the class properties in picture, and if any changes occur it is simple to keep the reference the same all the time
class image:
    def __init__(self):
        self.pic = Picture.StillCamera();
    def On(self):
        return self.pic;
    def Off(self):
        self.pic = None;
#This enables the user to get hold of the video class
#This makes it easy to get hold of all the class properties in video, and if any changes occur it is simple to keep the reference the same all the time
class video:
    def __init__(self):
        self.vid = Video.MotionCamera();
    def On(self):
        return self.vid;
    def Off(self):
        self.vid = None;
        
class tool:
    def __init__(self):
        self.toolInstruc = ToolBox.videoConvert();
    def On(self):
        return self.toolInstruc;
    def Off(self):
        self.toolInstruc = None
        
#THis is the only contact the user has with the entire package.