from ping_pong_lib import *

def restart():
  global player, ball1, pad1, pad2, score_j1, score_j2, white, black, player_has_change,player1_name,player2_name
  player_has_change = 1
  if player == 1:
    score_j1 += 1
    player = -1
  else:
    score_j2 += 1
    player = 1
  if score_j1 == 10 or score_j2 == 10:
    ball1.frenesie = True
    fill_rect(0,0,500,500,black)
    draw_string("New colours unlock",0,0)
    sleep(2)
        
  fill_rect(0,0,500,500,black)
  draw_string("scores:",100,70)
  draw_string(player1_name+": "+str(score_j1),100,110)
  draw_string(player2_name+": "+str(score_j2),100,150)
  sleep(2.3)
  fill_rect(0,0,500,500,black)
  for i in range (0,5):
    draw_string("Debut dans "+str(5 - i),0,0)
    sleep(1)
    fill_rect(0,0,500,500,black)
  ball1.start()
  pad1.start()
  pad2.start()
  pad2.afficher()
  pad1.afficher()  

def sign_nb(nb):
 if nb < 0:
   return -1
 else:
   return 1
    
def tours():
 global player
 if player == -1:
   player = 1
   return 1
 else:
   player = -1
   return -1   
  
def victory():
  global player, pad1, pad2, ball1
  if player == 1:
    if ball1.loose(player,pad2.posy) == True:
      restart()
  else:
    if ball1.loose(player,pad1.posy) == True:
      restart()
        
def depart():
  global pad2,ball1,player1_name,player2_name
  speed = int(input("Choisissez la vitesse de la \n balle (1/3)"))
  ball1.set_speed(speed)
  reponse = input("Voulez vous jouer avec une IA\n(o/n) ")
  print(reponse)
  if reponse == "o" or reponse == "0" or reponse == "O":
    pad2.ia = True
    level = int(input("Donnez le niveau de l Ia \n(0/5) "))
    pad2.set_ia_difficulty(level)
    player1_name = input("Rentrez votre nom: ")
    player2_name = "IA super forte :)"
  elif reponse == "n" or reponse == "N":
    pad2.ia = False
    player1_name = input("Rentrez le nom du j1: ")
    player2_name = input("Rentrez le nom du j2: ")
  else:
    print("erreur de reponse")
    depart()  
def fin():
  global black
  fill_rect(0,0,500,500,black)
  draw_string("Fin du jeu",0,0)

white = 255,255,255
black = 0,0,0
red = 255,0,0

player = -1
nb = 0
nb2 = 0
nb3 = 0
player_has_change = 0
score_j1 = 0
score_j2 = 0
player1_name = "j1"
player2_name = "j2"

ball1 = balle(white)
pad1 = raquette(0,70,white)
pad2 = IA(312,70,white)
depart()

fill_rect(0,0,500,500,black)
fill_rect(0,219,350,6,white)

pad1.afficher()
pad2.afficher()
ball1.start()

while keydown(KEY_BACK) == False:  
  victory()
  if pad2.ia == True:
   if nb != 0:
     if nb == nb2:
       nb = 1
       nb2 = 1
     else:
         pad2.monter(1 * nb3)
         nb2 += 1
            
  ball1.avancer(player)
  if keydown(KEY_RIGHTPARENTHESIS) == True:
    break
  if keydown(KEY_UP) == True:
    pad1.monter(-1)
  if keydown(KEY_DOWN) == True:
    pad1.descendre(1) 
  if ball1.touch(pad1.posy,pad2.posy,player) == 2:
    tours()
    ball1.rebondir(1)
    player_has_change = 1
  elif ball1.touch(pad1.posy,pad2.posy,player) == 3:
    ball1.rebondir(3) 
  if pad2.ia == True:
   if player == 1 and player_has_change == 1:
     nb = pad2.go(pad2.calcul(ball1.angle,player,ball1.mul,ball1.pixel,ball1.posx))
     nb3 = sign_nb(nb)
     nb = abs(nb)
     player_has_change = 0  
  else:
    if keydown(KEY_NINE) == True:
      pad2.monter(-1)
    if keydown(KEY_SIX) == True:
      pad2.descendre(1)       
 
fin()