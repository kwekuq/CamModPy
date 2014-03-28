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
    
    #Now let us test some built in effects
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
    cam = Camera.image().Off();
    
    #Now we can start to test video
    cam = Camera.video().On();
    #Let us test a general video
    cam.setName('testVideo');
    cam.setDuration('10');
    cam.setlocation('test');
    cam.capture();
    cam.clean();
    
    #Now let us test some effects
    #Testing the size
    cam.setName('testVideoSize');
    cam.setSize('400', '600');
    cam.setDuration('10');
    cam.setlocation('test');
    cam.capture();
    tool = Camera.tool().On();
    tool.setLocation('test');
    tool.transpose('testVideoSize');
    tool = Camera.tool().Off();
    cam.clean();
    
    #Testing easy video sizer
    cam.setName('testVideoSizer');
    cam.setEasySize('small');
    cam.setDuration('5');
    cam.setlocation('test');
    cam.capture();
    tool = Camera.tool().On();
    tool.setLocation('test');
    tool.transpose('testVideoSizer');
    tool = Camera.tool().Off();
    cam.clean();
    
    #Testing the sharpness
    cam.setName('TestSharpnessVid');
    cam.setSharpness('10');
    cam.setDuration('10');
    cam.setlocation('test');
    cam.capture();
    tool = Camera.tool().On();
    tool.setLocation('test');
    tool.transpose('TestSharpnessVid');
    tool = Camera.tool().Off();
    cam.clean();

    print(__author__)