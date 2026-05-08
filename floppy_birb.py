from math import *
from kandinsky import fill_rect as rect, get_pixel as gpix, draw_string as ds, color
from ion import keydown as kd
from ion import *
from random import *
from time import *
colb=(150,200,250)
l=[
[0]*19,
[0]*7+[1]*6+[0]*6,
[0]*5+[1,1,2,2,2,1,6,6,1]+[0]*5,
[0]*4+[1,2,2,2,2,1,6,6,6,6,1]+[0]*4,
[0,0,1,1,1,1,2,2,2,1,6,6,6,1,6,1,0,0,0],
[0,1,5,5,5,5,1,2,2,1,6,6,6,1,6,1,0,0,0],
[0,1]+[5]*5+[1,2,2,1,6,6,6,6,1,0,0,0],
[0,1,2,5,5,5,2,1,2,2,2]+[1]*6+[0,0],
[0,0,1,2,2,2,1,2,2,2,1]+[4]*6+[1,0],
[0,0,0,1,1,1,3,3,3,1,4]+[1]*6+[0,0],
[0,0,0,1]+[3]*6+[1]+[4]*5+[1,0,0],
[0,0,0,0,1,1]+[3]*5+[1]*5+[0,0,0],
[0]*6+[1]*5+[0]*8,
[0]*19
]

cols=[(150,200,250),(10,10,10),(249,241,36),(249,194,44),(253,104,75),(250,252,233),(253,255,250)]
bl=(0,0,0)
wh=color(255,255,255)

def draw(y,last_y,px,py,score,deltad,rt,lrt):
  if last_y<y:
    rect(11,last_y-18,38,y-last_y,colb)
  if last_y>y:
    rect(11,y+15,38,last_y-y+5,colb)
  rt=radians(rt)
  lrt=radians(lrt)
  for idx in range(5):
    cx = ceil(px[idx])
    cy = py[idx]
    ccf = ceil(68*config[2]/100)
    #refresh
    rect(cx+32,cy+15,deltad,240-cy,colb)
    rect(cx+32,cy-15-ccf,deltad,-240,colb)
    #draw pipe
    rect(cx+1,cy+15,29,240-cy,'green')
    rect(cx+1,cy-15-ccf,29,-240,'green')
    rect(cx-1,cy+15,2,240-cy,bl)
    rect(cx-1,cy-ccf-15,2,-240,bl)
    rect(cx+30,cy+15,2,240-cy,bl)
    rect(cx+30,cy-15-ccf,2,-240,bl)
    #refresh
    rect(cx+36,cy,deltad,15,colb)
    rect(cx+36,cy-ccf,deltad,-15,colb)
    #better graphics
    rect(cx-5,cy+13,40,2,bl)
    rect(cx-5,cy,40,2,bl)
    rect(cx-6,cy,2,15,bl)
    rect(cx+35,cy,2,15,bl)
    rect(cx-5,cy-ccf-2,40,2,bl)
    rect(cx-5,cy-ccf-15,40,2,bl)
    rect(cx-6,cy-ccf-15,2,15,bl)
    rect(cx+35,cy-ccf-15,2,15,bl)
    #draw pipe entry
    rect(cx-4,cy-ccf-2,39,-11,'green')
    rect(cx-4,cy+2,39,11,'green')
    #draw player
  srt,crt=sin(rt)*2,cos(rt)*2
  for ys in range(14):
    for xs in range(19):
      pixel_x=30+floor((xs-9.5)*srt)+floor((ys-7)*crt)
      pixel_y=y+floor((ys-7)*srt)-floor((xs-9.5)*crt)
      cur_pixel=gpix(pixel_x,pixel_y)
      if cur_pixel==(82,195,0) or cur_pixel==(0,0,0):
        break
      rect(pixel_x,pixel_y,2,2,cols[l[ys][xs]])
  if not (gpix(155,20)==color(82, 195, 0) or gpix(165+len(str(score))*10,20)==color(82, 195, 0)):
    ds(str(score),155,20,wh,colb)

def menu(sel,config):
  ds("Floppy Birb",100,30,wh,colb)    
  if sel==2:
    ds(">Start [OK]  ",70,60,wh,colb)
    ds("Config   ",70,80,wh,colb)
  if sel==1:
    ds("Start      ",70,60,wh,colb)
    ds(">Config [>]  ",70,80,wh,colb)
  if sel>=3:
    ds("Gravity : "+str(config[0])+"%     ",20,80,wh,colb)
    ds("Jump force : "+str(config[1])+"%     ",20,100,wh,colb)
    ds("Spaced pipes : "+str(config[2])+"%     ",20,120,wh,colb)
    ds("Config",120,50,wh,colb)
    ds("[<] Back",10,10,wh,colb)
    ds(">",10,80+20*(sel-3),wh,colb)

config=[100,100,100]
  
def main():
  rect(0,0,320,240,colb)
  y=120.0
  vy=0.0
  r=90
  px,py=[100.0,200.0,300.0,400.0,500.0],[randrange(100,200),randrange(100,200),randrange(100,200),randrange(100,200),randrange(100,200)]
  last_y=y
  last_r=90
  score=0
  sel=2
  end=False
  move=True
  cooldown=0
  hasScored=False
  while kd(4):
    pass
  while not kd(4):
    if kd(2) and sel==2:
      sel=1
      
    while not sel == 2:
      if kd(1) and sel==1:
        sel=2
        sleep(0.2)      
        rect(0,0,360,240,colb)
      if kd(3) and sel==1:
        sel=3
        rect(0,0,360,240,colb)
        sleep(0.1)      
      if kd(0) and sel>=3:
        rect(0,0,360,240,colb)
        sel=1
        sleep(0.1)      
      if sel-2<len(config) and sel>=3 and kd(2):
        sel+=1
        rect(10,40,8,200,colb)  
        sleep(0.2)
      if sel-3>0 and sel>=3 and kd(1):
        sel-=1
        rect(10,40,8,200,colb)  
        sleep(0.2)      
      if sel>=3 and kd(45):
        config[sel-3]+=5
        sleep(0.15)      
      if sel>=3 and kd(46):
        config[sel-3]-=5
        sleep(0.15)        
      menu(sel,config)
    menu(sel,config)
  while kd(4):
    rect(0,0,320,240,colb)
  mt=monotonic()
  draw(ceil(y),ceil(last_y),px,py,score,2,r,last_r)
  delta=monotonic()-mt
  while end==False:
    mt=monotonic()
    if kd(4):
      cooldown+=1
    if cooldown==1 and move:
      vy=(-9*config[1]/100)
      r=30
    if not kd(4):
      cooldown=0
    for i in range(5):
      if move:
        px[i]=px[i]-(60*delta)
      if px[i]<-40:
        px[i]=480
        py[i]=randrange(100,200)
      if px[i]<=45 and px[i]>=-17:
        if not hasScored:
          score+=1
          hasScored=True
        if y+13>py[i] or y-13<py[i]-ceil(68*config[2]/100):
          move=False
      if px[i]<-17:
        hasScored=False
    draw(ceil(y),ceil(last_y),px,py,score,ceil(1+delta*60),r,last_r)
    last_r,last_y=r,y
    y+=vy*delta*30
    if vy<10:
      vy+=(config[0]/100)*delta*45
    if r<179:
      r+=delta*150
    if y>=215:
      end=True
    delta=monotonic()-mt
  ds("Score : "+str(score),108,80,bl,wh)
  ds("Press OK to go back",60,100,bl,wh)
  ds("to main menu",90,120,bl,wh)
  while kd(4):
    pass
  while not kd(4):
    pass

while True:
  main()
