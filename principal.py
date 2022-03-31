# importing libraries
import numpy as np#to clip and make a constrain whit the xyz cordinates and manage arrays
import sys#to change the apend to select correctly betwen folders
import pygame
import time
import random
import glob# to import multiple pythons files
import os# to load pwd of where is this archive in the directory

from locales import *
from visitantes import *

velocidad = 8#ciclos por segundo
# Window size aqui cada 10 pixels representa 25cm
window_x = 1350
window_y = 880
limite_x = 1240#metros 155x55x40 xyz
limite_y = 440#1240x440 xy
z0       = 880#0 para crear el plano xz 770
limite_z = z0-440#z

hx1 = 30#hitbox x min
hx2 = 15#hitbox x max
hy1 = 35#hitbox y min
hy2 = 25#hitbox y max
hz1 = 35#hitbox z min
hz2 = 25#hitbox z max
hx = False
hy = False
hz = False

for x in range(0,1):# defining colors
    black = pygame.Color(0, 0, 0)
    black2 = pygame.Color(20, 20, 20)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    green2 = pygame.Color(0, 150, 0)
    blue = pygame.Color(40, 40, 255)
    cian = pygame.Color(0,255,255)
    brown = pygame.Color(115,0,0)
    yellow = pygame.Color(255,255,0)
    grey = pygame.Color(127,127,127)
    orange = pygame.Color(255,100,10)
    purple = pygame.Color(240,0,255)
    pink = pygame.Color(255,100,180)
    white = pygame.Color(255,255,255)
    orb_color = green

# Initialising pygame
pygame.init()

# Initialise game window xy
pygame.display.set_caption('cyber_ball_simulator v1')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

bandera_texto_orb = False
#banderas
agarre_orb = 0#corroborar si el orb esta siendo sostenido o no y en ese caso caera por gravedad

# initial score
score1 = 0#equipo 1 locales
score2 = 0#equipo 2 visitantes
# formacion inicial chaser 3, seeker 1, beater 2, keeper 1
for x in range(0,1):#jugadores posiciones
    #equipo 1 
    chaser1_equipo1_pos = [380, 180, 220]
    chaser2_equipo1_pos = [380, 220, 220]
    chaser3_equipo1_pos = [380, 260, 220]
    seeker_equipo1_pos  = [460, 220, 220]
    beater1_equipo1_pos = [420, 200, 220]
    beater2_equipo1_pos = [420, 240, 220]
    keeper_equipo1_pos  = [340, 220, 220]

    #equipo2
    chaser1_equipo2_pos = [860, 180, 220]
    chaser2_equipo2_pos = [860, 220, 220]
    chaser3_equipo2_pos = [860, 260, 220]
    seeker_equipo2_pos  = [780, 220, 220]
    beater1_equipo2_pos = [820, 200, 220]
    beater2_equipo2_pos = [820, 240, 220]
    keeper_equipo2_pos  = [900, 220, 220]
for x in range(0,1):#objetos del juego
    orb_pos =             [620, 220, 220]#xyz
    sniper_pos =          [620, 240, 220]#600 220 100
    bulldozer1_pos =      [620, 260, 220]
    bulldozer2_pos =      [620, 200, 220]

    aro1_equipo1 =           [60, 160, 220]
    aro2_equipo1 =           [60, 220, 220]
    aro3_equipo1 =           [60, 280, 220]
    aro1_equipo2 =         [1175, 160, 220]
    aro2_equipo2 =         [1175, 220, 220]
    aro3_equipo2 =         [1175, 280, 220]

    portador_orb_pos = {}
    portador_sniper_pos = {}
    portador_bulldozer1_pos = {}
    portador_bulldozer2_pos = {}
    #portador_orb_pos = [380, 180, 100]
    portador_orb_pos[3] = "0"


    sniper_velocidad =        45#100km/h = 27m/s
    bulldozer1_velocidad =      27
    bulldozer2_velocidad =      27
    gravedad_aceleracion = 9.8#gravedad normal en la tierra 9.8m/s
    x =0
    y = 0
    gravity =[-x,-y]
score = 0# initial score

