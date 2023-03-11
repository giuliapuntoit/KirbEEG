import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports

# Global Variables for the game
FPS = 16
SCREENWIDTH = 800
TOTAL_SCREENHEIGHT = 600
SCREENHEIGHT = TOTAL_SCREENHEIGHT / 2
SCREEN = pygame.display.set_mode((SCREENWIDTH, TOTAL_SCREENHEIGHT))

GROUNDY = SCREENHEIGHT - 36
ROOFY = -2

GROUNDY_2 = TOTAL_SCREENHEIGHT - 36
ROOFY_2 = SCREENHEIGHT + 2

GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/kirby2_crop.png'
PLAYER_2 = 'gallery/sprites/kirby2_crop.png'
# BACKGROUND = 'gallery/sprites/kirby_background.png'
BACKGROUND = 'players2/kirby_background_small.png'
PIPE = 'gallery/sprites/pipe_dim_medium.png'
PIPESMALL = 'gallery/sprites/pipe_dim_small.png'
PIPEBIG = 'gallery/sprites/pipe_dim_big.png'
WINNING = 5


def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)

    playerx_2 = int(SCREENWIDTH / 5)
    playery_2 = int(SCREENWIDTH / 2 + SCREENHEIGHT)

    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    basex_2 = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY + 18))
                # SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                # SCREEN.blit(GAME_SPRITES['player_2'], (playerx_2, playery_2))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))
                SCREEN.blit(GAME_SPRITES['base_2'], (basex_2, GROUNDY_2))
                SCREEN.blit(GAME_SPRITES['roof_2'], (basex_2, ROOFY_2))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))

                pygame.display.update()
                FPSCLOCK.tick(FPS)


