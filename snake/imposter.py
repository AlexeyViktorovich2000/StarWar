import pygame as pg
import random
import time

pg.init()
pg.font.init()


f1 = pg.font.Font(None, 20)


sound2 = pg.mixer.Sound('expl3.wav')
sound1 = pg.mixer.Sound('expl6.wav')
sound3 = pg.mixer.Sound('pew.wav')
pg.mixer.music.load('marsh.wav')
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops=-1)
WIDTH = 1200
HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FIRE = (255, 0, 0)
BODY = (0, 0, 255)
# Размер точки
q=15
def word():
    for ex2 in range(0,5):
        for z2 in range(0,10):
            textA = f1.render('А', True, (180, 180, 180),(0,0,0))
            place = textA.get_rect(center=(3*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2))
            sc.blit(textA, place)

            textB = f1.render('Б', True, (180, 180, 180),(0,0,0))
            place = textB.get_rect(center=(3*q+q//2+8*q*z2+q, 2*q+q//2+8*q*ex2))
            sc.blit(textB, place)

            textC = f1.render('В', True, (180, 180, 180),(0,0,0))
            place = textC.get_rect(center=(3*q+q//2+8*q*z2+2*q, 2*q+q//2+8*q*ex2))
            sc.blit(textC, place)

            textD = f1.render('Г', True, (180, 180, 180),(0,0,0))
            place = textD.get_rect(center=(3*q+q//2+8*q*z2+3*q, 2*q+q//2+8*q*ex2))
            sc.blit(textD, place)

            textE = f1.render('Д', True, (180, 180, 180),(0,0,0))
            place = textE.get_rect(center=(3*q+q//2+8*q*z2+4*q, 2*q+q//2+8*q*ex2))
            sc.blit(textE, place)

            text1 = f1.render('1', True, (180, 180, 180),(0,0,0))
            place = text1.get_rect(center=(2*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2+q))
            sc.blit(text1, place)

            text2 = f1.render('2', True, (180, 180, 180),(0,0,0))
            place = text2.get_rect(center=(2*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2+2*q))
            sc.blit(text2, place)

            text3 = f1.render('3', True, (180, 180, 180),(0,0,0))
            place = text3.get_rect(center=(2*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2+3*q))
            sc.blit(text3, place)

            text4 = f1.render('4', True, (180, 180, 180),(0,0,0))
            place = text4.get_rect(center=(2*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2+4*q))
            sc.blit(text4, place)

            text5 = f1.render('5', True, (180, 180, 180),(0,0,0))
            place = text5.get_rect(center=(2*q+q//2+8*q*z2, 2*q+q//2+8*q*ex2+5*q))
            sc.blit(text5, place)

            textAlpha = f1.render('Альфа', True, (180, 180, 180),(0,0,0))
            place = textAlpha.get_rect(center=(5*q+8*5*q*z2, q+q//2+8*q*ex2))
            sc.blit(textAlpha, place)
            
            textBeta = f1.render('Бета', True, (180, 180, 180),(0,0,0))
            place = textBeta.get_rect(center=(13*q+8*5*q*z2, q+q//2+8*q*ex2))
            sc.blit(textBeta, place)

            textGamma = f1.render('Гамма', True, (180, 180, 180),(0,0,0))
            place = textGamma.get_rect(center=(21*q+8*5*q*z2, q+q//2+8*q*ex2))
            sc.blit(textGamma, place)

            textDelta = f1.render('Дельта', True, (180, 180, 180),(0,0,0))
            place = textDelta.get_rect(center=(29*q+8*5*q*z2, q+q//2+8*q*ex2))
            sc.blit(textDelta, place)

            textEpsilon = f1.render('Эпсилон', True, (180, 180, 180),(0,0,0))
            place = textEpsilon.get_rect(center=(37*q+8*5*q*z2, q+q//2+8*q*ex2))
            sc.blit(textEpsilon, place)

            textBY = f1.render('Позавчера', True, (180, 180, 180),(0,0,0))
            place = textBY.get_rect(center=(21*q+8*5*q*z2, q//1.4))
            sc.blit(textBY, place)

            textY = f1.render('Вчера', True, (180, 180, 180),(0,0,0))
            place = textY.get_rect(center=(21*q+8*5*q*z2, q//1.4+8*q))
            sc.blit(textY, place)

            textT = f1.render('Сегодня', True, (180, 180, 180),(0,0,0))
            place = textT.get_rect(center=(21*q+8*5*q*z2, q//1.4+16*q))
            sc.blit(textT, place)

            textTm = f1.render('Завтра', True, (180, 180, 180),(0,0,0))
            place = textTm.get_rect(center=(21*q+8*5*q*z2, q//1.4+24*q))
            sc.blit(textTm, place)

            textTa = f1.render('Послезавтра', True, (180, 180, 180),(0,0,0))
            place = textTa.get_rect(center=(21*q+8*5*q*z2, q//1.4+24*q))
            sc.blit(textTa, place)

    pg.display.update()

#Расставим корабли ситхов
sith=[]
sith_screen=[]
s_ship=24
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            for m in range(1,6):
                sith.append([i,j,k,m,BLACK])
#print(sith)
#Координаты кораблей ситхов
s_death_star=[[3,3,4,2],[3,3,4,1],[3,3,4,3],[3,3,3,2],[3,3,5,2],[3,2,4,2],[3,4,4,2],[2,3,4,2],[4,3,4,2]]
s_star_destroyer_1=[[1,1,1,1],[1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1]]
s_star_destroyer_2=[[1,5,5,5],[1,5,5,4],[1,5,4,5],[1,4,5,5],[2,5,5,5]]
s_star_destroyer_3=[[5,1,1,1],[4,1,1,1],[5,2,1,1],[5,1,2,1],[5,1,1,2]]
#Функция установки кораблей ситхов
def comp_establish(stroke):
    for element in stroke:
        p=element
        p.append(BLACK)
        #print(p)
        sith.remove(p)
        p.remove(BLACK)
        p.append(BODY)
        sith.append(p)
comp_establish(s_death_star)
comp_establish(s_star_destroyer_1)
comp_establish(s_star_destroyer_2)
comp_establish(s_star_destroyer_3)
# print(sith)
#Расставим корабли джедаев, сначала зададим пустое пространство
jedi=[]
j_ship=24
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            for m in range(1,6):
                jedi.append([i,j,k,m,BLACK])
#Функция установки кораблей джедаев
def establish(c1,c2,c3,c4):
    point=[c1,c2,c3,c4,BLACK]
    jedi.remove(point)
    point.remove(BLACK)
    point.append(BODY)
    jedi.append(point)
# НАЧАЛО. ОТКЛЮЧИЛ НА ВРЕМЯ ОТЛАДКИ            
# Point1=int(input("\nВведите координаты центра звезды смерти: 1\n"))
# Point2=int(input("\nВведите координаты центра звезды смерти: 2\n"))
# Point3=int(input("\nВведите координаты центра звезды смерти: 3\n"))
# Point4=int(input("\nВведите координаты центра звезды смерти: 4\n"))
# КОНЕЦ. ОТКЛЮЧИЛ НА ВРЕМЯ ОТЛАДКИ
#НАЧАЛО. А ВОТ ЭТО НАДО СОВСЕМ УДАЛИТЬ ПОСЛЕ ОТЛАДКИ
Point1=3
Point2=3
Point3=3
Point4=3
#КОНЕЦ. А ВОТ ЭТО НАДО СОВСЕМ УДАЛИТЬ ПОСЛЕ ОТЛАДКИ
establish(Point1,Point2,Point3,Point4)
establish(Point1+1,Point2,Point3,Point4)
establish(Point1-1,Point2,Point3,Point4)
establish(Point1,Point2+1,Point3,Point4)
establish(Point1,Point2-1,Point3,Point4)
establish(Point1,Point2,Point3+1,Point4)
establish(Point1,Point2,Point3-1,Point4)
establish(Point1,Point2,Point3,Point4+1)
establish(Point1,Point2,Point3,Point4-1)
j_death_star=[[Point1,Point2,Point3,Point4,BODY],[Point1+1,Point2,Point3,Point4,BODY],[Point1-1,Point2,Point3,Point4,BODY],[Point1,Point2+1,Point3,Point4,BODY],[Point1,Point2-1,Point3,Point4,BODY],[Point1,Point2,Point3+1,Point4,BODY],[Point1,Point2,Point3-1,Point4,BODY],[Point1,Point2,Point3,Point4+1,BODY],[Point1,Point2,Point3,Point4-1,BODY]]
# Теперь расставим три звездных разрушителя
# НАЧАЛО. ОТКЛЮЧИЛ НА ВРЕМЯ ОТЛАДКИ
# for i in range(1,6):
#     Point1=int(input("\nВведите координаты первого звездного разрушителя: 1\n"))
#     Point2=int(input("\nВведите координаты первого звездного разрушителя: 2\n"))
#     Point3=int(input("\nВведите координаты первого звездного разрушителя: 3\n"))
#     Point4=int(input("\nВведите координаты первого звездного разрушителя: 4\n"))

#     establish(Point1,Point2,Point3,Point4)
# for i in range(1,6):
#     Point1=int(input("\nВведите координаты второго звездного разрушителя: 1\n"))
#     Point2=int(input("\nВведите координаты второго звездного разрушителя: 2\n"))
#     Point3=int(input("\nВведите координаты второго звездного разрушителя: 3\n"))
#     Point4=int(input("\nВведите координаты второго звездного разрушителя: 4\n"))

#     establish(Point1,Point2,Point3,Point4)
# for i in range(1,6):
#     Point1=int(input("\nВведите координаты третьего звездного разрушителя: 1\n"))
#     Point2=int(input("\nВведите координаты третьего звездного разрушителя: 2\n"))
#     Point3=int(input("\nВведите координаты третьего звездного разрушителя: 3\n"))
#     Point4=int(input("\nВведите координаты третьего звездного разрушителя: 4\n"))

#     establish(Point1,Point2,Point3,Point4)
# КОНЕЦ. ОТКЛЮЧИЛ НА ВРЕМЯ ОТЛАДКИ
#НАЧАЛО. А ВОТ ЭТО НАДО СОВСЕМ УДАЛИТЬ ПОСЛЕ ОТЛАДКИ
establish(1,1,1,1)
establish(2,1,1,1)
establish(1,2,1,1)
establish(1,1,2,1)
establish(1,1,1,2)
j_star_destroyer_1=[[1,1,1,1,BODY],[2,1,1,1,BODY],[1,2,1,1,BODY],[1,1,2,1,BODY],[1,1,1,2,BODY]]
establish(1,5,5,5)
establish(2,5,5,5)
establish(1,4,5,5)
establish(1,5,4,5)
establish(1,5,5,4)
j_star_destroyer_2=[[1,5,5,5,BODY],[2,5,5,5,BODY],[1,4,5,5,BODY],[1,5,4,5,BODY],[1,5,5,4,BODY]]
establish(5,5,5,5)
establish(4,5,5,5)
establish(5,4,5,5)
establish(5,5,4,5)
establish(5,5,5,4)
j_star_destroyer_3=[[5,5,5,5,BODY],[4,5,5,5,BODY],[5,4,5,5,BODY],[5,5,4,5,BODY],[5,5,5,4,BODY]]


#КОНЕЦ. А ВОТ ЭТО НАДО СОВСЕМ УДАЛИТЬ ПОСЛЕ ОТЛАДКИ

# Первый ход
hod="sit"
# Создаем игру и окно
pg.init()
pg.mixer.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Star War 4D")
clock = pg.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    
    # Обновление
    
    # Рендеринг
    sc.fill(BLACK)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        # Наносим удар мышью
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and hod=="jed":
                x_1=event.pos[0]//q
                y_1=event.pos[1]//q
                if (x_1<=40 and x_1%8>2) and (y_1<=40 and y_1%8>2):
                    z=x_1//8
                    t=y_1//8
                    x=x_1-8*z-2
                    y=y_1-8*t-2
                    
                    shoot=[x,y,z+1,t+1,BODY]
                
                    if shoot in sith:
                        #print("Попал")
                        sith.remove(shoot) 
                        shoot.remove(BODY)
                        shoot.append(FIRE)
                        sith.append(shoot)
                        sound2.play()
                        time.sleep(0.5)
                        s_ship-=1
                        sith_screen.append(shoot)
                        if s_ship==0:
                            running = False
                    else:
                        #print("Мазила!")
                        shoot.remove(BODY)
                        shoot.append(WHITE)
                        sith.append(shoot)
                        sith_screen.append(shoot)
                        sound3.play()
                        time.sleep(0.5)
                        hod="sit"
            
    for rect in sith_screen:
        x=rect[0]
        y=rect[1]
        z=rect[2]
        expanse=rect[3]
        color=rect[4]
        c_x=(z-1)*q*5+q*(x-1)+3*z*q
        c_y=(expanse-1)*q*5+q*(y-1)+3*expanse*q
        pg.draw.rect(sc, color, (c_x, c_y, q, q))
    for rect in jedi:
        x=rect[0]
        y=rect[1]
        z=rect[2]
        expanse=rect[3]
        color=rect[4]
        c_x=(z-1)*q*5+q*(x-1)+5*5*q+3*z*q+3*5*q
        c_y=(expanse-1)*q*5+q*(y-1)+3*expanse*q
        pg.draw.rect(sc, color, (c_x, c_y, q, q))   
    
    # Рисуем сетку
    # for h in range(0,5):
    #     pg.draw.line(sc, WHITE, [0, 5*q*h], [2*5*5*q, 5*q*h], 3)
    # for v in range(0,10):
    #     pg.draw.line(sc, WHITE, [5*q*v, 0], [5*q*v, 2*5*5*q], 3)
    for ex in range(0,5):
        for z1 in range(0,10):
            for h1 in range(2,9):
                pg.draw.line(sc, WHITE, [8*q*z1+2*q, q*h1+8*q*ex], [6*q+8*q*z1+2*q, q*h1+8*q*ex], 1)
            for v1 in range(0,7):
                pg.draw.line(sc, WHITE, [q*v1+8*q*z1+2*q, 2*q+8*q*ex], [q*v1+8*q*z1+2*q, 8*q+8*q*ex], 1)
    pg.draw.line(sc, WHITE, [615, 0], [615, 600], 5)
    if hod=="sit":
        flag=True
        while flag:
            i=random.randint(1,5)
            j=random.randint(1,5)
            k=random.randint(1,5)
            m=random.randint(1,5)
            shoot=[i,j,k,m,BODY]
            #print("удар на:",shoot)
            
            if shoot in j_death_star:
                for sh in j_death_star:
                    jedi.remove(sh) 
                    sh.remove(BODY)
                    sh.append(FIRE)
                    jedi.append(sh)
                    j_ship-=1
                    x=sh[0]
                    y=sh[1]
                    z=sh[2]
                    expanse=sh[3]
                    color=sh[4]
                    c_x=(z-1)*q*8+q*(x+2)+5*8*q
                    c_y=(expanse-1)*q*8+q*(y+2)
                    pg.draw.rect(sc, color, (c_x, c_y, q, q))
                    word()
                    
                    pg.display.flip() 
                    sound2.play()
                    time.sleep(0.5)
                    if j_ship==0:
                        running = False
            elif shoot in j_star_destroyer_1:
                for sh in j_star_destroyer_1:
                    jedi.remove(sh) 
                    sh.remove(BODY)
                    sh.append(FIRE)
                    jedi.append(sh)
                    j_ship-=1
                    x=sh[0]
                    y=sh[1]
                    z=sh[2]
                    expanse=sh[3]
                    color=sh[4]
                    c_x=(z-1)*q*8+q*(x+2)+5*8*q
                    c_y=(expanse-1)*q*8+q*(y+2)
                    pg.draw.rect(sc, color, (c_x, c_y, q, q))
                    word()
                    
                    pg.display.flip() 
                    sound2.play()
                    time.sleep(0.5)
                    if j_ship==0:
                        running = False
            elif shoot in j_star_destroyer_2:
        
                for sh in j_star_destroyer_2:
                    jedi.remove(sh) 
                    sh.remove(BODY)
                    sh.append(FIRE)
                    jedi.append(sh)
                    j_ship-=1
                    x=sh[0]
                    y=sh[1]
                    z=sh[2]
                    expanse=sh[3]
                    color=sh[4]
                    c_x=(z-1)*q*8+q*(x+2)+5*8*q
                    c_y=(expanse-1)*q*8+q*(y+2)
                    pg.draw.rect(sc, color, (c_x, c_y, q, q))
                    word()
                    pg.display.flip()
                    
                    sound2.play()
                    time.sleep(0.5)
                    if j_ship==0:
                        running = False
            elif shoot in j_star_destroyer_3:
                    
                for sh in j_star_destroyer_3:
                    jedi.remove(sh) 
                    sh.remove(BODY)
                    sh.append(FIRE)
                    jedi.append(sh)
                    j_ship-=1
                    x=sh[0]
                    y=sh[1]
                    z=sh[2]
                    expanse=sh[3]
                    color=sh[4]
                    c_x=(z-1)*q*8+q*(x+2)+5*8*q
                    c_y=(expanse-1)*q*8+q*(y+2)
                    pg.draw.rect(sc, color, (c_x, c_y, q, q))
                    word()
                    pg.display.flip()

                    
                    sound2.play()
                    time.sleep(0.5)
                    if j_ship==0:
                        running = False
            else:
                
                shoot.remove(BODY)
                shoot.append(FIRE)
                if not shoot in jedi: 
                    shoot.remove(FIRE)
                    shoot.append(WHITE)
                    jedi.append(shoot)
                    sound1.play()
                    hod="jed"
                    flag=False
                else:
                    continue
                    
    # После отрисовки всего, переворачиваем экран
    word()

    
    pg.display.flip()

pg.quit()