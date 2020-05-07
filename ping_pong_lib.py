from math import *
from cmath import *
from random import *
from kandinsky import *
from ion import *
from time import *

class balle:
  
  def __init__(self,color):
    self.pixel = 0
    self.color = color
    self.last_player = 1
    self.angle = 6
    self.mul = 1
    self.frenesie = False
      
  def __repr__(self):
    return "{} {}".format(
    self.posx, self.posy)
    
  def __str__(self):
    return "{} {}".format(
    self.posx, self.posy)
  
  def __int__(self):
    return self.posy    
  
  def __getattr__(self,nom):
    print("Pas d attribut nomme {} ici.".format(nom))
  
  def __setattr__(self, nom_attr, val_attr):
    object.__setattr__(self, nom_attr, val_attr)
    
  def change(self):
    list = [-1,1]
    self.mul = choice(list)
  
  def set_speed(self,speed):
    if speed <= 3 and speed >= 1:
      if speed == 1:
        speed = 3
      elif speed == 3:
        speed = 1  
      self.speed = speed + 4
  
  def start(self):
    self.turn = 1
    self.posx = 100
    self.posy = 95
    self.angle = 6
    fill_rect(self.posx,self.posy,5,5,self.color) 
  
  def touch(self,posy_pad1,posy_pad2,player):
    
    if player == -1:
      
      if self.posx <= 5  and self.posy <= posy_pad1 + 50 and self.posy >= posy_pad1:
        return 2      
    
    if player == 1:
      
      if self.posx >= 303 and self.posy <= int(posy_pad2) + 50 and self.posy >= posy_pad2:
        return 2  
    
    if self.posx <= 320 and self.posx >= 0:
      
      if self.posy == 0 or self.posy +1 == 216:
        return 3       
        
  def set_avancer(self, posx, posy):
    black = 0,0,0 
    fill_rect(self.posx,self.posy,5,5,black)
    self.posx += posx    
    self.posy -= posy
    if self.frenesie == True:
      self.color = randint(0,255),randint(0,255),randint(0,255)
    fill_rect(self.posx,self.posy,5,5,self.color)
  
  def avancer(self, player):
     
     if self.angle == 6:
       self.set_avancer(1 * player,0)
     
     if self.angle == 1:
       self.set_avancer(1 * player,5 * self.mul)
     
     if self.angle == 2:
       
       if self.turn < self.speed - 3:
         self.turn += 1
       
       else:
        self.set_avancer(2 * player,5 * self.mul)
        self.turn = 1
     
     if self.angle == 3:
       
       if self.turn < self.speed - 2:
         self.turn += 1
       
       else:  
        self.set_avancer(3 * player,5 * self.mul)
        self.turn = 1
     
     if self.angle == 4:
       
       if self.turn < self.speed - 1:
         self.turn += 1
       
       else:  
         self.set_avancer(4 * player,5 * self.mul)
         self.turn = 1
     if self.angle == 5:
       
       if self.turn < self.speed:
         self.turn += 1
       
       else:
         self.set_avancer(5 * player,5 * self.mul)
         self.turn = 1
           
  def rebondir(self,touch):
     
     if touch == 1 or touch == 2:
       self.pixel = self.posy
       self.turn = 0
       self.angle = randint(3,5)
       self.change()
     
     elif touch == 3:
       self.turn = 10
       
       if self.mul == -1:
         self.mul = 1
       
       elif self.mul == 1:
         self.mul = -1   
  
  def loose(self,player,raquette_posy):
    if player == 1:
      if self.posx >= 316:
         if self.posy < raquette_posy or self.posy > raquette_posy + 50:
            return True
         else:
            return False    
      else:
        return False
    else:
       if self.posx <= 0:
         if self.posy < raquette_posy or self.posy > raquette_posy + 50:                
           return True
         else:
           return False
       else:
          return False
          
class raquette:
  black = 0,0,0
  
  def __init__(self, posx, posy,color):
    self.ia = False
    self.base_posy = posy
    self.base_posx = posx
    self.posx = posx
    self.posy = posy
    self.color = color
  
  def __repr__(self):
    return "{} {}".format(
    self.posx, self.posy)
  
  def __str__(self):
    return "{} {}".format(
    self.posx, self.posy)
  
  def __int__(self):
    return self.posy
    
  def __getattr__(self, nom):
    print("Pas attribut nomme {} ici.".format(nom))
  
  def __setattr__(self, nom_attr, val_attr):
    object.__setattr__(self, nom_attr, val_attr)
    
  def start(self):
    self.posx = self.base_posx
    self.posy = self.base_posy
  
  def descendre(self,nb):
    black = 0,0,0
    if self.posy <= 170:
      fill_rect(self.posx,self.posy,5,50,black)
      self.posy += nb
      fill_rect(self.posx,self.posy,5,50,self.color)
  
  def monter(self,nb):
    black = 0,0,0
    if self.posy >= 0:
      fill_rect(self.posx,self.posy,5,50,black)
      self.posy += nb
      fill_rect(self.posx,self.posy,5,50,self.color)
  
  def afficher(self):
    fill_rect(self.posx,self.posy,5,50,self.color)      
   
class IA(raquette):
   
   def calcul(self, angle, player, random, depart_y, depart_x):
     if player == 1:
       if angle == 6:
         return self.posy
       self.depart_x = depart_x
       while self.depart_x <= 303:
         self.depart_x += (angle * player)  
         depart_y -= (5 * random)
         if depart_y <= 0 or depart_y + 1 >= 216:
           if depart_y <= 0:
             depart_y = 0
           if depart_y + 1 >= 216:
             depart_y = 215  
           random *= -1
       self.set_go_position = depart_y
       return self.set_go_position    
     
       if player == -1:
        if angle == 6:
          return self.posy
        self.depart_x = depart_x
        while self.depart_x >= 0:
         self.depart_x += (angle * player)  
         depart_y -= (5 * random)
         if depart_y <= 0 or depart_y + 1 >= 216:
           if depart_y <= 0:
             depart_y = 0
           if depart_y + 1 >= 216:
             depart_y = 215  
           random *= -1
        self.set_go_position = depart_y
        return self.set_go_position 
   def set_ia_difficulty(self,difficulty):
     if difficulty <= 5 or difficulty >= 1:
       self.difficulty = (5 - difficulty) * 5   
   
   def go(self,go_position):
     self.if_fail = randint(0,100)
     if self.if_fail <= self.difficulty:
       self.if_fail = True
     else:
       self.if_fail = False
         
     if go_position > self.posy + 50:
        #balle en dessous de la raquette
        self.nb_tours = (self.posy - go_position + 25) * -1   
        if self.if_fail == True:
          self.nb_tours -= randint(25,50)
        if abs(self.nb_tours) + self.posy >= 171:
          return 171 - self.posy
        return int(self.nb_tours -1)
     
     elif go_position < self.posy:
        #balle au dessus de la raquette
        self.nb_tours = go_position - self.posy - 25
        if self.if_fail == True:
          self.nb_tours += randint(25,50)
        if self.posy - abs(self.nb_tours) <= 0:          
          return self.posy * -1
        return self.nb_tours +1 
     
     elif go_position <= self.posy + 50 and go_position >= self.posy:
        return 0