def winningScreen(winner):
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)

    playerx_2 = int(SCREENWIDTH / 5)
    playery_2 = int(SCREENWIDTH / 2 + SCREENHEIGHT)

    messagex = int((SCREENWIDTH - GAME_SPRITES['winning'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    basex_2 = 0
    print("WINNER", winner)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            # elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
            #    return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                # SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                # SCREEN.blit(GAME_SPRITES['player_2'], (playerx_2, playery_2))
                SCREEN.blit(GAME_SPRITES['winning'], (messagex, messagey))
                # SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                # SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))
                # SCREEN.blit(GAME_SPRITES['base_2'], (basex_2, GROUNDY_2))
                # SCREEN.blit(GAME_SPRITES['roof_2'], (basex_2, ROOFY_2))
                #if winner == 1:
                #    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                #else:
                #    SCREEN.blit(GAME_SPRITES['player_2'], (playerx_2, playery_2))

                SCREEN.blit(GAME_SPRITES['numbers'][winner], (SCREENWIDTH / 2 - 5, SCREENHEIGHT + 30))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    score_2 = 0
    playerx_2 = int(SCREENWIDTH / 5)
    playery_2 = int(SCREENWIDTH / 2 + SCREENHEIGHT)
    basex_2 = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # Create 2 pipes for blitting on the screen
    newPipe1_2 = getRandomPipe_2()
    newPipe2_2 = getRandomPipe_2()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y'], 'type': newPipe1[0]['type']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y'], 'type': newPipe2[0]['type']}
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y'], 'type': newPipe1[1]['type']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y'], 'type': newPipe2[1]['type']},
    ]

    # my List of upper pipes
    upperPipes_2 = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1_2[0]['y'], 'type': newPipe1_2[0]['type']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2_2[0]['y'], 'type': newPipe2_2[0]['type']},
    ]
    # my List of lower pipes
    lowerPipes_2 = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1_2[1]['y'], 'type': newPipe1_2[1]['type']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2_2[1]['y'], 'type': newPipe2_2[1]['type']},
    ]

    # Values from code
    pipeVelX = -4
    pipeVelX_2 = -4

    # I think playerVelY is what gives the gravity feature
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerVelY_2 = -9
    playerMaxVelY_2 = 10
    playerMinVelY_2 = -8
    playerAccY_2 = 1

    playerFlapAccv = -10  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    playerFlapAccv_2 = -10  # velocity while flapping
    playerFlapped_2 = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # TODO here we probably need to define another keyboard input to get down (if no gravity)
            if event.type == KEYDOWN and (event.key == K_a):
                # Reducing the roof boundary: how to set it as if it were soldi?
                # if playery > 0:
                if playery > ROOFY + GAME_SPRITES['roof'].get_height():
                    # print(ROOFY, playerHeight)
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    # Removed sound when pressing space!
                    # GAME_SOUNDS['wing'].play()
            # Adding keyboard pressed keeps jumping
            else:
                playerFlapped = False
            if event.type == KEYDOWN and (event.key == K_b):
                if playery_2 > ROOFY_2 + GAME_SPRITES['roof_2'].get_height():
                    playerVelY_2 = playerFlapAccv_2
                    playerFlapped_2 = True
            else:
                playerFlapped_2 = False

        crashTest = isCollide(playerx, playery, upperPipes,
                              lowerPipes)  # This function will return true if the player is crashed
        crashTest_2 = isCollide_2(playerx_2, playery_2, upperPipes_2,
                                  lowerPipes_2)  # This function will return true if the player is crashed

        if crashTest:
            pipeVelX = 0
        else:
            pipeVelX = -4

        if crashTest_2:
            pipeVelX_2 = 0
        else:
            pipeVelX_2 = -4

        # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            # TODO probably need to change this + 4 value too
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your score is {score}")
                # GAME_SOUNDS['point'].play()

        # check for score
        playerMidPos_2 = playerx_2 + GAME_SPRITES['player_2'].get_width() / 2
        for pipe_2 in upperPipes_2:
            pipeMidPos_2 = pipe_2['x'] + GAME_SPRITES['pipe_2'][0].get_width() / 2
            # TODO probably need to change this + 4 value too
            if pipeMidPos_2 <= playerMidPos_2 < pipeMidPos_2 + 4:
                score_2 += 1
                print(f"P2: Your score is {score_2}")
                # GAME_SOUNDS['point'].play()

        if score > WINNING:
            GAME_SOUNDS['point'].play()
            return 1

        elif score_2 > WINNING:
            GAME_SOUNDS['point'].play()
            return 2

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerVelY_2 < playerMaxVelY_2 and not playerFlapped_2:
            playerVelY_2 += playerAccY_2

        # if playerFlapped:
        #    playerFlapped = False

        # if playerFlapped_2:
        #    playerFlapped_2 = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playerHeight_2 = GAME_SPRITES['player_2'].get_height()

        old_playery = playery
        playery = old_playery + min(playerVelY, GROUNDY - old_playery - playerHeight)

        old_playery_2 = playery_2
        playery_2 = old_playery_2 + min(playerVelY_2, GROUNDY_2 - old_playery_2 - playerHeight_2)

        # Added roof boundary
        if old_playery < ROOFY + GAME_SPRITES['roof'].get_height():
            playery = max(old_playery + playerVelY, ROOFY + GAME_SPRITES['roof'].get_height() + playerVelY)

        # Added roof boundary
        if old_playery_2 < ROOFY_2 + GAME_SPRITES['roof_2'].get_height():
            playery_2 = max(old_playery_2 + playerVelY_2, ROOFY_2 + GAME_SPRITES['roof_2'].get_height() + playerVelY_2)

        playerWidth = GAME_SPRITES['player'].get_width()
        playerWidth_2 = GAME_SPRITES['player_2'].get_width()

        pipe = upperPipes[0]
        pipeHeight = GAME_SPRITES[pipe['type']][0].get_height()
        pipeWidth = GAME_SPRITES['pipe'][0].get_width()

        pipe_2 = upperPipes_2[0]
        pipeHeight_2 = GAME_SPRITES[pipe_2['type']][0].get_height()
        pipeWidth_2 = GAME_SPRITES['pipe_2'][0].get_width()

        if playery < pipeHeight + pipe['y'] \
                and playerx + playerWidth > pipe['x'] \
                and playerx < pipe['x'] + pipeWidth:
            if not crashTest:
                playery = max(old_playery + playerVelY, pipe['y'] + pipeHeight, pipe['y'] + pipeHeight + playerVelY)

        if playery_2 < pipeHeight_2 + pipe_2['y'] \
                and playerx_2 + playerWidth_2 > pipe_2['x'] \
                and playerx_2 < pipe_2['x'] + pipeWidth_2:
            if not crashTest_2:
                playery_2 = max(old_playery_2 + playerVelY_2, pipe_2['y'] + pipeHeight_2,
                                pipe_2['y'] + pipeHeight_2 + playerVelY_2)

        pipe = lowerPipes[0]
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] \
                and playerx + playerWidth > pipe['x'] \
                and playerx < pipe['x'] + pipeWidth:
            if not crashTest:
                playery = old_playery + min(playerVelY, pipe['y'] - old_playery - playerHeight)

        pipe_2 = lowerPipes_2[0]
        if playery_2 + GAME_SPRITES['player_2'].get_height() > pipe_2['y'] \
                and playerx_2 + playerWidth_2 > pipe_2['x'] \
                and playerx_2 < pipe_2['x'] + pipeWidth_2:
            if not crashTest_2:
                playery_2 = old_playery_2 + min(playerVelY_2, pipe_2['y'] - old_playery_2 - playerHeight_2)

        # if the pipe starts getting out of the screen need to check it is not too far
        if pipe['x'] + pipeWidth > 0 and pipe['x'] <= 0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            playery = old_playery + min(playerVelY, GROUNDY - old_playery - playerHeight)

            # Added roof boundary
            if old_playery < ROOFY + GAME_SPRITES['roof'].get_height():
                playery = max(old_playery + playerVelY, ROOFY + GAME_SPRITES['roof'].get_height() + playerVelY)

        # if the pipe starts getting out of the screen need to check it is not too far
        if pipe_2['x'] + pipeWidth_2 > 0 and pipe_2['x'] <= 0 and playerx_2 - (pipe_2['x'] + pipeWidth_2) < pipeWidth_2:
            playery_2 = old_playery_2 + min(playerVelY_2, GROUNDY_2 - old_playery_2 - playerHeight_2)

            # Added roof boundary
            if old_playery_2 < ROOFY_2 + GAME_SPRITES['roof_2'].get_height():
                playery_2 = max(old_playery_2 + playerVelY_2,
                                ROOFY_2 + GAME_SPRITES['roof_2'].get_height() + playerVelY_2)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        for upperPipe_2, lowerPipe_2 in zip(upperPipes_2, lowerPipes_2):
            upperPipe_2['x'] += pipeVelX_2
            lowerPipe_2['x'] += pipeVelX_2

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes_2[0]['x'] < 5:
            newpipe_2 = getRandomPipe_2()
            upperPipes_2.append(newpipe_2[0])
            lowerPipes_2.append(newpipe_2[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # if the pipe is out of the screen, remove it
        if upperPipes_2[0]['x'] < -GAME_SPRITES['pipe_2'][0].get_width():
            upperPipes_2.pop(0)
            lowerPipes_2.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES[upperPipe['type']][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES[lowerPipe['type']][1], (lowerPipe['x'], lowerPipe['y']))

        for upperPipe_2, lowerPipe_2 in zip(upperPipes_2, lowerPipes_2):
            # Taking pipe small or big based on the type of the upper
            SCREEN.blit(GAME_SPRITES[upperPipe_2['type']][0], (upperPipe_2['x'], upperPipe_2['y']))
            SCREEN.blit(GAME_SPRITES[lowerPipe_2['type']][1], (lowerPipe_2['x'], lowerPipe_2['y']))

        # Adding floor and roof
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY + 18))
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['roof'], (basex, ROOFY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        SCREEN.blit(GAME_SPRITES['base_2'], (basex_2, GROUNDY_2))
        SCREEN.blit(GAME_SPRITES['roof_2'], (basex_2, ROOFY_2))
        SCREEN.blit(GAME_SPRITES['player_2'], (playerx_2, playery_2))

        myDigits = [int(x) for x in list(str(score))]
        width = 0

        myDigits_2 = [int(x) for x in list(str(score_2))]
        width_2 = 0

        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2

        for digit_2 in myDigits_2:
            width_2 += GAME_SPRITES['numbers_2'][digit_2].get_width()
        Xoffset_2 = (SCREENWIDTH - width_2) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        for digit_2 in myDigits_2:
            SCREEN.blit(GAME_SPRITES['numbers_2'][digit_2], (Xoffset_2, SCREENHEIGHT * 0.12 + SCREENHEIGHT))
            Xoffset_2 += GAME_SPRITES['numbers_2'][digit_2].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    # Removed hit noise when hitting the roof
    # if playery> GROUNDY - 25  or playery < 0:
    #    GAME_SOUNDS['hit'].play()
    #    return True

    # TODO change isCollide to only vertical touches, not also horizontally
    # If we touch on top or on bottom is not a problem

    collision = False

    # for pipe in upperPipes:
    #    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    #    if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
    #        #GAME_SOUNDS['hit'].play()
    #        collision = True

    # for pipe in lowerPipes:
    #    if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
    #        #GAME_SOUNDS['hit'].play()
    #        collision = True

    playerWidth = GAME_SPRITES['player'].get_width()

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES[pipe['type']][0].get_height()
        pipeWidth = GAME_SPRITES[pipe['type']][0].get_height()
        if playery < pipeHeight + pipe['y'] \
                and playerx + playerWidth > pipe['x'] \
                and playerx < pipe['x'] + pipeWidth \
                and playerx - pipe['x'] <= pipeWidth:
            collision = True

        if pipe['x'] + pipeWidth > 0 and pipe['x'] <= 0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            collision = False

    for pipe in lowerPipes:
        pipeHeight = GAME_SPRITES[pipe['type']][0].get_height()
        pipeWidth = GAME_SPRITES[pipe['type']][0].get_height()
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] \
                and playerx + playerWidth > pipe['x'] \
                and playerx < pipe['x'] + pipeWidth \
                and playerx - pipe['x'] <= pipeWidth:
            collision = True

        if pipe['x'] + pipeWidth > 0 and pipe['x'] <= 0 and playerx - (pipe['x'] + pipeWidth) < pipeWidth:
            collision = False

    return collision


