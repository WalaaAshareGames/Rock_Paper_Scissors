
from game import game




def Welcoming() :
    
    print ("""
     ###########################################################################
                                                    
                  Welcome to our Rock_Paper_Scissors game        
          The principle of this game is that the rock breaks the scissors 
          and the scissors cut the paper and the paper covers the room
                 Whoever makes the strongest move wins the game
                 rock > scissors, scissors > paper, paper > rock

           This game requires two people and It consists of three rounds,
                and whoever gets the highest total wins the game

                Rock represent by "R"
                paper represent by "P"
                scissors represent by "S"

                hint: you can play with computer or with your partner
    ##############################################################################
    """)


Welcoming()
numper_player=input("if you want to play with computer enter 1 ,if you want to play with your partner enter 2 \n")

game.set_player(numper_player)

i=0
total=0
while i<3:
   
    char=input("enter you char (R:Rock ,P:Paper ,S:Scissors)")
    total+=game.result(char)
    print(total)
    i +=1

if total==0:
    print("Draw")
elif total>0:
    print("Winner")
else :
    print("Loser")

  


