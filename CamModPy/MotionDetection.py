'''
Created on 23 Feb 2014

@author: kwekuq
'''
import Image
import numpy
import sys

def main():
    img1 = Image.open('test.jpg')
    img2 = Image.open('test2.jpg')

    if img1.size != img2.size or img1.getbands() != img2.getbands():
        return -1

    s = 0
    for band_index, band in enumerate(img1.getbands()):
        m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
        m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
        s += numpy.sum(numpy.abs(m1-m2))
    print s

if __name__ == "__main__":
    sys.exit(main())
    
    