def isCollide_2(playerx_2, playery_2, upperPipes_2, lowerPipes_2):
    collision = False

    playerWidth_2 = GAME_SPRITES['player_2'].get_width()

    for pipe_2 in upperPipes_2:
        pipeHeight_2 = GAME_SPRITES[pipe_2['type']][0].get_height()
        pipeWidth_2 = GAME_SPRITES[pipe_2['type']][0].get_height()
        if playery_2 < pipeHeight_2 + pipe_2['y'] \
                and playerx_2 + playerWidth_2 > pipe_2['x'] \
                and playerx_2 < pipe_2['x'] + pipeWidth_2 \
                and playerx_2 - pipe_2['x'] <= pipeWidth_2:
            collision = True

        if pipe_2['x'] + pipeWidth_2 > 0 and pipe_2['x'] <= 0 and playerx_2 - (pipe_2['x'] + pipeWidth_2) < pipeWidth_2:
            collision = False

    for pipe_2 in lowerPipes_2:
        pipeHeight_2 = GAME_SPRITES[pipe_2['type']][0].get_height()
        pipeWidth_2 = GAME_SPRITES[pipe_2['type']][0].get_height()
        if playery_2 + GAME_SPRITES['player_2'].get_height() > pipe_2['y'] \
                and playerx_2 + playerWidth_2 > pipe_2['x'] \
                and playerx_2 < pipe_2['x'] + pipeWidth_2 \
                and playerx_2 - pipe_2['x'] <= pipeWidth_2:
            collision = True

        if pipe_2['x'] + pipeWidth_2 > 0 and pipe_2['x'] <= 0 and playerx_2 - (pipe_2['x'] + pipeWidth_2) < pipeWidth_2:
            collision = False

    return collision


