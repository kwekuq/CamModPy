#!/usr/bin/python
# Filename: Picture.py
__author__ = 'kwekuq'
import os

class StillCamera:

    command = "";
    imgLocation = False;
    imgExpose = False;
    imgWhiteBalance = False;
    imgSize = False;
    quality = False;
    sharpness = False;
    contrast = False;
    contrast = False;
    

    def __init__(self):
        self.command = "raspistill -t 100 -o ";


    def setlocation(self, location):
        if self.imgLocation == False:
            #os.system("mkdir -p /" + location)
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


    def addExposure(self, exposure):
        if self.imgExposure == False:
            self.command = self.command + "-ex " + exposure + " ";
            self.imgExpose = True;
        else:
            print("Exposure has already been set, try running clean() if you wish to start over.");


    def addWhiteBalance(self, whiteBalance):
        if self.imgWhiteBalance == False:
            self.command = self.command + "-awb " + whiteBalance + " ";
            self.imgWhiteBalance = True;
        else:
            print("White balance has already been set, try running clean() if you wish to start over.");
            
    def setQuality(self, quality):
        if self.quality == False:
            self.command = self.command + "-q " + int(quality) + " ";
            self.quality = True;
        else:
            print("Quality has already been set, try running clean() if you wish to start over");
            

    def setSharpness(self, sharpness):
        if self.sharpness == False:
            self.command = self.command + "-sh " + int(sharpness) + " ";
            self.sharpness = True;
        else:
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setContrast(self, contrast):
        if self.contrast == False:
            self.command = self.command + "-co " + int(contrast) + " ";
            self.contrast = True;
        else:
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setBrightness(self, brightness):
        if self.brightness == False:
            self.command = self.command + "-br " + int(brightness) + " ";
            self.contrast = True;
        else:
            print("Brightness has already been set, try running clean() if you wish to start over");
            
    def setSaturation(self, saturation):
        if self.saturation == False:
            self.command = self.command + "-sa " + int(saturation) + " ";
            self.saturation = True;
        else:
            print("Saturation has already been set, try running clean() if you wish to start over");

    def clean(self):
        self.command = "";
        self.command = "raspistill -t 1000 -o "
        self.imgLocation = False;
        self.imgExpose = False;
        self.imgWhiteBalance = False;
        self.imgSize = False;
        print("Clean up complete");


    def capture(self, FileName):
        os.system(self.command + FileName)
        #self.command = self.command + FileName + " "
        #print(self.command)



#testing that it works proper
if __name__ == '__main__':
    cam = StillCamera();
    cam.capture("GeneralTest.jpg");
    cam.clean();
    
    #Now let us test some effects
    #Testing the size
    cam.setSize('400', '600');
    cam.capture("TestSize.jpg");
    cam.clean();
    
    #Testing easy video sizer
    cam.setEasySize('small');
    cam.capture('TestEasyVid.jpg');
    cam.clean();
    
    #Testing the sharpness
    cam.setSharpness('10');
    cam.capture('TestSharpness.jpg');
    cam.clean();

version = '0.6'




