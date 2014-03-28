__author__ = 'kwekuq'

import os;
import subprocess
class MotionCamera:

    command = "raspivid ";
    fullpath = "";
    imgLocation = False;
    imgExpose = False;
    imgWhiteBalance = False;
    imgSize = False;
    imgSharpness = False;
    imgContrast = False;
    imgBrightness = False;
    imgSaturation = False;
    imgBitrate = False;
    imgDuration = False;
    
    message = "";
    
    def __init__(self):
        self.command = "raspivid ";

    def setlocation(self, location):
        if self.imgLocation == False:
            try:
                if not os.path.exists(location):
                    os.makedirs(location)
                    self.message = ("Directory created!");
                else:
                    self.message = ("Directory already exists and using!");
                self.command = self.command + location
                self.imgLocation = True;
                
            except:
                self.message = ("Error! Could not create directory, please check permissions.");
        else:
            self.message = ("Location has already been set, try running clean() if you wish to start over.");
            
    def setName(self, nameOfVid):
        self.command = self.command + "-o " + nameOfVid + ".h264 "
        
    def setSize(self, width, height):
        if self.imgSize == False:
            self.command = self.command + "-w " + width + " -h " + height + " "
            self.imgSize = True;
        else:
            self.message = ("Capture size has already been set, try running clean() if you wish to start over.");

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
            self.message = ("Capture size has already been set, try running clean() if you wish to start over.");
            
    def setSharpness(self, sharpness):
        if self.imgSharpness == False:
            self.command = self.command + "-sh " + sharpness + " ";
            self.imgSharpness = True;
        else:
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setContrast(self, contrast):
        if self.imgContrast == False:
            self.command = self.command + "-co " + int(contrast) + " ";
            self.imgContrast = True;
        else:
            self.message = ("Sharpness has already been set, try running clean() if you wish to start over");

    def setBrightness(self, brightness):
        if self.imgBrightness == False:
            self.command = self.command + "-br " + int(brightness) + " ";
            self.imgBrightness = True;
        else:
            self.message = ("Brightness has already been set, try running clean() if you wish to start over");
            
    def setSaturation(self, saturation):
        if self.imgSaturation == False:
            self.command = self.command + "-sa " + int(saturation) + " ";
            self.imgSaturation = True;
        else:
            self.message = ("Saturation has already been set, try running clean() if you wish to start over");
            
    def setBitrate(self, bitrate):
        if self.imgBitrate == False:
            self.command = self.command + "-b " + int(bitrate) + " ";
            self.imgBitrate = True;
        else:
            self.message = ("bitrate has already been set, try running clean() if you wish to start over");
            
    def setDuration(self, duration):
        if self.imgDuration == False:
            self.command = self.command + "-t " + duration + " ";
            self.imgDuration = True;
        else:
            self.message = ("Saturation has already been set, try running clean() if you wish to start over");
            
    def clean(self):
        self.command = "raspivid "
        self.imgLocation = False;
        self.imgExpose = False;
        self.imgWhiteBalance = False;
        self.imgSize = False;
        self.imgSharpness = False;
        self.imgContrast = False;
        self.imgBrightness = False;
        self.imgSaturation = False;
        self.imgBitrate = False;
        self.imgDuration = False;
        self.message = ("Clean up complete");

    def capture(self):
        try:
            #os.system(self.command + "-o " + FileName + ".h264")
            #self.command = self.command + "-o " + FileName + " ";
            subprocess.call(self.command);
        except OSError:
            self.message = "ERROR! Please make sure you have plugged in your Camera Module, and in the correct place!";
        

            

version = '0.7'

    
    