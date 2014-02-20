#!/usr/bin/python


__author__ = 'kwekuq'





if __name__ == '__main__':
    from RaspiPyCam import Picture
    #

    cam = Picture.Camera()
    #print(Camera.command);
    #cam.setlocation("img/")
    #cam.capture("Kweku2.jpg")
    #cam.setSize("600","400")
    #cam.setEasySize("big")
    #cam.setEasySize("big")
    cam.setlocation('home/');
    cam.capture('james.jpg');
    #print("Kweku your command is ",  cam.command)
    #cam.clean();
    #cam.capture("Kweku11.jpg")
    #print("Kweku your clean command is ",  cam.command)
    print(__author__)

#Camera.__init__("Camera Module");
#Camera.setEasySize("huge");
#Camera.capture("Camera Module","Kwekuq.jpg");
#Camera.sayHi("Camera Moduldce");