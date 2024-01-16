
import pygame
import random
import sys
import time

pygame.display.set_caption("RistiNolla")

xwin = 0
owin = 0
tie = 0

Turn = random.randint(0,1)
GameOn = True
scrW = 800
scrH = 800
allW = 800
allH = 900

counter = 0

Voitto = False


Board = [0,0,0,0,0,0,0,0,0]

Moves = [0,1,2,3,4,5,6,7,8,]


def reset():
    global Board
    global Moves
    global GameOn
    global Turn
    global Voitto
    global counter

    Board = [0,0,0,0,0,0,0,0,0]
    Moves = [0,1,2,3,4,5,6,7,8,]
    GameOn = True
    Turn = random.randint(0,1)
    Voitto = False
    counter = 0

def TekstiRuutuun(Teksti):
    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render(Teksti, True, (0,0,0))
    temp_surface = pygame.Surface(txtsurf.get_size())
    temp_surface.fill((255, 255, 255))
    temp_surface.blit(txtsurf, (0, 0))
    text_rect = txtsurf.get_rect(center=(scrW/2, scrH/2))
    

    return screen.blit(temp_surface, text_rect)

def  PisteetRuutuun(x,o, t):
    Teksti = "X voitti: " + str(x) + "    O voitti: " + str(o) + "    tasapeli: " + str(t)
    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render(Teksti, True, (255, 255, 255))
    temp_surface = pygame.Surface(txtsurf.get_size())
    temp_surface.fill((0,0,0))
    temp_surface.blit(txtsurf, (0, 0))
    text_rect = txtsurf.get_rect(center=(scrW/2, allH-40))
    

    return screen.blit(temp_surface, text_rect)

def Voittiko(merkki):
    
    if Board[0] == merkki and Board[1] == merkki and Board[2] == merkki:
        return True
    elif Board[3] == merkki and Board[4] == merkki and Board[5] == merkki:
        return True
    elif Board[6] == merkki and Board[7] == merkki and Board[8] == merkki:
        return True
    elif Board[0] == merkki and Board[3] == merkki and Board[6] == merkki:
        return True
    elif Board[1] == merkki and Board[4] == merkki and Board[7] == merkki:
        return True
    elif Board[2] == merkki and Board[5] == merkki and Board[8] == merkki:
        return True
    elif Board[0] == merkki and Board[4] == merkki and Board[8] == merkki:
        return True
    elif Board[2] == merkki and Board[4] == merkki and Board[6] == merkki:
        return True
    else:
        return False
# Minimax liike
def AIMove(Board):

    Best_test = float("-inf")
    bestMove = 0

    for x in range(len(Board)):
        if Board[x] == 0:
            Board[x] = 2

            Move_test = Minimax(Board, 0 ,False)
            Board[x] = 0


            if Move_test > Best_test:
                bestMove = x
                Best_test = Move_test


    return bestMove

# Minimax algoritmi
def Minimax(Board, depth, maximizing_player):
     if Voittiko(2):
        Score = 1
        return Score
     elif Voittiko(1):
        Score = -1
        return Score
     elif Board.count(0) == 0:
        Score = 0
        return Score
     
     elif maximizing_player:
         MaxTest = float("-inf")
         for x in range(len(Board)):
            if Board[x] == 0:
                Board[x] = 2
                Test = Minimax(Board, depth +1 ,False)
                Board[x] = 0
                MaxTest = max(MaxTest, Test)
         return MaxTest

     elif maximizing_player == False :
        MinTest = float("inf")
        for x in range(len(Board)):
            if Board[x] == 0:
                Board[x] = 1
                Test = Minimax(Board, depth +1 ,True)
                Board[x] = 0
                MinTest = min(MinTest, Test)
        return MinTest


# pygame setup
pygame.init()
screen = pygame.display.set_mode((allW, allH))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(scrW / 2, scrH / 2)
player_pos1 = pygame.Vector2(scrW / 2,scrH / 2)
player_pos2 = pygame.Vector2(scrW / 2, scrH / 2)