def show_score(choice, color, font, size):
    my_font2 = pygame.font.SysFont('times new roman', 15)#para los jugadores
    # creating font object score_font
    #score_font = pygame.font.SysFont(font, size)
    score_font = pygame.font.SysFont(font, 30)
    # create the display surface object
    # score_surface
    score_surface = score_font.render('locales : ' + str(score1)+'  ' 'visitantes : ' + str(score2), True, color,)
    #score_surface = score_font.render('locales : ' + str(sniper_pos[0])+'  ' 'visitantes : ' + str(sniper_pos[1]), True, color,)
    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)
    # create the display surface object
    for i in range (0,1):
        for c in range (0,1):#equipo 1 locales
            chaser1_equipo1_surface = my_font2.render(chaser1_equipo1[0], True, pink)
            chaser2_equipo1_surface = my_font2.render(chaser2_equipo1[0], True, pink)
        chaser3_equipo1_surface = my_font2.render(chaser3_equipo1[0], True, pink)

        beater1_equipo1_surface = my_font2.render(beater1_equipo1[0], True, pink)
        beater2_equipo1_surface = my_font2.render(beater2_equipo1[0], True, pink)

        keeper_equipo1_surface = my_font2.render(keeper_equipo1[0], True, pink)
        seeker_equipo1_surface = my_font2.render(seeker_equipo1[0], True, pink)
    for c in range (0,1):#equipo 2 visitantes
        chaser1_equipo2_surface = my_font2.render(chaser1_equipo2[0], True, cian)
        chaser2_equipo2_surface = my_font2.render(chaser2_equipo2[0], True, cian)
        chaser3_equipo2_surface = my_font2.render(chaser3_equipo2[0], True, cian)

        beater1_equipo2_surface = my_font2.render(beater1_equipo2[0], True, cian)
        beater2_equipo2_surface = my_font2.render(beater2_equipo2[0], True, cian)

        keeper_equipo2_surface = my_font2.render(keeper_equipo2[0], True, cian)
        seeker_equipo2_surface = my_font2.render(seeker_equipo2[0], True, cian)

    bulldozer1_surface = my_font2.render("B1", True, yellow)
    # create a rectangular object for the
    # text surface object
    for i in range (0,1):
        for c in range (0,1):#equipo 1
            chaser1_equipo1_rect = chaser1_equipo1_surface.get_rect()
            chaser2_equipo1_rect = chaser2_equipo1_surface.get_rect()
            chaser3_equipo1_rect = chaser3_equipo1_surface.get_rect()

            beater1_equipo1_rect = beater1_equipo1_surface.get_rect()
            beater2_equipo1_rect = beater2_equipo1_surface.get_rect()

            keeper_equipo1_rect = keeper_equipo1_surface.get_rect()
            seeker_equipo1_rect = seeker_equipo1_surface.get_rect()
                                                        ########PRESPECTIVA XZ
            chaser1_equipo1_rectXZ = chaser1_equipo1_surface.get_rect()
            chaser2_equipo1_rectXZ = chaser2_equipo1_surface.get_rect()
            chaser3_equipo1_rectXZ = chaser3_equipo1_surface.get_rect()

            beater1_equipo1_rectXZ = beater1_equipo1_surface.get_rect()
            beater2_equipo1_rectXZ = beater2_equipo1_surface.get_rect()

            keeper_equipo1_rectXZ = keeper_equipo1_surface.get_rect()
            seeker_equipo1_rectXZ = seeker_equipo1_surface.get_rect()
        for c in range (0,1):#equipo 2
            chaser1_equipo2_rect = chaser1_equipo2_surface.get_rect()
            chaser2_equipo2_rect = chaser2_equipo2_surface.get_rect()
            chaser3_equipo2_rect = chaser3_equipo2_surface.get_rect()

            beater1_equipo2_rect = beater1_equipo2_surface.get_rect()
            beater2_equipo2_rect = beater2_equipo2_surface.get_rect()

            keeper_equipo2_rect = keeper_equipo2_surface.get_rect()
            seeker_equipo2_rect = seeker_equipo2_surface.get_rect()
                                                        ########PRESPECTIVA XZ
            chaser1_equipo2_rectXZ = chaser1_equipo2_surface.get_rect()
            chaser2_equipo2_rectXZ = chaser2_equipo2_surface.get_rect()
            chaser3_equipo2_rectXZ = chaser3_equipo2_surface.get_rect()

            beater1_equipo2_rectXZ = beater1_equipo2_surface.get_rect()
            beater2_equipo2_rectXZ = beater2_equipo2_surface.get_rect()

            keeper_equipo2_rectXZ = keeper_equipo2_surface.get_rect()
            seeker_equipo2_rectXZ = seeker_equipo2_surface.get_rect()
    bulldozer1_rect = bulldozer1_surface.get_rect()
    # setting position of the text
    for i in range (0,1):
        for c in range (0,1):#equipo 1
            chaser1_equipo1_rect.midtop = (chaser1_equipo1_pos[0]+5, chaser1_equipo1_pos[1]-17)
            chaser2_equipo1_rect.midtop = (chaser2_equipo1_pos[0]+5, chaser2_equipo1_pos[1]-17)
            chaser3_equipo1_rect.midtop = (chaser3_equipo1_pos[0]+5, chaser3_equipo1_pos[1]-17)

            beater1_equipo1_rect.midtop = (beater1_equipo1_pos[0]+5, beater1_equipo1_pos[1]-17)
            beater2_equipo1_rect.midtop = (beater2_equipo1_pos[0]+5, beater2_equipo1_pos[1]-17)

            keeper_equipo1_rect.midtop = (keeper_equipo1_pos[0]+5, keeper_equipo1_pos[1]-17)
            seeker_equipo1_rect.midtop = (seeker_equipo1_pos[0]+5, seeker_equipo1_pos[1]-17)
            ########PRESPECTIVA XZ
            chaser1_equipo1_rectXZ.midtop = (chaser1_equipo1_pos[0]+5,z0-chaser1_equipo1_pos[2]-17)
            chaser2_equipo1_rectXZ.midtop = (chaser2_equipo1_pos[0]+5,z0-chaser2_equipo1_pos[2]-17)
            chaser3_equipo1_rectXZ.midtop = (chaser3_equipo1_pos[0]+5,z0-chaser3_equipo1_pos[2]-17)

            beater1_equipo1_rectXZ.midtop = (beater1_equipo1_pos[0]+5,z0-beater1_equipo1_pos[2]-17)
            beater2_equipo1_rectXZ.midtop = (beater2_equipo1_pos[0]+5,z0-beater2_equipo1_pos[2]-17)

            keeper_equipo1_rectXZ.midtop = (keeper_equipo1_pos[0]+5,z0-keeper_equipo1_pos[2]-17)
            seeker_equipo1_rectXZ.midtop = (seeker_equipo1_pos[0]+5,z0-seeker_equipo1_pos[2]-17)
        for c in range (0,1):#equipo 2
            chaser1_equipo2_rect.midtop = (chaser1_equipo2_pos[0]+5, chaser1_equipo2_pos[1]-17)
            chaser2_equipo2_rect.midtop = (chaser2_equipo2_pos[0]+5, chaser2_equipo2_pos[1]-17)
            chaser3_equipo2_rect.midtop = (chaser3_equipo2_pos[0]+5, chaser3_equipo2_pos[1]-17)

            beater1_equipo2_rect.midtop = (beater1_equipo2_pos[0]+5, beater1_equipo2_pos[1]-17)
            beater2_equipo2_rect.midtop = (beater2_equipo2_pos[0]+5, beater2_equipo2_pos[1]-17)

            keeper_equipo2_rect.midtop = (keeper_equipo2_pos[0]+5, keeper_equipo2_pos[1]-17)
            seeker_equipo2_rect.midtop = (seeker_equipo2_pos[0]+5, seeker_equipo2_pos[1]-17)
            ########PRESPECTIVA XZ
            chaser1_equipo2_rectXZ.midtop = (chaser1_equipo2_pos[0]+5,z0-chaser1_equipo2_pos[2]-17)
            chaser2_equipo2_rectXZ.midtop = (chaser2_equipo2_pos[0]+5,z0-chaser2_equipo2_pos[2]-17)
            chaser3_equipo2_rectXZ.midtop = (chaser3_equipo2_pos[0]+5,z0-chaser3_equipo2_pos[2]-17)

            beater1_equipo2_rectXZ.midtop = (beater1_equipo2_pos[0]+5,z0-beater1_equipo2_pos[2]-17)
            beater2_equipo2_rectXZ.midtop = (beater2_equipo2_pos[0]+5,z0-beater2_equipo2_pos[2]-17)

            keeper_equipo2_rectXZ.midtop = (keeper_equipo2_pos[0]+5,z0-keeper_equipo2_pos[2]-17)
            seeker_equipo2_rectXZ.midtop = (seeker_equipo2_pos[0]+5,z0-seeker_equipo2_pos[2]-17)

     #   pygame.draw.rect(game_window, orange, pygame.Rect(                      #jugador perspectiva xz
    bulldozer1_rect.midtop = (bulldozer1_pos[0]+2, bulldozer1_pos[1]-17)
    # displaying text
    for i in range (0,1):
        for c in range (0,1):#equipo 1
            game_window.blit(chaser1_equipo1_surface, chaser1_equipo1_rect)
            game_window.blit(chaser2_equipo1_surface, chaser2_equipo1_rect)
            game_window.blit(chaser3_equipo1_surface, chaser3_equipo1_rect)

            game_window.blit(beater1_equipo1_surface, beater1_equipo1_rect)
            game_window.blit(beater2_equipo1_surface, beater2_equipo1_rect)

            game_window.blit(keeper_equipo1_surface, keeper_equipo1_rect)
            game_window.blit(seeker_equipo1_surface, seeker_equipo1_rect)
                                                                    ########PRESPECTIVA XZ
            game_window.blit(chaser1_equipo1_surface, chaser1_equipo1_rectXZ)
            game_window.blit(chaser2_equipo1_surface, chaser2_equipo1_rectXZ)
            game_window.blit(chaser3_equipo1_surface, chaser3_equipo1_rectXZ)

            game_window.blit(beater1_equipo1_surface, beater1_equipo1_rectXZ)
            game_window.blit(beater2_equipo1_surface, beater2_equipo1_rectXZ)

            game_window.blit(keeper_equipo1_surface, keeper_equipo1_rectXZ)
            game_window.blit(seeker_equipo1_surface, seeker_equipo1_rectXZ)
        for c in range (0,1):#equipo 2
            game_window.blit(chaser1_equipo2_surface, chaser1_equipo2_rect)
            game_window.blit(chaser2_equipo2_surface, chaser2_equipo2_rect)
            game_window.blit(chaser3_equipo2_surface, chaser3_equipo2_rect)

            game_window.blit(beater1_equipo2_surface, beater1_equipo2_rect)
            game_window.blit(beater2_equipo2_surface, beater2_equipo2_rect)

            game_window.blit(keeper_equipo2_surface, keeper_equipo2_rect)
            game_window.blit(seeker_equipo2_surface, seeker_equipo2_rect)
                                                                    ########PRESPECTIVA XZ
            game_window.blit(chaser1_equipo2_surface, chaser1_equipo2_rectXZ)
            game_window.blit(chaser2_equipo2_surface, chaser2_equipo2_rectXZ)
            game_window.blit(chaser3_equipo2_surface, chaser3_equipo2_rectXZ)

            game_window.blit(beater1_equipo2_surface, beater1_equipo2_rectXZ)
            game_window.blit(beater2_equipo2_surface, beater2_equipo2_rectXZ)

            game_window.blit(keeper_equipo2_surface, keeper_equipo2_rectXZ)
            game_window.blit(seeker_equipo2_surface, seeker_equipo2_rectXZ)
    game_window.blit(bulldozer1_surface, bulldozer1_rect)# displaying Score function

