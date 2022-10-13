import random



class game :
    def __init__(self):
        self.player=0

    def set_player(self,n):
        self.player=n

    def get_player(self):
        return self.player

    def game (self,char):
        count=0
        if self.get_player()==1:
            list=['R','S','P']
            number= random.randint(0,2)
            v=list[number]
            print (v)
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
            return count
                
                
                



        

    
    



#test1
g1=game()
g1.set_player(1)
print(g1.get_player())

#test2
print(g1.game('R'))
