import pygame
import BoatClass

'''mapa()
posboat()
Coordnates()
show()
check()'''

def mapa(Display, x, y, cor=(0, 0, 0)):
    pygame.draw.rect(Display, (82,212,235), (x, y, 375, 375))

    pygame.draw.line(Display, cor, (x + 23, y), (x + 23, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*1, y), (x + 23 + 25*1, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*2, y), (x + 23 + 25*2, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*3, y), (x + 23 + 25*3, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*4, y), (x + 23 + 25*4, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*5, y), (x + 23 + 25*5, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*6, y), (x + 23 + 25*6, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*7, y), (x + 23 + 25*7, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*8, y), (x + 23 + 25*8, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*9, y), (x + 23 + 25*9, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*10, y), (x + 23 + 25*10, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*11, y), (x + 23 + 25*11, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*12, y), (x + 23 + 25*12, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*14, y), (x + 23 + 25*14, y + 375), 3)
    pygame.draw.line(Display, cor, (x + 23 + 25*13, y), (x + 23 + 25*13, y + 375), 3)

    pygame.draw.line(Display, cor, (x, y + 23 + 25*0), (x + 375, y + 23 + 25*0), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*1), (x + 375, y + 23 + 25*1), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*2), (x + 375, y + 23 + 25*2), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*3), (x + 375, y + 23 + 25*3), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*4), (x + 375, y + 23 + 25*4), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*5), (x + 375, y + 23 + 25*5), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*6), (x + 375, y + 23 + 25*6), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*7), (x + 375, y + 23 + 25*7), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*8), (x + 375, y + 23 + 25*8), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*9), (x + 375, y + 23 + 25*9), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*10), (x + 375, y + 23 + 25*10), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*11), (x + 375, y + 23 + 25*11), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*12), (x + 375, y + 23 + 25*12), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*13), (x + 375, y + 23 + 25*13), 3)
    pygame.draw.line(Display, cor, (x, y + 23 + 25*14), (x + 375, y + 23 + 25*14), 3)

def posboat(x, y, ship, G):
    if G == 0:
        y -= 400
    elif G == 1:
        x -= 425
        y += 20
    
    if ship.fliped:
        y -= (25*len(ship))/2 - 12
    else:
        x -= (25*len(ship))/2 - 12

    if x < 48:
        x = 25
    elif x > 50 and x < 73:
        x = 50
    elif x > 75 and x < 98:
        x = 75
    elif x > 100 and x < 123:
        x = 100
    elif x > 125 and x < 148:
        x = 125
    elif x > 150 and x < 173:
        x = 150
    elif x > 175 and x < 198:
        x = 175
    elif x > 200 and x < 223:
        x = 200
    elif x > 225 and x < 248:
        x = 225
    elif x > 250 and x < 273:
        x = 250
    elif x > 275 and (x < 298 or (len(ship) == 5 and not ship.fliped)):
        x = 275
    elif x > 300 and (x < 323 or (len(ship) == 4 and not ship.fliped)):
        x = 300
    elif x > 325 and (x < 348 or (len(ship) == 3 and not ship.fliped)):
        x = 325
    elif x > 350 and (x < 373 or (len(ship) == 2 and not ship.fliped)):
        x = 350
    elif x > 375:
        x = 375

    if y < 123:
        y = 100
    elif y > 125 and y < 148:
        y = 125
    elif y > 150 and y < 173:
        y = 150
    elif y > 175 and y < 198:
        y = 175
    elif y > 200 and y < 223:
        y = 200
    elif y > 225 and y < 248:
        y = 225
    elif y > 250 and y < 273:
        y = 250
    elif y > 275 and y < 298:
        y = 275
    elif y > 300 and y < 323:
        y = 300
    elif y > 325 and y < 348:
        y = 325
    elif y > 350 and (y < 373 or (len(ship) == 5 and ship.fliped)):
        y = 350
    elif y > 375 and (y < 398 or (len(ship) == 4 and ship.fliped)):
        y = 375
    elif y > 400 and (y < 423 or (len(ship) == 3 and ship.fliped)):
        y = 400
    elif y > 425 and (y < 448 or (len(ship) == 2 and ship.fliped)):
        y = 425
    elif y > 450:
        y = 450

    if G == 0:
        y += 400
    elif G == 1:
        x += 425
        y -= 20
    
    return(x, y)

def Coordnates(boatpositions, newboat, x, y):
    coord = []
    if not newboat.fliped:
        for e in range(len(newboat)):
            coord.append((y, x+e*25))
    elif newboat.fliped:
        for e in range(len(newboat)):
            coord.append((y+25*e, x))

    for c in coord:
        if c in boatpositions:
            return(True, None)
    return(False, coord)
            
def show(Display, items):
    for item in items:
        if type(item) == BoatClass.barco or type(item) == BoatClass.shot:
            item.show(Display)
        else:
            pygame.draw.rect(Display, (0, 0, 0, 250), (*item[::-1], 22, 22))

def check(x, y, shots, G):
    j = k = None
    if G == 1:
        y += 20
    
    if x > 25 and x < 48:
        j = 25
    elif x > 50 and x < 73:
        j = 50
    elif x > 75 and x < 98:
        j = 75
    elif x > 100 and x < 123:
        j = 100
    elif x > 125 and x < 148:
        j = 125
    elif x > 150 and x < 173:
        j = 150
    elif x > 175 and x < 198:
        j = 175
    elif x > 200 and x < 223:
        j = 200
    elif x > 225 and x < 248:
        j = 225
    elif x > 250 and x < 273:
        j = 250
    elif x > 275 and x < 298:
        j = 275
    elif x > 300 and x < 323:
        j = 300
    elif x > 325 and x < 348:
        j = 325
    elif x > 350 and x < 373:
        j = 350
    elif x > 375 and x < 398:
        j = 375

    if y > 100 and y < 123:
        k = 100
    elif y > 125 and y < 148:
        k = 125
    elif y > 150 and y < 173:
        k = 150
    elif y > 175 and y < 198:
        k = 175
    elif y > 200 and y < 223:
        k = 200
    elif y > 225 and y < 248:
        k = 225
    elif y > 250 and y < 273:
        k = 250
    elif y > 275 and y < 298:
        k = 275
    elif y > 300 and y < 323:
        k = 300
    elif y > 325 and y < 348:
        k = 325
    elif y > 350 and y < 373:
        k = 350
    elif y > 375 and y < 398:
        k = 375
    elif y > 400 and y < 423:
        k = 400
    elif y > 425 and y < 448:
        k = 425
    elif y > 450 and y < 473:
        k = 450

    if G == 1 and type(k) == int:
        k -= 20

    if ((k, j) not in shots) and k and j:
        return(False, (k, j))
    return(True, None)

if __name__ == '__main__':
    import Jogo
    Jogo.Start()