size = [30,30]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    if GameOn == True:
        if Turn == 0:
            #X move
            xMove = AIMove(Board)
            #xMove = random.choice(Moves)
            Board[xMove] = 2
            Moves.remove(xMove)
            Turn = 1

        elif Turn == 1:
            #O move
            # Tässä satunnaiset siirrot
            """
            xMove = random.choice(Moves)
            Board[xMove] = 1
            Moves.remove(xMove)
            Turn = 0
            """
            mw2 = scrW/3
            mw4 = scrW/1.5
            #Tässä pelaaja pelaa hiirellä
            # Tunnista Hiiri painallus
            nappi = pygame.mouse.get_pressed()
            # Testaa mitä ruutua painetaan ja laita merkki siihen ruutuun jos vapaa. Muuten odota että löytyy vapaa ruutu
            if nappi[0] == True:
                kohta = pygame.mouse.get_pos()
                if kohta[0]<mw2 and kohta[1]< mw2: # Vasen ylä
                    liike = 0
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[0]>mw2 and kohta[1]< mw2 and kohta[0]<mw4: #Vasen keski
                    liike = 1
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[1]< mw2 and kohta[0]>mw4: # Vasen oikea
                    liike = 2
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[1]<mw4 and kohta[1]> mw2 and kohta[0]<mw2:# Keski vasen
                    liike = 3
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[0]>mw2 and kohta[1]> mw2 and kohta[1]<mw4 and kohta[0]<mw4:# Keski keski
                    liike = 4
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[0]>mw4 and kohta[1]> mw2 and kohta[1]<mw4:# Keski oikea
                    liike = 5
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[1]>mw4 and kohta[0]< mw2:# Ala vasen
                    liike = 6
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[0]>mw2 and kohta[1]> mw4 and kohta[0]<mw4:# Ala keski
                    liike = 7
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                elif kohta[0]>mw4 and kohta[1]> mw4:# Ala oikea
                    liike = 8
                    if Moves.count(liike)>0:
                        Board[liike] = 1
                        Moves.remove(liike)
                        Turn = 0
                
    

    # Täytä näyttö mustalla värillä jolla pyyhitään pois edelliset kuvat
    screen.fill("black")


    #Piirrä ruudukko
    pygame.draw.line(screen, "white",(scrW/3, 0), (scrW/3, scrH), 5)
    pygame.draw.line(screen, "white",(scrW/3*2, 0), (scrW/3*2, scrH), 5)
    pygame.draw.line(screen, "white",(0, scrH/3), (scrW, scrH/3), 5)
    pygame.draw.line(screen, "white",(0, scrH/3*2), (scrW, scrH/3*2), 5)
    pygame.draw.line(screen, "white",(0, scrH), (scrW, scrH), 5)

    # Piirrä pisteet
    PisteetRuutuun(xwin,owin, tie)


    spotx = (scrW/6,scrW/2,scrW/1.2)
    spoty = (scrH/6,scrH/2,scrH/1.2)

    county = 0
    countx = 0

    xw = int((scrW/8.5)*-1)

    for x in Board:      


        # Piirrä O ja X pelilautaan
        if x == 1:
            pygame.draw.circle(screen, "white",(spotx[countx], spoty[county]), scrW/7.5, 10 )
        elif x == 2:
            pygame.draw.line(screen, "white",(spotx[countx]-xw, spoty[county]-xw), (spotx[countx]+xw, spoty[county]+xw),5)
            pygame.draw.line(screen, "white",(spotx[countx]+xw, spoty[county]-xw), (spotx[countx]-xw, spoty[county]+xw),5)

        countx +=1


        if countx>=3:

            county +=1
            countx = 0

    
        
    # Voittiko X
        if Voittiko(2):
            GameOn = False
            Voitto = True
            TekstiRuutuun("X Voitti")
            counter +=1
            if counter >= 300:
                reset()
                xwin +=1
                



    # Voittiko O
        if Voittiko(1):
            GameOn = False
            Voitto = True
            TekstiRuutuun("O Voitti")
            counter +=1

            if counter >= 300:
                reset()
                owin +=1
                

  

    # Onko tasapeli
    if len(Moves) == 0 and Voitto == False:
        GameOn = False
        TekstiRuutuun("Tasapeli")
        counter +=1
        
        if counter >= 50:
            reset()
            tie +=1
            



    # näytä piirretyt objektit näytöllä
    pygame.display.flip()

    # rajoita FPS to 60

    dt = clock.tick(60) / 1000

    

pygame.quit()