def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    type_upper = 'pipe'
    type_lower = 'pipe'

    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 5
    y1 = pipeHeight - y2 + offset

    # Logic for lower
    if y2 + pipeHeight < SCREENHEIGHT - GAME_SPRITES['base'].get_height():
        type_lower = 'pipe_big'
        if y2 + GAME_SPRITES['pipe_big'][1].get_height() < SCREENHEIGHT - GAME_SPRITES['base'].get_height():
            y2 = SCREENHEIGHT - GAME_SPRITES['pipe_big'][1].get_height()

    if y2 + pipeHeight > SCREENHEIGHT:
        type_lower = 'pipe_small'
        if y2 + GAME_SPRITES['pipe_small'][1].get_height() > SCREENHEIGHT:
            y2 = SCREENHEIGHT - GAME_SPRITES['base'].get_height() - GAME_SPRITES['pipe_small'][1].get_height()

    # logic for upper
    if y1 < -GAME_SPRITES['roof'].get_height():
        type_upper = 'pipe_big'
        y1 = -GAME_SPRITES['roof'].get_height()

    pipe = [
        {'x': pipeX, 'y': -y1, 'type': type_upper},  # upper Pipe
        {'x': pipeX, 'y': y2, 'type': type_lower}  # lower Pipe
    ]
    return pipe


