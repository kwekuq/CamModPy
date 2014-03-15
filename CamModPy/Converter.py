'''
Created on 08 Mar 2014

@author: kwekuq
'''
class video():
    command = "";

    def __init__(self):
        self.command = "MP$Box -add ";
        
    def transpose(self, video):
        self.command = self.command + video + ".h264 " + video + ".mp4";
        
