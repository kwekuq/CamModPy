__author__ = 'kwekuq'

import os;
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
    
    def __init__(self):
        self.command = "raspivid ";

    def setlocation(self, location):
        if self.imgLocation == False:
            os.system("mkdir -p /" + location)
            self.command = self.command + "/" + location +" ";
            self.imgLocation = True;
        else:
            print("Location has already been set, try running clean() if you wish to start over.");
    def setName(self, nameOfVid):
        self.command = self.command + "-o " + nameOfVid + ".h264 "
        
    def setSize(self, width, height):
        if self.imgSize == False:
            self.command = self.command + "-w " + width + " -h " + height + " "
            self.imgSize = True;
        else:
            print("Capture size has already been set, try running clean() if you wish to start over.");

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
            print("Sharpness has already been set, try running clean() if you wish to start over");

    def setBrightness(self, brightness):
        if self.imgBrightness == False:
            self.command = self.command + "-br " + int(brightness) + " ";
            self.imgBrightness = True;
        else:
            print("Brightness has already been set, try running clean() if you wish to start over");
            
    def setSaturation(self, saturation):
        if self.imgSaturation == False:
            self.command = self.command + "-sa " + int(saturation) + " ";
            self.imgSaturation = True;
        else:
            print("Saturation has already been set, try running clean() if you wish to start over");
            
    def setBitrate(self, bitrate):
        if self.imgBitrate == False:
            self.command = self.command + "-b " + int(bitrate) + " ";
            self.imgBitrate = True;
        else:
            print("bitrate has already been set, try running clean() if you wish to start over");
            
    def setDuration(self, duration):
        if self.imgDuration == False:
            self.command = self.command + "-t " + duration + " ";
            self.imgDuration = True;
        else:
            print("Saturation has already been set, try running clean() if you wish to start over");
            
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
        print("Clean up complete");

    def capture(self):
        #os.system(self.command + "-o " + FileName + ".h264")
        print(self.command)

if __name__ == "__main__":
    
    #Let us test a general video
    cam = MotionCamera();
    cam.setName('testVideo');
    cam.setDuration('10');
    #cam.setlocation('testVid');
    cam.capture();
    cam.clean();
    
    #Now let us test some effects
    #Testing the size
    cam.setName('testVideoSize');
    cam.setSize('400', '600');
    cam.setDuration('10');
    #cam.setlocation('testVid');
    cam.capture();
    cam.clean();
    
    #Testing easy video sizer
    cam.setName('testVideoSizer');
    cam.setEasySize('small');
    cam.setDuration('5');
    #cam.setlocation('testVid');
    cam.capture();
    cam.clean();
    
    #Testing the sharpness
    cam.setName('TestSharpnessVid');
    cam.setSharpness('10');
    cam.setDuration('10');
    #cam.setlocation('testVid');
    cam.capture();
    cam.clean();
    
    #test
    
    