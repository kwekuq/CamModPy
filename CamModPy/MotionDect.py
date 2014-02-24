from CamModPy import Picture
__author__ = 'kwekuq'

import time



interval = 2;
Stop = False;
def setMotion():
    time.sleep(1);
    Picture.capture(Picture,'normal.jpg');
    print('Motion detection in play');

def compare():
    print("comparing");
    print("all clear at" + str(time.time()))
    return False;

def detect():
    setMotion();
    while True:
        Picture.clean(Picture);
        Picture.capture(Picture,'check.jpg');
        compare();
        time.sleep(int(interval));


if __name__ == '__main__' :
    detect();