#def guardar_IA(identificador):
#	print("guardando IA 19")
def game_over():# game over function
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)#game over


    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)


    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()


    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)


    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    for i in range (0,1):
        if jugadores1[19]==True:guardar_IA(19)
        if jugadores1[19]==True:guardar_IA19()
        if jugadores1[20]==True:guardar_IA20()
        if jugadores1[21]==True:guardar_IA21()
        if jugadores1[22]==True:guardar_IA22()
        if jugadores1[23]==True:guardar_IA23()
        if jugadores1[24]==True:guardar_IA24()
        if jugadores1[25]==True:guardar_IA25()
        if jugadores1[26]==True:guardar_IA26()
        if jugadores1[27]==True:guardar_IA27()
        if jugadores1[28]==True:guardar_IA28()
        if jugadores1[29]==True:guardar_IA29()
        if jugadores1[30]==True:guardar_IA30()
        if jugadores1[31]==True:guardar_IA31()
        if jugadores1[32]==True:guardar_IA32()
        if jugadores1[33]==True:guardar_IA33()
        if jugadores1[34]==True:guardar_IA34()
        if jugadores1[35]==True:guardar_IA35()
        if jugadores1[36]==True:guardar_IA36()
        if jugadores1[37]==True:guardar_IA37()
        if jugadores1[38]==True:guardar_IA38()
        if jugadores1[39]==True:guardar_IA39()
        if jugadores1[40]==True:guardar_IA40()
        if jugadores1[41]==True:guardar_IA41()
        if jugadores1[42]==True:guardar_IA42()
        if jugadores1[43]==True:guardar_IA43()
        if jugadores1[44]==True:guardar_IA44()
        if jugadores1[45]==True:guardar_IA45()
        if jugadores1[46]==True:guardar_IA46()
        if jugadores1[47]==True:guardar_IA47()
        if jugadores1[48]==True:guardar_IA48()
        if jugadores1[49]==True:guardar_IA49()
        if jugadores1[50]==True:guardar_IA50()
        if jugadores1[51]==True:guardar_IA51()
        if jugadores1[52]==True:guardar_IA52()
        if jugadores1[53]==True:guardar_IA53()
        if jugadores1[54]==True:guardar_IA54()
        if jugadores1[55]==True:guardar_IA55()
        if jugadores1[56]==True:guardar_IA56()
        if jugadores1[57]==True:guardar_IA57()
        if jugadores1[58]==True:guardar_IA58()
        if jugadores1[59]==True:guardar_IA59()
        if jugadores1[60]==True:guardar_IA60()
        if jugadores1[61]==True:guardar_IA61()
        if jugadores1[62]==True:guardar_IA62()
        if jugadores1[63]==True:guardar_IA63()
        if jugadores1[64]==True:guardar_IA64()
        if jugadores1[65]==True:guardar_IA65()
        if jugadores1[66]==True:guardar_IA66()
        if jugadores1[67]==True:guardar_IA67()
        if jugadores1[68]==True:guardar_IA68()
        if jugadores1[69]==True:guardar_IA69()
        if jugadores1[70]==True:guardar_IA70()
        if jugadores1[71]==True:guardar_IA71()
        if jugadores1[72]==True:guardar_IA72()
        if jugadores1[73]==True:guardar_IA73()
        if jugadores1[74]==True:guardar_IA74()
        if jugadores1[75]==True:guardar_IA75()
        if jugadores1[76]==True:guardar_IA76()
        if jugadores1[77]==True:guardar_IA77()
        if jugadores1[78]==True:guardar_IA78()
        if jugadores1[79]==True:guardar_IA79()
        if jugadores1[80]==True:guardar_IA80()
        if jugadores1[81]==True:guardar_IA81()
        if jugadores1[82]==True:guardar_IA82()
        if jugadores1[83]==True:guardar_IA83()
        if jugadores1[84]==True:guardar_IA84()
        if jugadores1[85]==True:guardar_IA85()
        if jugadores1[86]==True:guardar_IA86()
        if jugadores1[87]==True:guardar_IA87()
        if jugadores1[88]==True:guardar_IA88()
        if jugadores1[89]==True:guardar_IA89()
        if jugadores1[90]==True:guardar_IA90()
        if jugadores1[91]==True:guardar_IA91()
        if jugadores1[92]==True:guardar_IA92()
        if jugadores1[93]==True:guardar_IA93()
        if jugadores1[94]==True:guardar_IA94()
        if jugadores1[95]==True:guardar_IA95()
        if jugadores1[96]==True:guardar_IA96()
        if jugadores1[97]==True:guardar_IA97()
        if jugadores1[98]==True:guardar_IA98()
        if jugadores1[99]==True:guardar_IA99()

        if jugadores2[19]==True:guardar_IA19()
        if jugadores2[20]==True:guardar_IA20()
        if jugadores2[21]==True:guardar_IA21()
        if jugadores2[22]==True:guardar_IA22()
        if jugadores2[23]==True:guardar_IA23()
        if jugadores2[24]==True:guardar_IA24()
        if jugadores2[25]==True:guardar_IA25()
        if jugadores2[26]==True:guardar_IA26()
        if jugadores2[27]==True:guardar_IA27()
        if jugadores2[28]==True:guardar_IA28()
        if jugadores2[29]==True:guardar_IA29()
        if jugadores2[30]==True:guardar_IA30()
        if jugadores2[31]==True:guardar_IA31()
        if jugadores2[32]==True:guardar_IA32()
        if jugadores2[33]==True:guardar_IA33()
        if jugadores2[34]==True:guardar_IA34()
        if jugadores2[35]==True:guardar_IA35()
        if jugadores2[36]==True:guardar_IA36()
        if jugadores2[37]==True:guardar_IA37()
        if jugadores2[38]==True:guardar_IA38()
        if jugadores2[39]==True:guardar_IA39()
        if jugadores2[40]==True:guardar_IA40()
        if jugadores2[41]==True:guardar_IA41()
        if jugadores2[42]==True:guardar_IA42()
        if jugadores2[43]==True:guardar_IA43()
        if jugadores2[44]==True:guardar_IA44()
        if jugadores2[45]==True:guardar_IA45()
        if jugadores2[46]==True:guardar_IA46()
        if jugadores2[47]==True:guardar_IA47()
        if jugadores2[48]==True:guardar_IA48()
        if jugadores2[49]==True:guardar_IA49()
        if jugadores2[50]==True:guardar_IA50()
        if jugadores2[51]==True:guardar_IA51()
        if jugadores2[52]==True:guardar_IA52()
        if jugadores2[53]==True:guardar_IA53()
        if jugadores2[54]==True:guardar_IA54()
        if jugadores2[55]==True:guardar_IA55()
        if jugadores2[56]==True:guardar_IA56()
        if jugadores2[57]==True:guardar_IA57()
        if jugadores2[58]==True:guardar_IA58()
        if jugadores2[59]==True:guardar_IA59()
        if jugadores2[60]==True:guardar_IA60()
        if jugadores2[61]==True:guardar_IA61()
        if jugadores2[62]==True:guardar_IA62()
        if jugadores2[63]==True:guardar_IA63()
        if jugadores2[64]==True:guardar_IA64()
        if jugadores2[65]==True:guardar_IA65()
        if jugadores2[66]==True:guardar_IA66()
        if jugadores2[67]==True:guardar_IA67()
        if jugadores2[68]==True:guardar_IA68()
        if jugadores2[69]==True:guardar_IA69()
        if jugadores2[70]==True:guardar_IA70()
        if jugadores2[71]==True:guardar_IA71()
        if jugadores2[72]==True:guardar_IA72()
        if jugadores2[73]==True:guardar_IA73()
        if jugadores2[74]==True:guardar_IA74()
        if jugadores2[75]==True:guardar_IA75()
        if jugadores2[76]==True:guardar_IA76()
        if jugadores2[77]==True:guardar_IA77()
        if jugadores2[78]==True:guardar_IA78()
        if jugadores2[79]==True:guardar_IA79()
        if jugadores2[80]==True:guardar_IA80()
        if jugadores2[81]==True:guardar_IA81()
        if jugadores2[82]==True:guardar_IA82()
        if jugadores2[83]==True:guardar_IA83()
        if jugadores2[84]==True:guardar_IA84()
        if jugadores2[85]==True:guardar_IA85()
        if jugadores2[86]==True:guardar_IA86()
        if jugadores2[87]==True:guardar_IA87()
        if jugadores2[88]==True:guardar_IA88()
        if jugadores2[89]==True:guardar_IA89()
        if jugadores2[90]==True:guardar_IA90()
        if jugadores2[91]==True:guardar_IA91()
        if jugadores2[92]==True:guardar_IA92()
        if jugadores2[93]==True:guardar_IA93()
        if jugadores2[94]==True:guardar_IA94()
        if jugadores2[95]==True:guardar_IA95()
        if jugadores2[96]==True:guardar_IA96()
        if jugadores2[97]==True:guardar_IA97()
        if jugadores2[98]==True:guardar_IA98()
        if jugadores2[99]==True:guardar_IA99()#guardar la IA

    # after 2 seconds we will quit the
    # program
    #for i in range(19,100):
    #    print("if jugadores[",i,"]==True: guardar_IA",i,"()")


    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()
