__author__ = 'kwekuq'

import os;
class Camera:

    command = "raspivid -o ";
    imgLocation = False;
    imgExpose = False;
    imgWhiteBalance = False;
    imgSize = False;

    def __init__(self):
        self.command = "raspivid -o ";

    def setlocation(self, location):
        if self.imgLocation == False:
            os.system("mkdir -p /" + location)
            self.command = self.command + location
            self.imgLocation = True;
        else:
            print("Location has already been set, try running clean() if you wish to start over.");


    def setSize(self, width, height):
        if self.imgSize == False:
            self.command = self.command + "-w " + width + " -h " + height + " "
            self.imgSize = True;
        else:
            print("Capture size has already been set, try running clean() if you wish to start over.")


    def setEasySize(self, size):
        if self.imgSize == False:
            if size == "huge":
                self.command("")
            elif size == "big":
                self.command = self.command + "-w 1280 -h 960 ";
            elif size == "medium":
                self.command = self.command + "-w 640 -h 480 ";
            elif size == "small":
                self.command = self.command + "-w 320 -h 2400 ";
            else:
                print("Please select a size.");
            self.imgSize = True;
        else:
            print("Capture size has already been set, try running clean() if you wish to start over.");

    def capture(self, FileName):
        #os.system(self.command + "-o " + FileName + ".h264")
        self.command = self.command + FileName + " "
        print(self.command)