def getRandomPipe_2():
    # Logic is different for pipes of player 1 and 2

    # TODO I could change the type of image taken based on the position on the screen:
    # ex for lower pipes:  if it is high we get bigger pipes
    # if is low we take smaller pipes
    # viceversa for upper pipes
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """

    # TODO Try adding different types of pipe
    type_upper = 'pipe'
    type_lower = 'pipe'

    pipeHeight_2 = GAME_SPRITES['pipe_2'][0].get_height()
    offset_2 = SCREENHEIGHT / 3
    y2_2 = offset_2 + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base_2'].get_height() - 1.2 * offset_2))

    pipeX_2 = SCREENWIDTH + 5
    y1_2 = pipeHeight_2 - y2_2 + offset_2

    if y1_2 > GAME_SPRITES['roof_2'].get_height():
        # offset_2 = SCREENHEIGHT/5
        type_upper = 'pipe_small'
        y1_2 = 0

    if y1_2 < - GAME_SPRITES['roof_2'].get_height():
        type_upper = 'pipe_big'
        # offset_2 = SCREENHEIGHT/5
        y1_2 = GAME_SPRITES['roof_2'].get_height()

    if TOTAL_SCREENHEIGHT - (SCREENHEIGHT + y2_2) > pipeHeight_2:
        type_lower = 'pipe_big'
        if TOTAL_SCREENHEIGHT - (SCREENHEIGHT + y2_2) > GAME_SPRITES['pipe_big'][1].get_height():
            y2_2 += (TOTAL_SCREENHEIGHT - (SCREENHEIGHT + y2_2)) - GAME_SPRITES['pipe_big'][1].get_height()

    pipe_2 = [
        {'x': pipeX_2, 'y': SCREENHEIGHT - y1_2, 'type': type_upper},  # upper Pipe
        {'x': pipeX_2, 'y': SCREENHEIGHT + y2_2, 'type': type_lower}  # lower Pipe
    ]
    return pipe_2


if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init()  # Initialize all pygame's modules
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

    GAME_SPRITES['numbers_2'] = (
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

    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/kirby_welcome.png').convert_alpha()
    GAME_SPRITES['winning'] = pygame.image.load('gallery/sprites/winning.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/floor_try.png').convert_alpha()
    GAME_SPRITES['roof'] = pygame.image.load('gallery/sprites/roof_try.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()

                            )
    # TRYING ADDING ANOTHER PIPE
    GAME_SPRITES['pipe_small'] = (pygame.transform.rotate(pygame.image.load(PIPESMALL).convert_alpha(), 180),
                                  pygame.image.load(PIPESMALL).convert_alpha()

                                  )
    # TRYING ADDING ANOTHER PIPE
    GAME_SPRITES['pipe_big'] = (pygame.transform.rotate(pygame.image.load(PIPESMALL).convert_alpha(), 180),
                                pygame.image.load(PIPEBIG).convert_alpha()

                                )

    GAME_SPRITES['base_2'] = pygame.image.load('gallery/sprites/floor_try.png').convert_alpha()
    GAME_SPRITES['roof_2'] = pygame.image.load('gallery/sprites/roof_try.png').convert_alpha()
    GAME_SPRITES['pipe_2'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
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
    GAME_SPRITES['player_2'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # Shows welcome screen to the user until he presses a button
        result = mainGame()  # This is the main game function
        if result is not None:
            winningScreen(result)
