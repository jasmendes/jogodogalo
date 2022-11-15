# -*- coding: cp1252 -*-
t=[0,0,0,0,0,0,0,0,0]

import random

def ver():
    c=0
    r=0
    if t[0]==t[1]==t[2]:r=t[0]
    if t[3]==t[4]==t[5]:r=t[3]
    if t[6]==t[7]==t[8]:r=t[6]
    if t[0]==t[3]==t[6]:r=t[0]
    if t[1]==t[4]==t[7]:r=t[1]
    if t[2]==t[5]==t[8]:r=t[2]
    if t[0]==t[4]==t[8]:r=t[0]
    if t[2]==t[4]==t[6]:r=t[2]

    if r:
        print " %i %i %i \n %i %i %i \n %i %i %i" % tuple(t)
        print 'Ganhou o jogador %i' %r
    
    return r

def vEm():
    p=t.count(0)
    if p==0:
        print " %i %i %i \n %i %i %i \n %i %i %i" % tuple(t)
        print 'Empate'
        return 11
    
def joga():
    l=[]
    for i,v in enumerate(t):
        if v==0: l.append(i)

   

      # VERIFICA DIAGONAL #
    if (t[0]==1 and t[4]==1) and t[8]==0:
        t[8]=2
    elif (t[0]==1 and t[8]==1) and t[4]==0:
        t[4]=2
    elif (t[8]==1 and t[4]==1) and t[0]==0:
        t[0]=2

    elif (t[2]==1 and t[4]==1) and t[6]==0:
        t[6]=2
    elif (t[2]==1 and t[6]==1) and t[4]==0:
        t[4]=2
    elif (t[6]==1 and t[4]==1) and t[2]==0:
        t[2]=2

         # VERIFICA HORIZONTAL #
    elif t[0]==1 and t[1]==1 and t[2]==0:
        t[2]=2
    elif t[1]==1 and t[2]==1 and t[0]==0:
        t[0]=2
    elif t[0]==1 and t[2]==1 and t[1]==0:
        t[1]=2    

    elif (t[3]==1 and t[4]==1) and t[5]==0:
        t[5]=2
    elif (t[3]==1 and t[5]==1) and t[4]==0:
        t[4]=2
    elif (t[5]==1 and t[4]==1) and t[3]==0:
        t[3]=2
        
    elif (t[6]==1 and t[7]==1) and t[8]==0:
        t[8]=2
    elif (t[6]==1 and t[8]==1) and t[7]==0:
        t[7]=2
    elif (t[8]==1 and t[7]==1) and t[6]==0:
        t[6]=2

    # VERIFICA VERTICAL #

    elif t[0]==1 and t[3]==1 and t[6]==0:
        t[6]=2
    elif t[0]==1 and t[6]==1 and t[3]==0:
        t[3]=2
    elif t[6]==1 and t[3]==1 and t[0]==0:
        t[0]=2

    elif t[1]==1 and t[4]==1 and t[7]==0:
        t[7]=2
    elif t[1]==1 and t[7]==1 and t[4]==0:
        t[4]=2
    elif t[7]==1 and t[4]==1 and t[1]==0:
        t[1]=2

    elif t[2]==1 and t[5]==1 and t[8]==0:
        t[8]=2
    elif t[2]==1 and t[8]==1 and t[5]==0:
        t[5]=2
    elif t[8]==1 and t[5]==1 and t[2]==0:
        t[2]=2

    elif t[4]==0:
        t[4]=2
  
        
    else:
        t[random.choice(l)]=2

while 1:
    print " %i %i %i \n %i %i %i \n %i %i %i" % tuple(t)

    m=1
    while m==1:
        x=int(raw_input('Posicao: '))-1
        if t[x]!=0:
            print 'Posição já ocupada'
        else :
            t[x]=1
            m=0
     
    if ver():break
    if vEm():break
    joga()
    if ver():break
    if vEm():break
