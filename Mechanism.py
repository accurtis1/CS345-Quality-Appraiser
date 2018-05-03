import pygame, os, tkinter
from MechanismInterface import MechanismInterface
from QualityAppraiser import QualityAppraiser
from Utility import Utility
from tkinter import filedialog

lowerKbBound = 20
upperKbBound = 10240
clientId = 'rWlrkeV8HRJ6FvoBfPrhzR1TdqNuY9vMN856YZ8v'
clientSecret = 'wY8pwK2J7FrqVGZx2oL4cvayzEP7Ab6JILBho0JKH6jNRiDEk3'


class Mechanism(MechanismInterface):
    def __init__(self):
        self.util = Utility()
        self.screen = self.util.screen

        self.tkinterRoot = tkinter.Tk()
        self.tkinterRoot.withdraw() #Hides the tkinter window that pops up

        self.qA = QualityAppraiser(clientId, clientSecret)
        self.qualityAppraiser = self.qA.get_token()
        self.url = 'https://api.everypixel.com/v1/quality'
        self.filedialog = filedialog

        self.eventDict = self.get_event_dict()

        self.userPath = None

        self.waitCursor = pygame.cursors.broken_x
        self.arrowCursor = pygame.cursors.arrow


    """Render"""
    #Render initial surfaces to display
    def render_display(self):
        #Draw background and frame
        self.draw_to_surface(self.screen, self.util.backgroundSurf, self.util.backgroundRect)
        self.draw_to_surface(self.screen, self.util.frameSurf, self.util.frameRect)
        #Draw buttons
        for s in self.util.buttonSurfList:
            self.draw_to_surface(self.screen, s, self.util.buttonRectDict[s])
        #Gather rects and render
        renderRects = [self.util.buttonRectDict[s] for s in self.util.buttonSurfList]
        renderRects.append(self.util.frameRect)
        renderRects.append(self.util.backgroundRect)
        self.update_display(renderRects)


    """User upload and API use"""
    #Set path and surface for user-selected image
    def get_user_image(self):
        try:
            self.userPath = self.get_path_from_file()
            imageSize = self.get_kb_size_from_path(self.userPath)
            if (self.check_image_size(imageSize, lowerKbBound, upperKbBound)):
                return self.userPath
            else:
                raise pygame.error("Image must be greater than 20 kb and less than 10 mb")
        except pygame.error:
            print(pygame.get_error())

    #Render user image to screen
    def display_user_image(self, imageSurf):
        try:
            userImage = self.get_scaled_surf(imageSurf, self.util.frameRect)
            self.draw_to_surface(self.screen, userImage, self.util.frameRect)
            self.update_display([self.util.frameRect])
        except pygame.error:
            print(pygame.get_error())

    #Get score from Everypixel API and render to screen
    def get_score_from_path(self, userPath):
        try:
            rawScore = self.get_raw_score_from_path(userPath)
            digitTup = self.get_digits_from_raw_score(rawScore)
            digitSurfTup = self.util.get_surf_from_digits(digitTup, self.util.numPathList)
            return digitSurfTup
        except pygame.error:
            print(pygame.get_error())

    #Render score to screen
    def display_score(self, digitSurfTup):
        try:
            self.draw_to_surface(self.screen, digitSurfTup[0], self.util.utilRectDict["tens"])
            self.draw_to_surface(self.screen, digitSurfTup[1], self.util.utilRectDict["ones"])
            self.update_display([self.util.utilRectDict["tens"], self.util.utilRectDict["ones"]])
        except pygame.error:
            print(pygame.get_error())

    #Full upload event
    def user_upload_event(self):
        userPath = self.get_user_image()
        userSurf = self.util.get_surf_from_path(userPath)
        self.display_user_image(userSurf)

    #Full score event
    def get_score_event(self):
        if self.userPath:
            digitSurfTup = self.get_score_from_path(self.userPath)
            self.display_score(digitSurfTup)
            self.userPath = None
        else:
            pass

    """Button events"""
    #Switch button with pressed image and returns pressed button
    def press_and_get_button(self, mousePos):
        rectDict = self.util.buttonRectDict
        surfDict = self.util.buttonSurfDict
        for bKey in surfDict:
            if rectDict[bKey].collidepoint(mousePos):
                self.draw_to_surface(self.screen, surfDict[bKey], rectDict[bKey])
                self.update_display([rectDict[bKey]])
                return surfDict[bKey]

    #Switch pressed button with button image
    def release_button(self, pressedButton):
        rectDict = self.util.buttonRectDict
        surfDict = self.util.buttonSurfDict
        for bKey, bValue in surfDict.items():
            if bValue is pressedButton:
                self.draw_to_surface(self.screen, bKey, rectDict[bKey])
                self.update_display([rectDict[bKey]])

    #Set button events
    def get_event_dict(self):
        surfList = self.util.pressedButtonSurfList
        eventDict = {surfList[0] : self.exit,
                     surfList[1] : self.user_upload_event,
                     surfList[2] : self.get_score_event}
        return eventDict
