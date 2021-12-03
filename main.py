import wrap,time
#мир и координаты
wrap.world.create_world(700,700,200,200)
wrap.world.set_back_color(255, 90, 0)
x=500
y=300


#создание центрльного пакмена и вопрос
answer=int(input("введите размер?"))
wrap.sprite.add("pacman",60,350,"player1",False)

#новогодний монстр средний
wrap.sprite.add("pacman",x,y,"enemy_ill_blue1")
wrap.sprite.set_size(1,answer,answer)

#новогодний монстр маленкий
answer1=answer/2
wrap.sprite.add("pacman",x,y-answer/2-answer1/2,"enemy_ill_blue1")
wrap.sprite.set_size(2,answer1,answer1)

#новогодний монстр большой
answer2=answer*2
wrap.sprite.add("pacman",x,y+answer2-answer/2,"enemy_ill_blue1")
wrap.sprite.set_size(3,answer2,answer2)

#пакмен виден
time.sleep(3)
wrap.sprite.add("pacman",60,y,"player1")

#поворот новогоднего монстра
wrap.actions.set_angle_modif(1,270)
wrap.actions.set_angle_modif(2,270)
wrap.actions.set_angle_modif(3,270)

#прыжок новогоднего монстра
wrap.actions.move_to(2,60,y)
wrap.actions.move_to(1,60,y)
wrap.actions.move_to(3,60,y)

#смерть пакмена
wrap.sprite.add_text("пока...",60,y-200,"Arial")