def cargar_jugadores():
    print ("locales",chaser1_equipo1[10])
    for i in range (0,1):
            print(chaser1_equipo1[0],chaser1_equipo1[1],chaser1_equipo1[3],chaser1_equipo1[2])
            #print(chaser1_equipo1_IA)
            print(chaser2_equipo1[0],chaser2_equipo1[1],chaser2_equipo1[3],chaser2_equipo1[2])
            print(chaser3_equipo1[0],chaser3_equipo1[1],chaser3_equipo1[3],chaser3_equipo1[2])

            print(beater1_equipo1[0],beater1_equipo1[1],beater1_equipo1[3],beater1_equipo1[2])
            print(beater2_equipo1[0],beater2_equipo1[1],beater2_equipo1[3],beater2_equipo1[2])

            print(keeper_equipo1[0],keeper_equipo1[1],keeper_equipo1[3],keeper_equipo1[2])
            print(seeker_equipo1[0],seeker_equipo1[1],seeker_equipo1[3],seeker_equipo1[2])
    print ("visitantes",chaser1_equipo2[10])
    for i in range (0,1):
            print(chaser1_equipo2[0],chaser1_equipo2[1],chaser1_equipo2[3],chaser1_equipo2[2])
            print(chaser2_equipo2[0],chaser2_equipo2[1],chaser2_equipo2[3],chaser2_equipo2[2])
            print(chaser3_equipo2[0],chaser3_equipo2[1],chaser3_equipo2[3],chaser3_equipo2[2])

            print(beater1_equipo2[0],beater1_equipo2[1],beater1_equipo2[3],beater1_equipo2[2])
            print(beater2_equipo2[0],beater2_equipo2[1],beater2_equipo2[3],beater2_equipo2[2])

            print(keeper_equipo2[0],keeper_equipo2[1],keeper_equipo2[3],keeper_equipo2[2])
            print(seeker_equipo2[0],seeker_equipo2[1],seeker_equipo2[3],seeker_equipo2[2])
