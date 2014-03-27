#!/usr/bin/python
# Filename: Picture.py
__author__ = 'kwekuq'
import subprocess
import os

class StillCamera:

    command = "";
    imgLocation = False;
    imgExposure = False;
    imgWhiteBalance = False;
    imgSize = False;
    quality = False;
    sharpness = False;
    contrast = False;
    contrast = False;
    brightness = False;
    saturation = False;
    
    message = "";
    
    def __init__(self):
        self.command = "raspistill -t 100 ";


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


    def setSize(self, width, height):
        if self.imgSize == False:
            self.command = self.command + "-w " + width + " -h " + height + " "
            self.imgSize = True;
        else:
            self.message = ("Capture size has already been set, try running clean() if you wish to start over.")


    def setEasySize(self, size):
        if self.imgSize == False:
            if size == "huge":
                self.command("")
            elif size == "big":
                self.command = self.command + "-w 1280 -h 960 ";
            elif size == "medium":
                self.command = self.command + "-w 640 -h 480 ";
            elif size == "small":
                self.command = self.command + "-w 320 -h 240 ";
            else:
                self.message = ("Please select a size.");
            self.imgSize = True;
        else:
            self.message = ("Capture size has already been set, try running clean() if you wish to start over.");


    def addExposure(self, exposure):
        if self.imgExposure == False:
            self.command = self.command + "-ex " + exposure + " ";
            self.imgExpose = True;
        else:
            self.message = ("Exposure has already been set, try running clean() if you wish to start over.");


    def addWhiteBalance(self, whiteBalance):
        if self.imgWhiteBalance == False:
            self.command = self.command + "-awb " + whiteBalance + " ";
            self.imgWhiteBalance = True;
        else:
            self.message = ("White balance has already been set, try running clean() if you wish to start over.");
            
    def setQuality(self, quality):
        if self.quality == False:
            self.command = self.command + "-q " + quality + " ";
            self.quality = True;
        else:
            self.message = ("Quality has already been set, try running clean() if you wish to start over");
            

    def setSharpness(self, sharpness):
        if self.sharpness == False:
            self.command = self.command + "-sh " + sharpness + " ";
            self.sharpness = True;
        else:
            self.message = ("Sharpness has already been set, try running clean() if you wish to start over");

    def setContrast(self, contrast):
        if self.contrast == False:
            self.command = self.command + "-co " + contrast + " ";
            self.contrast = True;
        else:
            self.message = ("Sharpness has already been set, try running clean() if you wish to start over");

    def setBrightness(self, brightness):
        if self.brightness == False:
            self.command = self.command + "-br " + brightness + " ";
            self.contrast = True;
        else:
            self.message = ("Brightness has already been set, try running clean() if you wish to start over");
            
    def setSaturation(self, saturation):
        if self.saturation == False:
            self.command = self.command + "-sa " + saturation + " ";
            self.saturation = True;
        else:
            self.message = ("Saturation has already been set, try running clean() if you wish to start over");

    def clean(self):
        self.command = "";
        self.command = "raspistill -t 100 "
        self.imgLocation = False;
        self.imgExpose = False;
        self.imgWhiteBalance = False;
        self.imgSize = False;
        self.message = ("Clean up complete");


    def capture(self, FileName):
        try:
            self.command = self.command + "-o " + FileName + " ";
            subprocess.call(self.command);
        except OSError:
            self.message = "ERROR! Please make sure you have plugged in your Camera Module, and in the correct place!";

version = '0.7'




