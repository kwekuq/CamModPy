'''
Created on 08 Mar 2014

@author: kwekuq
'''
class video():
    command = "";
    status = False;

    def __init__(self):
        self.command = "MP$Box -add ";
        
    def transpose(self, video):
        if(self.status == False):
            self.command = self.command + video + ".h264 " + video + ".mp4";
            self.status = True;
        else:
            print("Command already excuted. Please try running clean() to reset.");
        
    def clean(self):
        self.command = "MP$Box -add ";
        self.status = False;