def chaser1_equipo1_mecanicas():
    global portador_orb_pos,bandera_texto_orb,agarre_orb
    global hx1,hx2,hy1,hy2,hz1,hz2

    if agarre_orb == 1:
        if portador_orb_pos[3] == "11":#chaser 1 equipo 1
            atrapar_pelota("orb",chaser1_equipo1_pos[0],chaser1_equipo1_pos[1],chaser1_equipo1_pos[2])
    if chaser1_equipo1_pos[0]+hx1 >= orb_pos[0] and chaser1_equipo1_pos[0]-hx2 <= orb_pos[0]:
        hx = True
    else: hx = False
    if chaser1_equipo1_pos[1]+hy1 >= orb_pos[1] and chaser1_equipo1_pos[1]-hy2 <= orb_pos[1]:
        hy = True
    else: hy = False
    if chaser1_equipo1_pos[2]+hz1 >= orb_pos[2] and chaser1_equipo1_pos[2]-hz2 <= orb_pos[2]:
        hz = True
    else: hz = False
    if hx == True and hy == True and hz == True:
        if portador_orb_pos[3] != "11":
            bandera_texto_orb = False
            if bandera_texto_orb == False:
                print("chaser locales",chaser1_equipo1[0],chaser1_equipo1[2],"tiene el orbe")
                portador_orb_pos[3] = "11"
                atrapar_pelota("orb",chaser1_equipo1_pos[0],chaser1_equipo1_pos[1],chaser1_equipo1_pos[2])

    chaser1_equipo1_pos[0] = np.clip(chaser1_equipo1_pos[0], 10, 1235)#restringe x
    chaser1_equipo1_pos[1] = np.clip(chaser1_equipo1_pos[1], 10, 430)#restringe y
    chaser1_equipo1_pos[2] = np.clip(chaser1_equipo1_pos[2], 0, 270)#restringe z
def chaser1_equipo2_mecanicas():
    global portador_orb_pos,bandera_texto_orb,agarre_orbs
    global hx1,hx2,hy1,hy2,hz1,hz2

    if agarre_orb == 1:
       if portador_orb_pos[3] == "12":#chaser 1 equipo 2
            atrapar_pelota("orb",chaser1_equipo2_pos[0],chaser1_equipo2_pos[1],chaser1_equipo2_pos[2])

    if chaser1_equipo2_pos[0]+hx1 >= orb_pos[0] and chaser1_equipo2_pos[0]-hx2 <= orb_pos[0]:
        if chaser1_equipo2_pos[1]+hy1 >= orb_pos[1] and chaser1_equipo2_pos[1]-hy2 <= orb_pos[1]:
            if chaser1_equipo2_pos[2]+hz1 >= orb_pos[2] and chaser1_equipo2_pos[2]-hz2 <= orb_pos[2]:
                if portador_orb_pos[3] != "12":
                    bandera_texto_orb = False
                if bandera_texto_orb == False:
                    print("chaser visitantes",chaser1_equipo2[0],chaser1_equipo2[2],"tiene el orbe")
                    portador_orb_pos[3] = "12"
                atrapar_pelota("orb",chaser1_equipo2_pos[0],chaser1_equipo2_pos[1],chaser1_equipo2_pos[2])

    chaser1_equipo2_pos[0] = np.clip(chaser1_equipo2_pos[0], 10, 1235)#restringe x
    chaser1_equipo2_pos[1] = np.clip(chaser1_equipo2_pos[1], 10, 430)#restringe y
    chaser1_equipo2_pos[2] = np.clip(chaser1_equipo2_pos[2], 0, 270)#restringe z
