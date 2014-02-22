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
        self.command = "raspistill -t 100 ";


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
                self.command = self.command + "-w 320 -h 240 ";
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
            self.command = self.command + "-q " + quality + " ";
            self.quality = True;
        else:
            print("Quality has already been set, try running clean() if you wish to start over");
            

    def setSharpness(self, sharpness):
        if self.sharpness == False:
            self.command = self.command + "-sh " + sharpness + " ";
            self.sharpness = True;
        else:
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setContrast(self, contrast):
        if self.contrast == False:
            self.command = self.command + "-co " + contrast + " ";
            self.contrast = True;
        else:
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setBrightness(self, brightness):
        if self.brightness == False:
            self.command = self.command + "-br " + brightness + " ";
            self.contrast = True;
        else:
            print("Brightness has already been set, try running clean() if you wish to start over");
            
    def setSaturation(self, saturation):
        if self.saturation == False:
            self.command = self.command + "-sa " + saturation + " ";
            self.saturation = True;
        else:
            print("Saturation has already been set, try running clean() if you wish to start over");

    def clean(self):
        self.command = "";
        self.command = "raspistill -t 100 "
        self.imgLocation = False;
        self.imgExpose = False;
        self.imgWhiteBalance = False;
        self.imgSize = False;
        print("Clean up complete");


    def capture(self, FileName):
        self.command = self.command + "-o " + FileName + " "
        os.system(self.command)
        #print(self.command)



#testing that it works proper
if __name__ == '__main__':
    cam = StillCamera();
    cam.capture("GeneralTest.jpg");
    cam.clean();
    
    #Now let us test some effects
    #Testing the size
    cam.setSize('600', '400');
    cam.capture("TestSize.jpg");
    cam.clean();
    
    #Testing easy video sizer
    cam.setEasySize('small');
    cam.capture('TestEasy.jpg');
    cam.clean();
    
    #Testing the sharpness
    cam.setSharpness('1');
    cam.capture('TestSharpness.jpg');
    cam.clean();
    
    #Testing the quality
    cam.setQuality('1');
    cam.capture('TestQuality.jpg');
    cam.clean();
    
    #Testing the contrast
    cam.setContrast('1');
    cam.capture('TestContrast.jpg');
    cam.clean();
    
    #Testing the brightness
    cam.setBrightness('1');
    cam.capture('TestBrightness.jpg');
    cam.clean();
    
    #Testing the saturation
    cam.setSaturation('1');
    cam.capture('TestSaturation.jpg');
    cam.clean();

    #Testing the exposure
    cam.addExposure('beach');
    cam.capture('TestExposure.jpg');
    cam.clean();
    
    #Testing the whitebalance
    cam.addWhiteBalance('sun');
    cam.capture('TestWhiteBalance.jpg');
    cam.clean();
version = '0.6'




