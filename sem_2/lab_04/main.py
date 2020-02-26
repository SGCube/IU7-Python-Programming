import pygame as pg
from pygame.locals import *
import pygame.time as time
from math import pi, sin, cos, sqrt
from random import randint

#########################
# КОНСТАНТЫ И ПАРАМЕТРЫ #
#########################

#параметры экраны
screen_width = 640
screen_height = 480
bg_color = (0, 0, 48)
milsec_update = 20  #интервал обновления экрана (в мс)

#планета (по центру)
planet = {"x" : int(screen_width / 2),
          "y" : int(screen_height / 2),
          "r" : 60,
          "angle" : 0,
          "da" : pi/360,
          "lwidth" : 4,
          "color" : (243, 71, 35),
          "lcolor" : (115, 25, 7),
          "lines" : [[[-2,-50],[-50,-2]],[[40,-40],[-40,40]],[[50,8],[8,50]]]}

#спутники
satellite1 = {"x" : planet["x"] - 6*planet["r"],
              "y" : planet["y"],
              "r" : 10,
              "xrot" : planet["x"],
              "yrot" : planet["y"],
              "rrot" : 3*planet["r"],
              "angle" : pi,
              "da" : pi/120,
              "lwidth" : 5,
              "color" : (194, 168, 148),
              "lcolor" : (153, 115, 86)}

satellite2 = {"x" : planet["x"] + 6*planet["r"],
              "y" : planet["y"],
              "r" : 20,
              "xrot" : planet["x"],
              "yrot" : planet["y"],
              "rrot" : 3*planet["r"],
              "angle" : 0,
              "da" : -pi/180,
              "lwidth" : 5,
              "color" : (196, 165, 95),
              "lcolor" : (138, 111, 50)}

#ракета
rocket = {"x" : randint(70, screen_width - 70),
          "y" : randint(70, screen_height - 70),
          "w" : 60,
          "h" : 60,
          "body" : Rect((0,0),(60,240)),
          "window" : (30, 40),
          "btm_1" : Rect((0,0),(30,60)),
          "btm_2" : Rect((30,0),(30,60)),
          "wind_r" : 15,
          "angle" : randint(-179,179),
          "speed" : 5,
          "lwidth" : 2,
          "main_col" : (255, 255, 255),
          "main_colb" : (240, 240, 240),
          "btm_col" : (153, 50, 204),
          "btm_colb" : (92, 31, 122),
          "window_col" : (66, 170, 255)}

#инициализация окна и поверхности экрана
pg.init()

pg.display.init()
pg.display.set_caption("PyGame Animation")
screen = pg.display.set_mode((screen_width, screen_height), 0, 0)

#########################
#       ФУНКЦИИ         #
#########################

#рисовка планеты
def planet_draw(p):
    x0, y0, r = p["x"], p["y"], p["r"]
    
    pg.draw.circle(screen, p["lcolor"], (x0, y0), r+p["lwidth"], 0)
    pg.draw.circle(screen, p["color"], (x0, y0), r, 0)

    for i in range(len(p["lines"])):
        x1, y1 = p["lines"][i][0][0], p["lines"][i][0][1]
        x2, y2 = p["lines"][i][1][0], p["lines"][i][1][1]
        pg.draw.line(screen, p["lcolor"], (x0+x1, y0+y1), (x0+x2, y0+y2),
                     p["lwidth"])

#вращение ракеты
def planet_rotate(p):
    p["angle"] += p["da"]
    if p["angle"] >= 2*pi:
        p["angle"] = 2*pi - p["angle"]

    for i in range(len(p["lines"])):
        angle = p["da"]
        x1, y1 = p["lines"][i][0][0], p["lines"][i][0][1]
        x2, y2 = p["lines"][i][1][0], p["lines"][i][1][1]
        p["lines"][i][0][0] = x1*cos(angle) + y1*sin(angle)
        p["lines"][i][0][1] = y1*cos(angle) - x1*sin(angle)
        p["lines"][i][1][0] = x2*cos(angle) + y2*sin(angle)
        p["lines"][i][1][1] = y2*cos(angle) - x2*sin(angle)
        
    return p