def atrapar_pelota(pelota,x,y,z):
    global portador_orb_pos,agarre_orb,bandera_texto_orb
    if pelota == "orb":
        agarre_orb = 1
        bandera_texto_orb = True
        portador_orb_pos[0] = x#+20
        portador_orb_pos[1] = y#-10
        portador_orb_pos[2] = z#+10
        orb()
def jugadores():
    chaser1_equipo1_mecanicas()
    chaser1_equipo2_mecanicas()
def orb():
    global orb_pos,bandera_texto_orb
    if agarre_orb == 1:
        orb_pos[0] = portador_orb_pos[0]+20
        orb_pos[1] = portador_orb_pos[1]-10
        orb_pos[2] = portador_orb_pos[2]+10
       # print ("orb",orb_pos[0],orb_pos[1])
    else:
        bandera_texto_orb = False
        #orb_pos[2] -= gravedad_aceleracion
        #orb_pos[2] = 100

   # if  orb_pos[2] < 0:
   #     orb_pos[2] = 0

    orb_pos[0] = np.clip(orb_pos[0], 10, 1235)#restringe x
    orb_pos[1] = np.clip(orb_pos[1], 10, 430)#restringe y
    orb_pos[2] = np.clip(orb_pos[2], 10, 430)#restringe z
def sniper():
    # direction_sniper = 4
    direction_sniper = random.randint(1,8)#direcion aleatoria

    if direction_sniper == 1:#up
        sniper_pos[1] -= sniper_velocidad
    if direction_sniper == 2:#down
        sniper_pos[1] += sniper_velocidad
    if direction_sniper == 3:#left
        sniper_pos[0] -= sniper_velocidad
    if direction_sniper == 4:#right
        sniper_pos[0] += sniper_velocidad
    if direction_sniper == 5:#up
        sniper_pos[1] -= sniper_velocidad
        sniper_pos[0] -= sniper_velocidad
    if direction_sniper == 6:#down
        sniper_pos[1] += sniper_velocidad
        sniper_pos[0] += sniper_velocidad
    if direction_sniper == 7:#left
        sniper_pos[0] -= sniper_velocidad
        sniper_pos[1] += sniper_velocidad
    if direction_sniper == 8:#right
        sniper_pos[0] += sniper_velocidad
        sniper_pos[1] -= sniper_velocidad
    sniper_pos[0] = np.clip(sniper_pos[0], 10, 1235)
    sniper_pos[1] = np.clip(sniper_pos[1], 10, 430)
    sniper_pos[2] = np.clip(sniper_pos[2], 0, 270)
def bulldozer1():
    direction_bulldozer1 = random.randint(1,8)

    if direction_bulldozer1 == 1:#up
        bulldozer1_pos[1] -= bulldozer1_velocidad
    if direction_bulldozer1 == 2:#down
        bulldozer1_pos[1] += bulldozer1_velocidad
    if direction_bulldozer1 == 3:#left
        bulldozer1_pos[0] -= bulldozer1_velocidad
    if direction_bulldozer1 == 4:#right
        bulldozer1_pos[0] += bulldozer1_velocidad
    if direction_bulldozer1 == 5:#up
        bulldozer1_pos[1] -= bulldozer1_velocidad
        bulldozer1_pos[0] -= bulldozer1_velocidad
    if direction_bulldozer1 == 6:#down
        bulldozer1_pos[1] += bulldozer1_velocidad
        bulldozer1_pos[0] += bulldozer1_velocidad
    if direction_bulldozer1 == 7:#left
        bulldozer1_pos[0] -= bulldozer1_velocidad
        bulldozer1_pos[1] += bulldozer1_velocidad
    if direction_bulldozer1 == 8:#right
        bulldozer1_pos[0] += bulldozer1_velocidad
        bulldozer1_pos[1] -= bulldozer1_velocidad

    bulldozer1_pos[0] = np.clip(bulldozer1_pos[0], 10, 1235)
    bulldozer1_pos[1] = np.clip(bulldozer1_pos[1], 10, 430)
    bulldozer1_pos[2] = np.clip(bulldozer1_pos[2], 0, 270)
def bulldozer2():
    direction_bulldozer2 = random.randint(1,8)

    if direction_bulldozer2 == 1:#up
        bulldozer2_pos[1] -= bulldozer2_velocidad
    if direction_bulldozer2 == 2:#down
        bulldozer2_pos[1] += bulldozer2_velocidad
    if direction_bulldozer2 == 3:#left
        bulldozer2_pos[0] -= bulldozer2_velocidad
    if direction_bulldozer2 == 4:#right
        bulldozer2_pos[0] += bulldozer2_velocidad
    if direction_bulldozer2 == 5:#up
        bulldozer2_pos[1] -= bulldozer2_velocidad
        bulldozer2_pos[0] -= bulldozer2_velocidad
    if direction_bulldozer2 == 6:#down
        bulldozer2_pos[1] += bulldozer2_velocidad
        bulldozer2_pos[0] += bulldozer2_velocidad
    if direction_bulldozer2 == 7:#left
        bulldozer2_pos[0] -= bulldozer2_velocidad
        bulldozer2_pos[1] += bulldozer2_velocidad
    if direction_bulldozer2 == 8:#right
        bulldozer2_pos[0] += bulldozer2_velocidad
        bulldozer2_pos[1] -= bulldozer2_velocidad

    bulldozer2_pos[0] = np.clip(bulldozer2_pos[0], 10, 1235)
    bulldozer2_pos[1] = np.clip(bulldozer2_pos[1], 10, 430)
    bulldozer2_pos[2] = np.clip(bulldozer2_pos[2], 0, 270)
