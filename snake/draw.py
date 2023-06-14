import pygame as pg
import random
import sys
WIDTH = 1200
HEIGHT = 600
FPS = 30
# Наличие подбитого корабля джедаев
FOUND=False
nedobit=0
no_name=False
ugol=False
krest=False
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FIRE = (255, 0, 0)
BODY = (0, 0, 255)
# Размер точки
q=24
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
establish(1,5,5,5)
establish(2,5,5,5)
establish(1,4,5,5)
establish(1,5,4,5)
establish(1,5,5,4)
establish(5,5,5,5)
establish(4,5,5,5)
establish(5,4,5,5)
establish(5,5,4,5)
establish(5,5,5,4)

#КОНЕЦ. А ВОТ ЭТО НАДО СОВСЕМ УДАЛИТЬ ПОСЛЕ ОТЛАДКИ
# Передаточная функция, чтобы не выйти за границы
def bound_up(number):
    if number==5:
        return 3
    else:
        return number+1
def bound_down(number):
    if number==1:
        return 3
    else:
        return number-1        

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
                z=x_1//5
                t=y_1//5
                x=x_1-5*z+1
                y=y_1-5*t+1
                #app=[x,y,z+1,t+1]
                shoot=[x,y,z+1,t+1,BODY]
                #app_n=[app]
                #print(app)
                #print(app_n)
                #comp_establish(app_n)
                if shoot in sith:
                    #print("Попал")
                    sith.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    sith.append(shoot)
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
                    hod="sit"
            

    # r1 = pg.Rect((150, 20, 100, 75))
    for rect in sith_screen:
        x=rect[0]
        y=rect[1]
        z=rect[2]
        expanse=rect[3]
        color=rect[4]
        c_x=(z-1)*q*5+q*(x-1)
        c_y=(expanse-1)*q*5+q*(y-1)
        pg.draw.rect(sc, color, (c_x, c_y, q, q))
    for rect in jedi:
        x=rect[0]
        y=rect[1]
        z=rect[2]
        expanse=rect[3]
        color=rect[4]
        c_x=(z-1)*q*5+q*(x-1)+5*5*q
        c_y=(expanse-1)*q*5+q*(y-1)
        pg.draw.rect(sc, color, (c_x, c_y, q, q))   
    
    # Рисуем сетку
    for h in range(0,5):
        pg.draw.line(sc, WHITE, [0, 5*q*h], [2*5*5*q, 5*q*h], 3)
    for v in range(0,10):
        pg.draw.line(sc, WHITE, [5*q*v, 0], [5*q*v, 2*5*5*q], 3)
    for h1 in range(0,25):
        pg.draw.line(sc, WHITE, [0, q*h1], [2*5*5*q, q*h1], 1)
    for v1 in range(0,50):
        pg.draw.line(sc, WHITE, [q*v1, 0], [q*v1, 2*5*5*q], 1)
    if hod=="sit":
        flag=True
        while flag:
            if FOUND==True:
                # Вся ветка неактивна, поскольку FOUND не равен True
                if no_name:
                    shoot=[bound_down(i_base),j_base,k_base,m_base,BODY]
                    if shoot in jedi:
                         # Значит это угол!
                        ugol=True
                        jedi.remove(shoot) 
                        shoot.remove(BODY)
                        shoot.append(FIRE)
                        jedi.append(shoot)
                        j_ship-=1
                        nedobit+=1
                        #print(j_ship)
                        if j_ship==0:
                            running = False
                    if not shoot in jedi:
                        # Эх! это только точка, придётся искать дальше 
                        jedi.append(shoot)
                        hod="jed"
                        flag=False

                elif krest:
                    i_central=(i_base+bound_down(i_base)+bound_up(i_base))
                    j_central=j_base
                    k_central=k_base
                    m_central=m_base
                    # Уничтожение креста:
                    shoot=[i_central,j_central+1,k_central,m_central,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    shoot=[i_central,j_central-1,k_central,m_central,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    shoot=[i_central,j_central,k_central+1,m_central,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    shoot=[i_central,j_central,k_central-1,m_central,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    shoot=[i_central,j_central,k_central,m_central+1,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    shoot=[i_central,j_central,k_central,m_central-1,BODY]
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    if j_ship==0:
                        running = False
                    # Крест уничтожен!
                    print("Ха-ха! Твоя планета уничтожена. Сдавайся!")
                    FOUND=False
                # Бахнем по соседним
                shoot=[bound_up(i_base),j_base,k_base,m_base,BODY]
                if shoot in jedi:
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    nedobit+=1
                    #print(j_ship)
                    if j_ship==0:
                        running = False
                    shoot=[bound_down(i_base),j_base,k_base,m_base,BODY]
                    if shoot in jedi:
                        jedi.remove(shoot) 
                        shoot.remove(BODY)
                        shoot.append(FIRE)
                        jedi.append(shoot)
                        j_ship-=1
                        nedobit+=1
                        # Значит это звезда!
                        krest=True
                        #print(j_ship)
                        if j_ship==0:
                            running = False
                    else:
                        # Значит это угол!
                        ugol=True
                        shoot.remove(BODY)
                        shoot.append(WHITE)
                        if not shoot in jedi: 
                            jedi.append(shoot)
                            hod="jed"
                            flag=False
                else:
                    # Значит это недобитый угол или точка!
                    no_name=True
                    shoot.remove(BODY)
                    shoot.append(WHITE)
                    if not shoot in jedi: 
                        jedi.append(shoot)
                        hod="jed"
                        flag=False
            else:
                i=random.randint(1,5)
                j=random.randint(1,5)
                k=random.randint(1,5)
                m=random.randint(1,5)
                shoot=[i,j,k,m,BODY]
                #print("удар на:",shoot)
                if shoot in jedi:
                    # Включить одну строку после наладки ИИ
                    #FOUND=True
                    #print("Попал")
                    # Запомним базовую точку
                    i_base=i
                    j_base=j
                    k_base=k
                    m_base=m
                    jedi.remove(shoot) 
                    shoot.remove(BODY)
                    shoot.append(FIRE)
                    jedi.append(shoot)
                    j_ship-=1
                    #print(j_ship)
                    if j_ship==0:
                        running = False
                else:
                    #print("Протонная ракет ситхов на этот раз не достигла цели. Но бой продолжается!")
                    #Выводим сообщение. НАЧАЛО. Зависло ((
                    # f1 = pg.font.Font(None, 36)
                    # text1 = f1.render('Протонная ракет ситхов на этот раз не достигла цели. Но бой продолжается!', True,(180, 0, 0)) 
                    # sc.blit(text1, (10, 50))
                    # pg.display.update()
    
                    # while 1:
                    #     for i in pg.event.get():
                    #         if i.type == pg.QUIT:
                    #             sys.exit()
                    #Выводим сообщение. КОНЕЦ. Зависло ((
                    shoot.remove(BODY)
                    shoot.append(WHITE)
                    if not shoot in jedi: 
                        jedi.append(shoot)
                        hod="jed"
                        flag=False
                    
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

pg.quit()