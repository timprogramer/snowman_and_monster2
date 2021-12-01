import wrap
#мир и координаты
wrap.world.create_world(700,700,200,200)
wrap.world.set_back_color(255, 90, 0)
x=500
y=300


#создание центрльного пакмена и вопрос
answer=int(input("введите размер?"))
wrap.sprite.add("pacman",60,350,"player1")

#снеговик монстр средний
wrap.sprite.add("pacman",x,y,"enemy_ill_blue1")
wrap.sprite.set_size(1,answer,answer)

#снеговик монстр маленкий
answer1=answer/2
wrap.sprite.add("pacman",x,y-answer/2-answer1/2,"enemy_ill_blue1")
wrap.sprite.set_size(2,answer1,answer1)