def draw():#dibuja todo excepto los numeros   #dibuja casi todo en pantalla

    pygame.draw.ellipse(game_window, black2, pygame.Rect(0, 0, 1240, 440))
    for x in range(0,1):#campo de juego x z
        pygame.draw.rect(game_window, grey, pygame.Rect(#campo de juego
               0, limite_y, 1350, 1))
        pygame.draw.rect(game_window, grey, pygame.Rect(#campo de juego
               limite_x, 0, 1, 880))


    pygame.draw.ellipse(game_window, black2, pygame.Rect(0, 440, 1240, 440))
    for x in range(0,1):#campo de juego x y
        pygame.draw.rect(game_window, grey, pygame.Rect(#campo de juego
               0, limite_y, 1350, 1))
        pygame.draw.rect(game_window, grey, pygame.Rect(#campo de juego
               limite_x, 0, 1, 720))

    for x in range(0,1):#hitbox chaser1
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-hx2, chaser1_equipo1_pos[1]-25, 1, 60))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]+hx1, chaser1_equipo1_pos[1]-25, 1, 60))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-25, chaser1_equipo1_pos[1]-hy1, 60, 1))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-25, chaser1_equipo1_pos[1]+hy2, 60, 1))

        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-hx2,z0-chaser1_equipo1_pos[2]-hz1, 1, 60))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]+hx1,z0-chaser1_equipo1_pos[2]-hz2, 1, 60))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-25,z0-chaser1_equipo1_pos[2]-hy1, 60, 1))
        pygame.draw.rect(game_window, white, pygame.Rect(
            chaser1_equipo1_pos[0]-25,z0-chaser1_equipo1_pos[2]+hy2, 60, 1))

    #chaser1_equipo1_pos[0]-hx2
    for x in range(0,1):#aros
        circleRect = pygame.draw.circle(
            game_window, grey, (aro1_equipo1[0], aro1_equipo1[1]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro2_equipo1[0], aro2_equipo1[1]), 10)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro3_equipo1[0], aro3_equipo1[1]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro1_equipo2[0], aro1_equipo2[1]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro2_equipo2[0], aro2_equipo2[1]), 10)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro3_equipo2[0], aro3_equipo2[1]), 5)

        circleRect = pygame.draw.circle(
            game_window, grey, (aro1_equipo1[0],z0-aro1_equipo1[2]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro2_equipo1[0],z0-aro2_equipo1[2]), 10)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro3_equipo1[0],z0-aro3_equipo1[2]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro1_equipo2[0],z0-aro1_equipo2[2]), 5)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro2_equipo2[0],z0-aro2_equipo2[2]), 10)
        circleRect = pygame.draw.circle(
            game_window, grey, (aro3_equipo2[0],z0-aro3_equipo2[2]), 5)

    circleRect = pygame.draw.circle(
        game_window, yellow, (sniper_pos[0], sniper_pos[1]), 2)
    circleRect = pygame.draw.circle(
        game_window, yellow, (sniper_pos[0],z0-sniper_pos[2]), 2)

    circleRect = pygame.draw.circle(
        game_window, grey, (bulldozer1_pos[0], bulldozer1_pos[1]), 4)
    circleRect = pygame.draw.circle(
        game_window, grey, (bulldozer1_pos[0],z0-bulldozer1_pos[2]), 4)

    circleRect = pygame.draw.circle(
        game_window, grey, (bulldozer2_pos[0], bulldozer2_pos[1]), 4)
    circleRect = pygame.draw.circle(
        game_window, grey, (bulldozer2_pos[0],z0-bulldozer2_pos[2]), 4)

    circleRect = pygame.draw.circle(
        game_window, orb_color, (orb_pos[0], orb_pos[1]), 5)
    circleRect = pygame.draw.circle(
        game_window, orb_color, (orb_pos[0],z0-orb_pos[2]), 5)


    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser1_equipo1_pos[0], chaser1_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser1_equipo1_pos[0]+5, chaser1_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(           #jugador perspectiva xz
        chaser1_equipo1_pos[0],z0-chaser1_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser1_equipo1_pos[0]+5,z0-chaser1_equipo1_pos[2], 5, 10))

    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser2_equipo1_pos[0], chaser2_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser2_equipo1_pos[0]+5, chaser2_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(           #jugador perspectiva xz
        chaser2_equipo1_pos[0],z0-chaser2_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser2_equipo1_pos[0]+5,z0-chaser2_equipo1_pos[2], 5, 10))

    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser3_equipo1_pos[0], chaser3_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser3_equipo1_pos[0]+5, chaser3_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(           #jugador perspectiva xz
        chaser3_equipo1_pos[0],z0-chaser3_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        chaser3_equipo1_pos[0]+5,z0-chaser3_equipo1_pos[2], 5, 10))

    pygame.draw.rect(game_window, green, pygame.Rect(
        beater1_equipo1_pos[0], beater1_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        beater1_equipo1_pos[0]+5, beater1_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(             #xz persepctiva
        beater1_equipo1_pos[0],z0-beater1_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red,pygame.Rect(
        beater1_equipo1_pos[0]+5,z0-beater1_equipo1_pos[2], 5, 10))

    pygame.draw.rect(game_window, green, pygame.Rect(
        beater2_equipo1_pos[0], beater2_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        beater2_equipo1_pos[0]+5, beater2_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(             #xz persepctiva
        beater2_equipo1_pos[0],z0-beater2_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red,pygame.Rect(
        beater2_equipo1_pos[0]+5,z0-beater2_equipo1_pos[2], 5, 10))

    pygame.draw.rect(game_window, cian, pygame.Rect(
        seeker_equipo1_pos[0], seeker_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        seeker_equipo1_pos[0]+5, seeker_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, cian, pygame.Rect(             #xz perspectiva
        seeker_equipo1_pos[0],z0-seeker_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        seeker_equipo1_pos[0]+5,z0-seeker_equipo1_pos[2], 5, 10))


    pygame.draw.rect(game_window, pink, pygame.Rect(
        keeper_equipo1_pos[0], keeper_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        keeper_equipo1_pos[0]+5, keeper_equipo1_pos[1], 5, 10))
    pygame.draw.rect(game_window, pink, pygame.Rect(            #xz persepctiva
        keeper_equipo1_pos[0],z0-keeper_equipo1_pos[2], 5, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        keeper_equipo1_pos[0]+5,z0-keeper_equipo1_pos[2], 5, 10))

    ########################################################################## equipo 2 visitantes

    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser1_equipo2_pos[0], chaser1_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser1_equipo2_pos[0]+5, chaser1_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(           #jugador perspectiva xz
        chaser1_equipo2_pos[0],z0-chaser1_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser1_equipo2_pos[0]+5,z0-chaser1_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser2_equipo2_pos[0], chaser2_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser2_equipo2_pos[0]+5, chaser2_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(          #perspectiva xz
        chaser2_equipo2_pos[0],z0-chaser2_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser2_equipo2_pos[0]+5,z0-chaser2_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, orange, pygame.Rect(
        chaser3_equipo2_pos[0], chaser3_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser3_equipo2_pos[0]+5, chaser3_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(           # perspectiva xz
        chaser3_equipo2_pos[0],z0-chaser3_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        chaser3_equipo2_pos[0]+5,z0-chaser3_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, green, pygame.Rect(
        beater1_equipo2_pos[0], beater1_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        beater1_equipo2_pos[0]+5, beater1_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(            #xz persepctiva
        beater1_equipo2_pos[0],z0-beater1_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue,pygame.Rect(
        beater1_equipo2_pos[0]+5,z0-beater1_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, green, pygame.Rect(
        beater2_equipo2_pos[0], beater2_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        beater2_equipo2_pos[0]+5, beater2_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(            #xz persepctiva
        beater2_equipo2_pos[0],z0-beater2_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue,pygame.Rect(
        beater2_equipo2_pos[0]+5,z0-beater2_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, cian, pygame.Rect(
        seeker_equipo2_pos[0], seeker_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        seeker_equipo2_pos[0]+5, seeker_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, cian, pygame.Rect(           #xz perspectiva
        seeker_equipo2_pos[0],z0-seeker_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        seeker_equipo2_pos[0]+5,z0-seeker_equipo2_pos[2], 5, 10))

    pygame.draw.rect(game_window, purple, pygame.Rect(
        keeper_equipo2_pos[0], keeper_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        keeper_equipo2_pos[0]+5, keeper_equipo2_pos[1], 5, 10))
    pygame.draw.rect(game_window, purple, pygame.Rect(         #xz persepctiva
        keeper_equipo2_pos[0],z0-keeper_equipo2_pos[2], 5, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(
        keeper_equipo2_pos[0]+5,z0-keeper_equipo2_pos[2], 5, 10))
cargar_jugadores()
while True:# Main Function

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     change_to = 'UP'
            # if event.key == pygame.K_DOWN:
            #     change_to = 'DOWN'
            # if event.key == pygame.K_LEFT:
            #     change_to = 'LEFT'
            # if event.key == pygame.K_RIGHT:
            #     change_to = 'RIGHT'
            if event.key == pygame.K_UP:
                direction = 'UP'
                chaser1_equipo1_pos[1] -= 5
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
                chaser1_equipo1_pos[1] += 5
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
                chaser1_equipo1_pos[0] -= 5
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
                chaser1_equipo1_pos[0] += 5
            if event.key == pygame.K_1:
                orb_pos[2] += orb_velocidad*2
            if event.key == pygame.K_3:
                orb_pos[2] -= orb_velocidad*2



            if event.key == pygame.K_i:
                chaser1_equipo2_pos[1] -= 20
            if event.key == pygame.K_k:
                chaser1_equipo2_pos[1] += 20
            if event.key == pygame.K_j:
                chaser1_equipo2_pos[0] -= 20
            if event.key == pygame.K_l:
                chaser1_equipo2_pos[0] += 20
    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    # if change_to == 'UP' and direction != 'DOWN':
    #      direction = 'UP'
    # if change_to == 'DOWN' and direction != 'UP':
    #      direction = 'DOWN'
    # if change_to == 'LEFT' and direction != 'RIGHT':
    #      direction = 'LEFT'
    # if change_to == 'RIGHT' and direction != 'LEFT':
    #      direction = 'RIGHT'

    # Moving the snake
    # if direction == 'UP':
    #     #snake_position[1] -= 0.000001
    #     orb_pos[1] -= 40
    # if direction == 'DOWN':
    #     #snake_position[1] += 0.000001
    #     orb_pos[1] += 40
    # if direction == 'LEFT':
    #     #snake_position[0] -= 0.000001
    #     orb_pos[0] -= 40
    # if direction == 'RIGHT':
    #     #snake_position[0] += 0.000001
    #     orb_pos[0] += 40

    #chaser1_equipo1_pos
    sniper()
    bulldozer1()
    bulldozer2()
    orb()
    jugadores()


    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10

  #  snake_body.insert(0, list(snake_position))
  #  if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
  #      score += 10
  #      fruit_spawn = False
  #  else:
  #      snake_body.pop()

  #  if not fruit_spawn:
  #      fruit_position = [random.randrange(1, (window_x//10)) * 10,
  #                        random.randrange(1, (window_y//10)) * 10]

  #  fruit_spawn = True
    game_window.fill(black)

  #  for pos in snake_body:
  #      pygame.draw.rect(game_window, green,
  #                       pygame.Rect(pos[0], pos[1], 10, 10))
   # pygame.draw.rect(game_window, white, pygame.Rect(
   #     fruit_position[0], fruit_position[1], 10, 10))


    draw()

    # circleRect = pygame.draw.circle(game_window, (100,100,100), (300, 30), 5)



    # Game Over conditions
    #if snake_position[0] < 0 or snake_position[0] > window_x-10:
    #    game_over()
    #if snake_position[1] < 0 or snake_position[1] > window_y-10:
    #    game_over()

    # Touching the snake body
    #for block in snake_body[1:]:
    #    if snake_position[0] == block[0] and snake_position[1] == block[1]:
    #        game_over()

    # displaying score countinuously
    show_score(1, white, 'times new roman', 30)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refres Rate
    fps.tick(velocidad)
#creditos:
#asesor en investigacion valmg7(persona en discord)
