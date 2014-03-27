from CamModPy import Picture
__author__ = 'kwekuq'

import time

import numpy
import Image
interval = 2;
Stop = False;
def setMotion():
    time.sleep(1);
    if( compare() == True):
        #Picture.capture(Picture,'normal.jpg');
        print('Motion detection in play');

def compare():
    img1 = Image.open('test.jpg')
    img2 = Image.open('test2.jpg')

    if img1.size != img2.size or img1.getbands() != img2.getbands():
        return -1

    s = 0
    for band_index, band in enumerate(img1.getbands()):
        m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
        m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
        s += numpy.sum(numpy.abs(m1-m2))
        if s > 3000000:
            #Take picture
            #Try find face
            #call the logger
            #send email

def detect():
    setMotion();
    while True:
        Picture.clean(Picture);
        Picture.capture(Picture,'check.jpg');
        compare();
        time.sleep(int(interval));


if __name__ == '__main__' :
    detect();

