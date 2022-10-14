import random

class Game :
    def __init__(self):
        self.player=1


    def set_player(self,n):
        self.player=n

    def get_player(self):
        return self.player


    def __str__ (self):
        return 'you are in Rock paper scissors game'
    def __repr__(self) :
        rep= self.__class__.__name__
        return rep 


    def random(self):
        list=['R','S','P']
        number= random.randint(0,2)
        v=list[number]
        return v

    def result (self,char):
        count=0     
        v=self.random()
        print (f"you threw '{char}' and the computer threw '{v}'")       
        if (v=="R"):
            if(char=="R"):
                count=0
            elif(char == "P"):
                count+=10
            elif (char == "S"):
                count-=10
        elif (v=="P"):
            if(char=="R"):
                count-=10
            elif(char == "P"):
                count=0
            elif (char == "S"):
                count+=10
        if (v=="S"):
            if(char=="R"):
                count+=10
            elif(char == "P"):
                count-=10
            elif (char == "S"):
                count=0
        print(f"you get {count}")
        return count
        
    def result2 (self,char1,char2):
        count1=0

        #count2=0 

        count2=0 

        if char1==char2:
            count1+=0
        if (char1=="S"):
            if(char2=="R"):
                count1-=10
            elif(char2 == "P"):
                count1+=10
        if (char1=="P"):
            if(char2=="R"):
                count1+=10
            elif(char2 == "S"):
                count1-=10
        if (char1=="R"):
            if(char2=="P"):
                count1-=10
            elif(char2 == "S"):
                count1+=10
        print (f"player 1 threw '{char1}' and the player 2 threw '{char2}'")
        return count1
          

game1 =Game()   

game1 =Game()   


if __name__ =="__main__" :
    #test1
    g1=Game()
    g1.set_player(1)
    print(g1.get_player())
    
    #test2
    print(g1.result('R'))
    