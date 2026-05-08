# Google simulator 
from kandinsky import *

BLEU = (66, 133, 244)
ROUGE = (234, 67, 53)
JAUNE = (251, 188, 5)
VERT = (52, 168, 83)

BLANC = (255, 255, 255)
GRIS = (235, 235, 235)
GRIS2 = (180, 180, 180)

fill_rect(0, 0, 320, 222, BLANC)

x = 92
y = 60

def logo(txt, px, couleur):
    draw_string(txt, px, y, couleur, BLANC)
    draw_string(txt, px+1, y, couleur, BLANC)
    draw_string(txt, px, y+1, couleur, BLANC)
    draw_string(txt, px+1, y+1, couleur, BLANC)

logo("G", x, BLEU)
logo("o", x+17, ROUGE)
logo("o", x+31, JAUNE)
logo("g", x+45, BLEU)
logo("l", x+59, VERT)
logo("e", x+67, ROUGE)

bx = 42
by = 108
bw = 236
bh = 34

fill_rect(bx, by, bw, bh, GRIS2)
fill_rect(bx+2, by+2, bw-4, bh-4, BLANC)

draw_string("Rechercher sur Google", 63, 117, (120,120,120), BLANC)

fill_rect(92, 165, 58, 22, GRIS)
fill_rect(170, 165, 58, 22, GRIS)

draw_string("Google", 100, 170, (80,80,80), GRIS)
draw_string("J'ai", 182, 170, (80,80,80), GRIS)