#рисовка спутников
def satellite_draw(sat):
    x0, y0, r = sat["x"], sat["y"], sat["r"]
    pg.draw.circle(screen, sat["lcolor"], (x0, y0), r+sat["lwidth"], 0)
    pg.draw.circle(screen, sat["color"], (x0, y0), r, 0)

#движение спутников
def satellite_move(sat):
    sat["angle"] += sat["da"]
    if sat["angle"] >= 2*pi:
        sat["angle"] = 2*pi - sat["angle"]
    
    x0, y0 = sat["xrot"], sat["yrot"]
    r, ang = sat["rrot"], sat["angle"]

    sat["x"] = x0 + int(r*cos(ang))
    sat["y"] = y0 - int(r*sin(ang))
    
    return sat

#проверка на столкновение спутников
def sat_colission_check(sat1,sat2):
    x1, y1, r1 = sat1["x"], sat1["y"], sat1["r"]
    x2, y2, r2 = sat2["x"], sat2["y"], sat2["r"]
    cline = sqrt((x2-x1)**2 + (y2-y1)**2)
    return (cline <= r1 + r2)

#рисовка ракеты
def rocket_draw(rk):
    rks = pg.Surface((rk["w"], 5*rk["h"]//4))
    rks.fill((0,0,0))
    rks.set_colorkey((0,0,0))
    position = (rk["x"] - rk["w"]//2, rk["y"] - rk["h"]//2)
    #основная часть
    rkbody = pg.Surface((rk["w"], rk["h"]))
    rkbody.fill((0,0,0))
    rkbody.set_colorkey((0,0,0))
    
    pg.draw.ellipse(rkbody, rk["main_col"], rk["body"], 0)
    pg.draw.circle(rkbody,rk["main_colb"],
                   rk["window"], rk["wind_r"] + 4, 0)
    pg.draw.circle(rkbody,rk["window_col"],
                   rk["window"], rk["wind_r"], 0)
    
    rks.blit(rkbody, (0,0))
    
    #задняя часть
    rkbtm = pg.Surface((rk["w"], rk["h"]//4))
    rkbtm.fill((0,0,0))
    rkbtm.set_colorkey((0,0,0))
    
    pg.draw.ellipse(rkbtm, rk["btm_col"], rk["btm_1"], 0)
    pg.draw.ellipse(rkbtm, rk["btm_col"], rk["btm_2"], 0)
    rks.blit(rkbtm, (0,rk["h"]))

    rks = pg.transform.rotate(rks, rk["angle"])
    screen.blit(rks, position)

#движение ракеты
def rocket_move(rk):
    dx = rk["speed"]*cos(pi/2 + rk["angle"]*pi/180)
    dy = -rk["speed"]*sin(pi/2 + rk["angle"]*pi/180)
    rk["x"] += int(dx)
    rk["y"] += int(dy)
    
    if (rk["x"] >= screen_width and -180<=rk["angle"]<=0) or (
        rk["x"] <= 0 and 0<=rk["angle"]<=180):
        rk["angle"] = - rk["angle"]
    if (rk["y"] >= screen_height and abs(rk["angle"])>=90) or (
        rk["y"] <= 0 and (abs(rk["angle"])<=90)):
        if rk["angle"] <= 0:
            rk["angle"] = -180 - rk["angle"]
        else:
            rk["angle"] = 180 - rk["angle"]
        

#########################
#     ОСНОВНОЙ ЦИКЛ     #
#########################

running = True
time.set_timer(USEREVENT + 1, milsec_update)

while running:
    for event in pg.event.get():
        #событие завершения
        if event.type == QUIT:
            running = False
        #обновление координат
        if event.type == USEREVENT + 1:
            planet_rotate(planet)
            satellite1 = satellite_move(satellite1)
            satellite2 = satellite_move(satellite2)
            if sat_colission_check(satellite1,satellite2):
                satellite1["da"] = -satellite1["da"]
                satellite2["da"] = -satellite2["da"]
            rocket_move(rocket)
            time.set_timer(USEREVENT + 1, milsec_update)

    #перерисовка экрана     
    screen.fill(bg_color)
    planet_draw(planet)
    satellite_draw(satellite1)
    satellite_draw(satellite2)
    rocket_draw(rocket)
    
    pg.display.flip()

pg.quit()
