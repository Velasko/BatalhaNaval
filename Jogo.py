import pygame, sys, connect, Functions, BoatClass, tkinter
from pygame.locals import *

def Start():

    #making the connection
    connection, server = connect.conn()
    print('Connected')
    
    #Creating the variables
    resolution = ((425, 900), (850, 475))
        #txt
    titlebox = ((212, 30), (425, 30))
    enrec = ((212, 70), (212, 60))
    myrec = ((212, 485), (637, 60))
    msg1 = ((65, 197), (65, 177))
    msg2 = ((105, 247), (105, 227))
    wmsg1 = ((120, 197), (120, 177))
    wmsg2 = ((85, 247), (85, 227))
    entmsg1 = ((77, 147), (77, 127))
    entmsg2 = ((77, 197), (77, 177))
    mytmsg1 = ((155, 547), (580, 127))
    mytmsg2 = ((39, 597), (464, 177))
    mytmsg3 = ((90, 647), (515, 227))
    mytmsg4 = ((132, 697), (557, 277))
    GOtxt = ((95, 260), (95,200))
    finaltxt = ((210, 340), (210,275))
        #maps
    enmap = ((25, 100), (25, 80))
    mymap = ((25, 500), (450, 80))

    sombra = (125, 125, 125, 120)
    Fundo = (2, 100, 100)
    LetterColor = (255, 255, 255, 000)

    barcos = {'portaviao' : BoatClass.barco('Porta Avião', 5, 'portavioes.png', *(9, 0)),
              'destroyer' : BoatClass.barco('Destroyer', 4, 'destroyer.png', *(1, 3)),
              'cruzador' : BoatClass.barco('Cruzador', 4, 'cruiser.png', *(2, 6)),
              'submarino' : BoatClass.barco('Submarino', 3, 'submarine.png', *(1, 6)),
              'patrulha': BoatClass.barco('Patrulha', 2, 'patrulha.png', *(2, 9))}
    btpos = []
    boatalreadysets = []
    shotsfired = []
    hits = 0
    
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    #defines the position of all items in game screen based in resolution
    if height >=950:
        G = 0
    else: G = 1

    connection.send(G)
    Ge = connection.recv()

    if G != Ge:
        cooradjust = ((425, -20), (0, 420))
    else:
        cooradjust = ((0, 400), (425, 0))

    #initializing pygame
    pygame.init()
    Display = pygame.display.set_mode((resolution[G]))
    Alfa = Display.convert_alpha()
    shadow = Display.convert_alpha()
    pygame.display.set_caption('Batalha Naval')
    fpsClock = pygame.time.Clock()

    #creating main texts
    Fonte = pygame.font.Font('freesansbold.ttf', 30)
    title = pygame.font.Font('freesansbold.ttf', 40).render('Batalha Naval!', True, LetterColor, Fundo)
    titlerect = title.get_rect()
    titlerect.center = titlebox[G]
    message1 = Fonte.render('Posicione os navios', True, LetterColor)
    message2 = Fonte.render('em seu mapa.', True, LetterColor)
    fonte = pygame.font.Font('freesansbold.ttf', 20)
    enemytop = fonte.render('Mapa Inimigo', True, LetterColor, Fundo)
    enrect = enemytop.get_rect()
    enrect.center = enrec[G]
    mytop = fonte.render('Seu mapa', True, LetterColor, Fundo)
    myrect = mytop.get_rect()
    myrect.center = myrec[G]
    myturnmsg1 = Fonte.render('Sua vez,', True, LetterColor)
    myturnmsg2 = Fonte.render('clique em um quadrado', True, LetterColor)
    myturnmsg3 = Fonte.render('do mapa inimigo', True, LetterColor)
    myturnmsg4 = Fonte.render('para atirar', True, LetterColor)
    enturn1 = Fonte.render('Vez do adversario,', True, LetterColor)
    enturn2 = Fonte.render('por favor, aguarde.', True, LetterColor)
    waitmessage1 = Fonte.render('Conectando', True, LetterColor)
    waitmessage2 = Fonte.render('Por favor, espere...', True, LetterColor)
    
    #Positioning ships
    x, y  = mymap[G][0], mymap[G][1] #initial boat position
    for ship in barcos.values():
        Ready = False   #When boat is positioned, leaves the loop
        while not Ready:

            #base img of game
            Display.fill(Fundo)
            shadow.fill((0, 0, 0, 0))
            pygame.draw.rect(shadow, sombra, (*enmap[G], 372, 372)) #shadow over enmap
                #shows squares/buttons
            Functions.mapa(Display, *enmap[G], Fundo)
            Functions.mapa(Display, *mymap[G], Fundo)
                #cast the shadow
            Display.blit(shadow, (0, 0))
                #shows txt
            Display.blit(title, titlerect)
            Display.blit(enemytop, enrect)
            Display.blit(mytop, myrect)
            Display.blit(message1, msg1[G])
            Display.blit(message2, msg2[G])
                #show boats
            Functions.show(Display, boatalreadysets)
            ship.show(Display, x, y)
            
            for event in pygame.event.get():
                #close game
                if event.type == QUIT:
                    pygame.quit()
                    connection.close()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    #fixing boat position - left click
                    conflicted, coord = Functions.Coordnates(btpos, ship, x, y)
                    if event.button == 1 and not conflicted:
                        ship.fix(x, y)
                        btpos += coord[::-1]
                        boatalreadysets.append(ship)
                        Ready = True
                    #spinning boat - right click
                    elif event.button == 3:
                        ship.flip()
                        x, y = Functions.posboat(*event.pos, ship, G)
                #keeping boat near the mouse
                if event.type == MOUSEMOTION:
                    x, y = Functions.posboat(*event.pos, ship, G)
            #refresing screen
            pygame.display.update()
            fpsClock.tick(30)
            
    try: #in case there's a connection error, closes it all
        #img while wait the other get ready
        Display.fill(Fundo)
        Display.blit(title, titlerect)
        Display.blit(enemytop, enrect)
        Display.blit(mytop, myrect)
            #shows squares/buttons
        Functions.mapa(Display, *enmap[G], Fundo)
        Functions.mapa(Display, *mymap[G], Fundo)
            #shadow over enmap
        pygame.draw.rect(shadow, sombra, (*enmap[G], 372, 372))
        Display.blit(shadow, (0, 0))
            #show boats
        Functions.show(Display, boatalreadysets)
        #ship.show(Display, x, y)   <- nao tenho ideia do que eh... ta ai, pq vai que...
            #show wait message
        Display.blit(waitmessage1, wmsg1[G])
        Display.blit(waitmessage2, wmsg2[G])
        pygame.display.update()

        #Defining who plays first - who is read firs begin
        ismyturn = True
        ready = False
        if connection.poll():
            ismyturn = False
            recv = connection.recv()
            otherturn, ready = recv[0], recv[1]
        connection.send((ismyturn, True))
        
        #if ready first, waiting for oponent to get ready
        while not ready:
            for event in pygame.event.get():
                #close game
                if event.type == QUIT:
                    pygame.quit()
                    connection.close()
                    sys.exit()
            if connection.poll():
                pygame.display.update()
                recv = connection.recv()
                otherturn, ready = recv[0], recv[1]
                
        
            #if ready at same time, host begins
        if otherturn and ismyturn:
            try:
                server += 1
            except NameError:
                ismyturn = False
            except TypeError:
                ismyturn = True

        #begining actual game loop
        #hits : number of hits on enemies boats. 18 needed to win
        #len(btpos) : number of hits until theres no ship left
        while hits != 18 and len(btpos) != 0:

            #base img of the game
            Display.fill(Fundo)
            Alfa.fill((0, 0, 0, 0))
            shadow.fill((0, 0, 0, 0))
                #show base txt
            Display.blit(title, titlerect)
            Display.blit(enemytop, enrect)
            Display.blit(mytop, myrect)
            
            #Functions.show(Alfa, btpos) #<- show where the boats are located 4 dmg
                #shows squares/buttons
            Functions.mapa(Display, *enmap[G], Fundo)
            Functions.mapa(Display, *mymap[G], Fundo)
                #show boats and shots taken
            Functions.show(Display, boatalreadysets)
            Functions.show(Alfa, shotsfired)

            for event in pygame.event.get():
                    #closing game
                if event.type == QUIT:
                    pygame.quit()
                    connection.close()
                    sys.exit()
                    
                if event.type == MOUSEBUTTONDOWN:
                    if ismyturn:
                        #Checking if shot already made at that coordinate
                        conflicted, coord = Functions.check(*event.pos, shotsfired, G)
                        if not conflicted:
                            #sending coordinate w/ map correction
                            connection.send((coord[0]+cooradjust[G][1], coord[1]+cooradjust[G][0]))
                            #feedback if hited a ship
                            hited = connection.recv()
                            #registering shot
                            shotsfired.append(BoatClass.shot(*coord, hited))
                            #end of my turn
                            ismyturn = False
                            if hited:
                                hits += 1                               
            if not ismyturn:
                #enemys turn drawing
                pygame.draw.rect(shadow, sombra, (*enmap[G], 372, 372))
                Display.blit(shadow, (0, 0))
                Display.blit(Alfa, (0, 0))
                    #enemy turn text
                Display.blit(enturn1, entmsg1[G])
                Display.blit(enturn2, entmsg2[G])
                if connection.poll():
                    #recieving shot coordinates
                    tiro = connection.recv()
                    #checking if hited a boat
                    hited = False
                    if tiro in btpos:
                        hited = True
                        btpos.remove(tiro)
                    #return if hited
                    connection.send(hited)
                    #registering shot
                    shotsfired.append(BoatClass.shot(*tiro, hited))
                    #end of enemys turn
                    ismyturn = True
            else:
                #my turn drawing
                pygame.draw.rect(shadow, sombra, (*mymap[G], 372, 372))
                Display.blit(shadow, (0, 0))
                Display.blit(Alfa, (0, 0))
                    #my turn msg
                Display.blit(myturnmsg1, mytmsg1[G])
                Display.blit(myturnmsg2, mytmsg2[G])
                Display.blit(myturnmsg3, mytmsg3[G])
                Display.blit(myturnmsg4, mytmsg4[G])
                
            pygame.display.update()
            fpsClock.tick(30)
    except EOFError:
        pygame.quit()
        print('Erro de Conexao.')
        sys.exit()

    connection.close()
    gameover = pygame.font.Font('freesansbold.ttf', 40).render('Game Over!', True, LetterColor, Fundo)
    if hits == 18:
        final = pygame.font.Font('freesansbold.ttf', 40).render('You Win!', True, LetterColor, Fundo)
    else: final = pygame.font.Font('freesansbold.ttf', 40).render('You Lose!', True, LetterColor, Fundo)
    finalrect = final.get_rect()
    finalrect.center = finaltxt[G]

    while True:
        #base img of the game
        Display.fill(Fundo)
        Alfa.fill((0, 0, 0, 0))
        shadow.fill((0, 0, 0, 0))
            #show base txt
        Display.blit(title, titlerect)
        Display.blit(enemytop, enrect)
        Display.blit(mytop, myrect)
            #shows squares/buttons
        Functions.mapa(Display, *enmap[G], Fundo)
        Functions.mapa(Display, *mymap[G], Fundo)
            #show boats and shots taken
        Functions.show(Display, boatalreadysets)
        Functions.show(Alfa, shotsfired)
        pygame.draw.rect(shadow, sombra, (*enmap[G], 372, 372))
        pygame.draw.rect(shadow, sombra, (*mymap[G], 372, 372))
        Display.blit(shadow, (0, 0))
        Display.blit(Alfa, (0, 0))
            #show 'Game Over' and the winner
        Display.blit(final, finalrect)
        Display.blit(gameover, GOtxt[G])
        pygame.display.update()

        for event in pygame.event.get():
            #closing game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    Start()

#hehe 24.1.17
