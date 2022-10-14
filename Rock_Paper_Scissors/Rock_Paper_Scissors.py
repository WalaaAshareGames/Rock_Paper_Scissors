
if __name__=="__main__":
    from game import game1
else:
    from .game import game1



def Welcoming() :
    
    return ("""
     ###########################################################################
                                                    
        Welcome to our Rock_Paper_Scissors game 

        The principle of this game is that the rock smashes the scissors 
        and the scissors cut the paper and the paper covers the rock
        Whoever makes the strongest move wins the game
        rock > scissors, scissors > paper, paper > rock

        This game requires two player and It consists of three rounds,
        and whoever gets the highest total wins the game

        Rock represent by "R"
        paper represent by "P"
        scissors represent by "S"

        You have to enter a character and then press the enter key.

        hint: you can play with computer or with your partner
    ##############################################################################
    """)

def single_player(total):
    name=input("enter your name\n")
    i=0
    while i<3:
   
        char=input("enter your char (R:Rock ,P:Paper ,S:Scissors)\n")
        total+=game1.result(char.upper())
        # print(total)
        i +=1
    if total==0:
        print(f"total point = {total}")
        return("**** Draw *****")
    elif total>0:
        print(f"total point = {total}")
        return(f"***** {name} is Winner ********")
    else :
        print(f"total point = {total}")
        return(f"****** {name} you lost *********")


def tow_player(total):
    name=input("enter player 1 name\n ")
    partner_name=input("enter player 2 name\n ")
    i=0
    while i<3:
   
        char1=input(f"{name} char (R:Rock ,P:Paper ,S:Scissors)\n")
        char2=input(f"{partner_name}  char (R:Rock ,P:Paper ,S:Scissors)\n")
        total+=game1.result2(char1.upper(),char2.upper())  
        # print(total)
        i +=1
    if total==0:
        print(f"{name} point = {total} ,{partner_name} point = {total}")
        return(f"******** {name} and {partner_name} are Draw ********")
    elif total>0:
        print(f"{name}'s points = {abs(total)} ,{partner_name}'s points = -{abs(total)}")
        return(f" ******* {name} is Winner ********")
    else :
        print(f"{name}'s points = -{abs(total)} , {partner_name}'s points = {abs(total)}")
        return(f"****** {partner_name} is Winner ********")

if __name__ =="__main__":
    print(Welcoming())
    
    while True:
        x=input("do you want to play (yes or no)\n")
        if x.lower()=="yes":
            numper_player=input("if you want to play with computer enter 1 ,if you want to play with another player enter 2 \n")
            total=0
            if numper_player=="1":
                print(single_player(total))
            elif numper_player=="2":
                print(tow_player(total))
            else:
                print("you should enter 1 or 2")
                continue
        else:
            print("no")
            break
    
      
        
    
    
    
    
    
    
    
    