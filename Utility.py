import pygame, os
from UtilityInterface import UtilityInterface

windowSize = width, height = 1024, 768

utilRectDict = {"tens" : (width-190, 275),
                "ones" : (width-90, 275),
                "frame" : (420, 310)}
preRectDict = {"/buttons/Power.png" : (width-75, 75),
               "/buttons/Upload.png" : (250, height-140),
               "/buttons/Get_Score.png" : (585, height-140)}

framePath = "/Empty_Picture_Frame.png"
backgroundPath = "/Background.png"

numPathList = ["/nums/Zero.png", "/nums/One.png",
               "/nums/Two.png", "/nums/Three.png",
               "/nums/Four.png", "/nums/Five.png",
               "/nums/Six.png", "/nums/Seven.png",
               "/nums/Eight.png", "/nums/Nine.png"]
buttonPathList = ["/buttons/Power.png",
                  "/buttons/Upload.png",
                  "/buttons/Get_Score.png"]
pressedButtonPathList = ["/buttons/Pressed_Power.png",
                         "/buttons/Pressed_Upload.png",
                         "/buttons/Pressed_Get_Score.png"]


class Utility(UtilityInterface):
    def __init__(self):
        self.path = os.path.realpath(os.path.expanduser('res'))
        self.utilRectDict = utilRectDict
        self.numPathList = numPathList
        self.screen = self.set_display()

        self.frameSurf = self.get_surf_from_path(self.path + framePath)
        self.frameRect = self.frameSurf.get_rect(center = self.utilRectDict["frame"])
        self.backgroundSurf = self.get_surf_from_path(self.path + backgroundPath)
        self.backgroundRect = self.backgroundSurf.get_rect()
    
        self.buttonSurfList = self.get_button_surf_list(buttonPathList)
        self.pressedButtonSurfList = self.get_pressed_button_surf_list(pressedButtonPathList)

        #Surface : Surface
        self.buttonSurfDict = self.get_button_surf_dict(self.buttonSurfList, self.pressedButtonSurfList)
        #Surface : Rect
        self.buttonRectDict = self.get_button_rect_dict()

    #Get dictionary of button rects
    def get_button_rect_dict(self):
        buttonRectDict = {}
        for index in range(len(buttonPathList)):
            surf = self.buttonSurfList[index]
            rect = surf.get_rect(center=preRectDict[buttonPathList[index]])
            buttonRectDict[surf] = rect
        return buttonRectDict

    #Set current pygame display
    def set_display(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        return pygame.display.set_mode(windowSize, pygame.NOFRAME)
