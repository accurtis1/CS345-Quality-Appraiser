import pygame, sys, os

class MechanismInterface:
    def __init__(self):
        raise NotImplementedError("Please use Mechanism implementation")


    """Display"""
    #Draw surface to canvas (usually the display)
    def draw_to_surface(self, canvasSurf, sourceSurf, destCoord, area=None):
        canvasSurf.blit(sourceSurf, destCoord, area)

    #Update display using multiple rects (instead of calling multiple times)
    def update_display(self, rectList):
        try:
            pygame.display.update(rectList)
        except pygame.error:
            print(pygame.get_error())

    #Scale surface to a specific width/height
    def get_scaled_surf(self, imageSurf, scaleRect):
        return pygame.transform.scale(imageSurf, (scaleRect.w, scaleRect.h))

    #Set mouse cursor
    def set_cursor(self, desiredCursor):
        pygame.mouse.set_cursor(*desiredCursor)


    """Events"""
    #Execute event
    def execute_event(self, pressedButtonSurf, eventDict):
        try:
            eventDict[pressedButtonSurf]()
        except pygame.error:
            print(pygame.get_error())


    """File selection"""
    #Select path from file
    def get_path_from_file(self):
        try:
            imagePath = self.filedialog.askopenfilename(initialdir = os.path.realpath,
                                                        title = "Select image",
                                                        filetypes = (("JPEG", "*.jpg"),
                                                                     ("PNG", "*.png")))
        except pygame.error:
            print(pygame.get_error())
        return imagePath

    #Get file size from path
    def get_kb_size_from_path(self, imagePath):
        try:
            with open(imagePath, "rb") as image:
                imageSize = os.path.getsize(image.name) / 1024
        except:
            print(pygame.get_error())
        return imageSize

    #Check if image size is valid for Everypixel
    def check_image_size(self, imageSize, lowerBound, upperBound):
        try:
            return (imageSize >= lowerBound and imageSize <= upperBound)
        except:
            print(pygame.get_error())


    """API use"""
    #Get raw score from API
    def get_raw_score_from_path(self, imagePath):
        try:
            with open(imagePath, 'rb') as image:
                data = {'data' : image}
                rawScore = self.qualityAppraiser.post(self.url,
                                                      files=data).json()
        except pygame.error:
            print(pygame.get_error())
        return rawScore

    #Get digits from raw score
    def get_digits_from_raw_score(self, rawScore):
        digitsStr = str(rawScore['quality']['score'] * 100)
        digitsTup = tensDig, onesDig = digitsStr[:1], digitsStr[1:2]
        return digitsTup


    """Exit"""
    def exit(self):
        pygame.display.quit()
        try:
            self.tkinterRoot.destroy()
        except:
            pass
        sys.exit()
