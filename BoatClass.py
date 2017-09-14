import pygame

global imgdirectory
imgdirectory = 'Boats/'

'''barco() - class
shot() - class'''

class barco():
    def __init__(self, name, size, img=None, adjustx=0, adjusty=0):
        self.name = name
        self.size = size
        self.dmgtaken = 0
        self.x, self.y = adjustx, adjusty
        self.fliped = False
        try:
            self.img = pygame.image.load(imgdirectory+img)
        except TypeError:
            self.img = None

    def __len__(self):
        return(self.size)
    def __str__(self):
        return(self.name)
    def __bool__(self):
        if self.size == self.dmgtaken: return False
        return True

    def takingdmg(self):
        self.dmgtaken += 1

    def show(self, Display, x=0, y=0):
        Display.blit(self.img, (x + self.x, y + self.y))

    def flip(self):
        self.img = pygame.transform.rotate(self.img, 90)
        self.x, self.y = self.y, self.x
        self.fliped = not self.fliped

    def fix(self, x, y):
        self.x += x
        self.y += y


class shot():
    def __init__(self, x, y, hited):
        self.x, self.y = x, y
        if (hited and (self.x < 499 and self.y < 449)) or (not hited and (self.x > 499 or self.y > 449)): self.color = (0, 255, 0, 100)
        else: self.color = (255, 0, 0, 150)

    def show(self, Display):
        pygame.draw.rect(Display, self.color, (self.y, self.x, 22, 22))

    def __eq__(self, other):
        if (self.x, self.y) == other: return True
        return False

if __name__ == '__main__':
    import Jogo
    Jogo.Start()
