from random import randint
import Users
import time
class MineSweeper:
    boardB = [[]];
    boardD = [[]];
    size = 0;
    def __init__(self, size1):
        self.boardB = [["x" for p in range(size1)] for p in range(size1)]; #B for Bomb
        self.boardD = [["x" for p in range(size1)] for p in range(size1)]; #D for Display
        self.size = size1; 
        
    def printboardD(self):
            for i in range(len(self.boardD)):
                for j in range(len(self.boardD)):
                    print(self.boardD[i][j], end=" ");
                print();
    def printboardB(self):
            for i in range(len(self.boardB)):
                for j in range(len(self.boardB)):
                    print(self.boardB[i][j], end=" ");
                print();

    def setboardB(self, numB):
        randomRow = randint(0,len(self.boardB)-1);
        randomCol = randint(0,len(self.boardB)-1);
        i=0;
        while(i<numB):
            while(self.boardB[randomRow][randomCol]!="x"):
                randomRow = randint(0,len(self.boardB)-1);
                randomCol = randint(0,len(self.boardB)-1);
            self.boardB[randomRow][randomCol]="B";
            i=i+1;                  
    
    def multiUser(self, input,command):
        if(command == "count"):
            numB = 0;
            if(Users.inbounds(input[0]-1,input[1]-1, self.boardB) and self.boardB[input[0]-1][input[1]-1] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0]-1,input[1], self.boardB) and self.boardB[input[0]-1][input[1]] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0]-1,input[1]+1, self.boardB) and self.boardB[input[0]-1][input[1]+1] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0],input[1]+1, self.boardB) and self.boardB[input[0]][input[1]+1] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0]+1,input[1]+1, self.boardB) and self.boardB[input[0]+1][input[1]+1] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0]+1,input[1], self.boardB) and self.boardB[input[0]+1][input[1]] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0]+1,input[1]-1, self.boardB) and self.boardB[input[0]+1][input[1]-1] == "B"):
                numB=numB+1;
            if(Users.inbounds(input[0],input[1]-1, self.boardB) and self.boardB[input[0]][input[1]-1] == "B"):
                numB=numB+1;
            return numB;
        
        elif(command == "change"):
            if(Users.inbounds(input[0]-1,input[1]-1, self.boardB) and self.multiUser([input[0]-1, input[1]-1, input[2]], "count") == 0):
                self.boardB[input[0]-1][input[1]-1] = "_";
                self.boardD[input[0]-1][input[1]-1] = "_";
            if(Users.inbounds(input[0]-1,input[1], self.boardB) and self.multiUser([input[0]-1,input[1],input[2]],"count") == 0):
                self.boardB[input[0]-1][input[1]] = "_";
                self.boardD[input[0]-1][input[1]] = "_";
            if(Users.inbounds(input[0]-1,input[1]+1, self.boardB) and self.multiUser([input[0]-1,input[1]+1,input[2]], "count") ==0):
                self.boardB[input[0]-1][input[1]+1] = "_";
                self.boardD[input[0]-1][input[1]+1] = "_";
            if(Users.inbounds(input[0],input[1]+1, self.boardB) and self.multiUser([input[0],input[1]+1,input[2]], "count") == 0):
                self.boardB[input[0]][input[1]+1] = "_";
                self.boardD[input[0]][input[1]+1] = "_";
            if(Users.inbounds(input[0]+1,input[1]+1, self.boardB) and self.multiUser([input[0]+1,input[1]+1,input[2]], "count") == 0):
                self.boardB[input[0]+1][input[1]+1] = "_";
                self.boardD[input[0]+1][input[1]+1] = "_";
            if(Users.inbounds(input[0]+1,input[1], self.boardB) and self.multiUser([input[0]+1,input[1],input[2]],"count") == 0):
                self.boardB[input[0]+1][input[1]] = "_";
                self.boardD[input[0]+1][input[1]] = "_";
            if(Users.inbounds(input[0]+1,input[1]-1, self.boardB) and self.multiUser([input[0]+1,input[1]-1,input[2]],"count") == 0):
                self.boardB[input[0]+1][input[1]-1] = "_";
                self.boardD[input[0]+1][input[1]-1] = "_";
            if(Users.inbounds(input[0],input[1]-1, self.boardB) and self.multiUser([input[0],input[1]-1,input[2]],"count")==0):
                self.boardB[input[0]][input[1]-1] = "_";
                self.boardD[input[0]][input[1]-1] = "_";
            
        
    def updateBoards(self, input,blocks):
        if(input[2]=="o"):
            if(self.boardB[input[0]][input[1]] == "B"):
                self.boardB[input[0]][input[1]] = "X";
                self.printboardB();
                print("KABOOM - You Lose.");
                return False;
            else:

                if(self.multiUser(input, "count")==0):
                    self.boardB[input[0]][input[1]] = "_";
                    self.boardD[input[0]][input[1]] = "_";
                    self.multiUser(input, "change");
                    self.printboardD();
                else:
                    self.boardB[input[0]][input[1]] = str(self.multiUser(input, "count"));
                    self.boardD[input[0]][input[1]] = str(self.multiUser(input, "count"));
                    self.printboardD();
        else: 
            self.boardD[input[0]][input[1]] = input[2];
            self.printboardD();
        for i in range(len(self.boardB)):
            for j in range(len(self.boardB)):
                if(self.boardD[i][j]=="x" or self.boardD[i][j]=="?"):
                    return True;
        print("YOU WIN!");
        return False; 