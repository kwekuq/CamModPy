#!/usr/bin/python


__author__ = 'kwekuq'

import Camera



if __name__ == '__main__':
    cam = Camera.image().On();
    cam.clean();
    print(cam.message);
    cam = Camera.image().Off(); #This is not necessary at all, but is good practice. If you switch it on, switch it off when you are done with it.
    cam = Camera.video().On();
    cam.clean();
    print(cam.message);
    cam = Camera.video().Off(); #This is not necessary at all, but is good practice. If you switch it on, switch it off when you are done with it.


    cam = Camera.image().On();
    cam.clean();
    print(cam.message);
    cam.setlocation("test");
    print(cam.message);
    cam.capture("GeneralTest.jpg");
    print(cam.message);
    cam.clean();
    print(cam.message);
    
    #Now let us test some effects
    #Testing the size
    cam.setSize('600', '400');
    cam.setlocation("test");
    print(cam.message);
    cam.capture("TestSize.jpg");
    print(cam.message);
    cam.clean();
    
    #Testing easy video sizer
    cam.setEasySize('small');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestEasy.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the sharpness
    cam.setSharpness('50');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestSharpness.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the quality
    cam.setQuality('30');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestQuality.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the contrast
    cam.setContrast('50');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestContrast.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the brightness
    cam.setBrightness('50');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestBrightness.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the saturation
    cam.setSaturation('50');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestSaturation.jpg');
    print(cam.message);
    cam.clean();

    #Testing the exposure
    cam.addExposure('beach');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestExposure.jpg');
    print(cam.message);
    cam.clean();
    
    #Testing the whitebalance
    cam.addWhiteBalance('sun');
    cam.setlocation("test");
    print(cam.message);
    cam.capture('TestWhiteBalance.jpg');
    print(cam.message);
    cam.clean();


    #print(Camera.command);
    #cam.setlocation("img/")
    #cam.capture("Kweku2.jpg")
    #cam.setSize("600","400")
    #cam.setEasySize("big")
    #cam.setEasySize("big")
    #cam.setlocation('home/');
    #cam.capture('james.jpg');
    #print("Kweku your command is ",  cam.command)
    #cam.clean();
    #cam.capture("Kweku11.jpg")
    #print("Kweku your clean command is ",  cam.command)
    print(__author__)

#Camera.__init__("Camera Module");
#Camera.setEasySize("huge");
#Camera.capture("Camera Module","Kwekuq.jpg");
#Camera.sayHi("Camera Moduldce");