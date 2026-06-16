import pygame as p
p.init()
s=p.display.set_mode((2,2),p.FULLSCREEN)
c=99
f=p.font.SysFont(0,c)
for x in range(700):t=f.render('adsux',0,(c,x/3,x/c),1);p.draw.line(s,(x/3,0,c),(0,x),(x*9,x-c));s.blit(t,([c-x,x-c][x>c],x));p.display.flip();p.event.wait(40)
