import pygame, sys

class UtilityInterface:
    def __init__(self):
        raise NotImplementedError("Please use Utility implementation")

    """Button/Image surfaces"""
    #Create surface from path
    def get_surf_from_path(self, imagePath):
        imageSurf = (pygame.image.load(imagePath)).convert_alpha()
        return imageSurf

    #Get list of button surfaces
    def get_button_surf_list(self, buttonPathList):
        return [self.get_surf_from_path(self.path + p) for p in buttonPathList]

    #Get list of pressed button surfaces
    def get_pressed_button_surf_list(self, pressedButtonPathList):
        return [self.get_surf_from_path(self.path + p) for p in pressedButtonPathList]

    #Get dictionary of button surfs : pressed button surfs
    def get_button_surf_dict(self, buttonSurfList, pressedButtonSurfList):
        buttonSurfDict = {}
        for s in buttonSurfList:
            buttonSurfDict[s] = pressedButtonSurfList[buttonSurfList.index(s)]
        return buttonSurfDict

    #Get surface objects from digits
    def get_surf_from_digits(self, digitsTup, numPathList):
        tensPath = self.path + numPathList[int(digitsTup[0])]
        onesPath = self.path + numPathList[int(digitsTup[1])]
        tensSurf = self.get_surf_from_path(tensPath)
        onesSurf = self.get_surf_from_path(onesPath)
        return (tensSurf, onesSurf)
