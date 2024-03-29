import random 
import sys 
import pygame
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 16
SCREENWIDTH = 900
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT -36
ROOFY = - 2
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/kirby2_crop.png'
BACKGROUND = 'gallery/sprites/kirby_background.png'
PIPE = 'gallery/sprites/pipe_big.png'

WINNING = 5

def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                #SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))   
                SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))  
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def winningScreen(winner):
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)


    messagex = int((SCREENWIDTH - GAME_SPRITES['winning'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    print("WINNER", winner)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            #elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
            #    return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                #SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))   
                #SCREEN.blit(GAME_SPRITES['player_2'], (playerx_2, playery_2))  
                SCREEN.blit(GAME_SPRITES['winning'], (messagex,messagey ))    
                #SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))   
                #SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))
                #SCREEN.blit(GAME_SPRITES['base_2'], (basex_2, GROUNDY_2))   
                #SCREEN.blit(GAME_SPRITES['roof_2'], (basex_2, ROOFY_2)) 
                if winner==1:
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))   

                SCREEN.blit(GAME_SPRITES['numbers'][winner], (SCREENWIDTH/2 - 5, SCREENHEIGHT +30))  
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    # Values from code
    #pipeVelX = -4

    # playerVelY is what gives the gravity feature
    #playerVelY = -9
    #playerMaxVelY = 10
    #playerMinVelY = -8
    #playerAccY = 1

    #playerFlapAccv = -8 # velocity while flapping

    # Trial values
    pipeVelX = -4

    # playerVelY is what gives the gravity feature
    playerVelY = -10
    playerMaxVelY = 10
    playerMinVelY = -3
    playerAccY = 3

    playerFlapAccv = -20 # velocity while flapping

    
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # Reducing the roof boundary: how to set it as if it were soldi?
                #if playery > 0:
                if playery > ROOFY + GAME_SPRITES['roof'].get_height():
                    #print(ROOFY, playerHeight)
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    # Removed sound when pressing space!
                    #GAME_SOUNDS['wing'].play()
            else:
                playerFlapped = False


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            pipeVelX = 0
        else:
            pipeVelX = -4

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()


        if score > WINNING:
            GAME_SOUNDS['point'].play()
            return 1

        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        #if playerFlapped:
        #    playerFlapped = False        
        #     
        playerHeight = GAME_SPRITES['player'].get_height()

        old_playery = playery
        playery = old_playery + min(playerVelY, GROUNDY - old_playery - playerHeight)

        # Added roof boundary
        if old_playery < ROOFY + GAME_SPRITES['roof'].get_height(): 
            playery = max(old_playery + playerVelY, ROOFY + GAME_SPRITES['roof'].get_height() + playerVelY)

            #playery = ROOFY + GAME_SPRITES['roof'].get_height()

        # Add here logic pipes:
        # logic to stay on top of pipes and don't crash inside them

        playerWidth = GAME_SPRITES['player'].get_width() 
            
        pipe = upperPipes[0]
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        pipeWidth = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] \
           and playerx + playerWidth > pipe['x'] \
           and playerx < pipe['x'] + pipeWidth:
            if not crashTest:
                playery = max(old_playery + playerVelY, pipe['y']+ pipeHeight, pipe['y']+ pipeHeight + playerVelY)

        pipe = lowerPipes[0]
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] \
            and playerx + playerWidth > pipe['x'] \
            and playerx < pipe['x'] + pipeWidth:
            if not crashTest:
                playery = old_playery + min(playerVelY, pipe['y'] - old_playery - playerHeight)

        # if the pipe starts getting out of the screen need to check it is not too far
        if pipe['x'] + pipeWidth > 0 and pipe['x']<=0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            playery = old_playery + min(playerVelY, GROUNDY - old_playery - playerHeight)

            # Added roof boundary
            if old_playery < ROOFY + GAME_SPRITES['roof'].get_height(): 
                playery = max(old_playery + playerVelY, ROOFY + GAME_SPRITES['roof'].get_height()+ playerVelY)


        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        # Adding floor and roof
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    # Removed hit noise when hitting the roof
    #if playery> GROUNDY - 25  or playery < 0: 
    #    GAME_SOUNDS['hit'].play()
    #    return True

    # change isCollide to only vertical touches, not also horizontally
    # If we touch on top or on bottom is not a problem
    
    collision = False

    #for pipe in upperPipes:
    #    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    #    if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
    #        #GAME_SOUNDS['hit'].play()
    #        collision = True

    #for pipe in lowerPipes:
    #    if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
    #        #GAME_SOUNDS['hit'].play()
    #        collision = True

    playerWidth = GAME_SPRITES['player'].get_width() 
        
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        pipeWidth = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] \
            and playerx + playerWidth > pipe['x'] \
            and playerx < pipe['x'] + pipeWidth \
            and playerx - pipe['x'] <= pipeWidth:
            collision = True

        if pipe['x'] + pipeWidth > 0 and pipe['x']<=0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            collision = False
            

    for pipe in lowerPipes:
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] \
            and playerx + playerWidth > pipe['x'] \
            and playerx < pipe['x'] + pipeWidth \
            and playerx - pipe['x'] <= pipeWidth:
                collision = True

        if pipe['x'] + pipeWidth > 0 and pipe['x']<=0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            collision = False

    return collision

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 5
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # Main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('KirbEEG by Group 2')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/kirby_welcome.png').convert_alpha()
    GAME_SPRITES['winning'] =pygame.image.load('gallery/sprites/winning.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/floor_try.png').convert_alpha()
    GAME_SPRITES['roof'] =pygame.image.load('gallery/sprites/roof_try.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        result = mainGame() # This is the main game function 
        if result is not None:
            winningScreen(result)
