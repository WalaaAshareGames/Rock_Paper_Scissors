
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


#code when we have single player
def single_player(total):
    name=input("Enter your name  \U0001F929	 \n")
    i=0
    while i<3:
   
        char=input(" Enter your char (R:Rock \U0000270A ,P:Paper \U0001F91A ,S:Scissors \U0000270C	)\n")
        if char.upper()!="R" and char.upper()!="P" and char.upper()!="S":
            return("you should add from this characters (R,S,P)")
        total+=game1.result(char.upper())
        # print(total)
        i +=1
    if total==0:
        print(f"total point = {total}")
        return("****  \U0001F643 \U0001F605	   Draw  \U0001F643 \U0001F605   ****")
    elif total>0:
        print(f"total point = {total}")
        return(f"\U0001F973  \U0001F973  \U0001F973  \U0001F973  {name} is Winner    \U0001F973  \U0001F973 \U0001F973 \U0001F973")
    else :
        print(f"total point = {total}")
        return(f"*****\U0001F61E \N{loudly crying face}   {name} you lost \U0001F61E \N{loudly crying face}*******")

#code when we have two player
def tow_player(total):
    name=input(" \U00002764 \U00002764 Enter player 1 name \U00002764 \U00002764 \n ")
    partner_name=input(" \U0001F9E1 \U0001F9E1 Enter player 2 name \U0001F9E1 \U0001F9E1 \n ")
    i=0
    while i<3:
   
        char1=input(f" {name} char (R:Rock \U0000270A ,P:Paper \U0001F91A ,S:Scissors \U0000270C	)\n  ")
        char2=input(f" {partner_name}  char (R:Rock \U0000270A ,P:Paper \U0001F91A ,S:Scissors \U0000270C	)\n")
        if char1.upper() not in ["R","S","P"]  or char2.upper() not in ["R","S","P"] : 
            return(" you should add from this characters (R,S,P)  \U0001F644 \U0001F644 \U0001F644	      ")
        total+=game1.result2(char1.upper(),char2.upper())  
        # print(total)
        i +=1
    if total==0:
        print(f"{name} point = {total} ,{partner_name} point = {total}")
        return(f" \U0001F643 \U0001F605 {name} and {partner_name} are Draw  \U0001F643 \U0001F605")
    elif total>0:
        print(f"{name}'s points = {abs(total)} ,{partner_name}'s points = -{abs(total)}")
        return(f" \U0001F973 \U0001F973 \U0001F973 \U0001F973  {name} is Winner \U0001F973 \U0001F973 \U0001F973 \U0001F973")
    else :
        print(f"{name}'s points = -{abs(total)} , {partner_name}'s points = {abs(total)}")
        return(f"\U0001F973  \U0001F973 \U0001F973 \U0001F973  {partner_name} is Winner  \U0001F973  \U0001F973 \U0001F973 \U0001F973")


if __name__ =="__main__":
    print(Welcoming())
    while True:
        x=input("\n  Do you want to play (yes or no) ? \U0001F601 \U0001F606	    \n")
        if x.lower()=="yes":
            numper_player=input(" ### If you want to play with computer enter 1 ,If you want to play with another player enter 2 ###  \n")
            total=0
            if numper_player=="1":
                print(single_player(total))
            elif numper_player=="2":
                print(tow_player(total))
            else:
                print(" You should enter 1 or 2  \U0001F9D0	  ")
                continue
        else:
            break

