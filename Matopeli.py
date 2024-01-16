import pygame
import random




f = open("C:\\Users\Jaakko Isokoski\muistio.txt", 'r')

nums = f.readlines()
savedScore = int(nums[0])

pygame.init()


window = (500, 500)

win = pygame.display.set_mode(window)

snake_speed = 15

fps = pygame.time.Clock()



y = 240
x = 240
xspeed = 20
yspeed = 0
foodPos = [0]
tail = 0
tailY = []
tailX = []
score = 0
maxScore = savedScore


def record (score1):
    global maxScore
     

    if maxScore < score1:
        maxScore = score1
        f = open("muistio.txt", "w")
        maxStr = str(maxScore)
        f.write(maxStr)
        f.close()
  
            





def main():

    global y 
    global x 
    global xspeed 
    global yspeed 
    global foodPos 
    global tail
    global tailY
    global tailX 
    global score
   
    

    #Skaalaa ruoan luomis kohdat
    for x in range(25):
        x *= 20
        foodPos.append(x)

    

    #Luo ruoka sijainti
    ypos = random.choice(foodPos)
    xpos = random.choice(foodPos)



    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for pos in range(tail):
            if tail > 1 and pos+1 >= tail :
                tailX.insert(pos+1, tailX[pos])
                tailY.insert(pos+1, tailY[pos])

        #Siirrä madon pään sijainti talteem
        tailX.insert(0, x)
        tailY.insert(0, y)

        #Luo ikkuna
        background = pygame.Surface(window)

        


        # Luo uusi ruoka, kun edellinen on syöty
        if x == xpos and y == ypos:
            ypos = random.choice(foodPos)
            xpos = random.choice(foodPos)
            
            #Tarkista ettei ruokaa luoda madon alle
            for food in tailX:    
                if xpos == food or xpos == x:
                    xpos = random.choice(foodPos)
                    food = 0

            for food in tailY:  
                if ypos == food or ypos == y:
                    ypos = random.choice(foodPos)
                    food = 0
            tail += 1
            score += 10
        
        
       
        #Liikuta matoa
        y -= yspeed
        x -= xspeed

        
        #Ohjaus
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xspeed = 20
                yspeed = 0



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xspeed = -20
                yspeed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                xspeed = 0
                yspeed = 20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                xspeed = 0
                yspeed = -20




        #Peli alkaa alusta jos mato karkaa reunojen ulkopuolelle
        if x > 481 or x < -1 or y > 481 or y < -1:
            x = 240
            y = 240
            tail = 0
            record (score)
            score = 0




   


        
        #Piirrä madon pää
        pygame.draw.rect(background,(255,20,147),(x,y,20,20))


        #Piirrä ruoka
        pygame.draw.rect(background,(255,255,0),(xpos,ypos,20,20))

        #Pirrä madon häntä
        for pos in range(tail):
            #Peli alkaa alusta jos pää osuu häntään
            if tailX[pos] == x and tailY[pos] == y:
                x = 240
                y = 240
                record (score)
                tail = 0
                score = 0

                
            #Muussa tapauksessa piirrä häntä
            else:
                pygame.draw.rect(background,(255,20,147),(tailX[pos],tailY[pos],20,20))

        point = str(score)
        font = pygame.font.SysFont(None, 24)
        MS = str(maxScore)

        # Piirrä pisteet
        img = font.render('Points: '+ point, True, (255,255,255))
        background.blit(img, (20, 20))

        # Piirrä ennätys
        img2 = font.render('Record: '+ MS, True, (255,255,255))
        background.blit(img2, (380, 20))



        
            
        win.blit(background,(0,0))
        
        pygame.display.update()

        #Pelin nopeus
        fps.tick(snake_speed)


                    
        

    pygame.quit()

if __name__ =="__main__":
    main()