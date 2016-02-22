import Users
import MineSweeper 

playAgain = "y";

while(playAgain == "y"):
    try:
        size = int(input("What size board do you want? "));
        number = int(input("How many bombs? "));
        while(number >= size**2):
            number = int(input("How many bombs? "));
    except:
        continue
    newGame = MineSweeper.MineSweeper(size);
    newGame.setboardB(number);
    newGame.printboardD();
    continueGame = True; 
    while(continueGame == True):
        try:
            userInput1, userInput2, userInput3 = input("Enter co-ordinates and o/b/?: ").split(" ");
            userInput = [int(userInput1)-1, int(userInput2)-1, userInput3];
        except ValueError:
            continue
        
    
    #    print(userInput);
        while(Users.verify(userInput, newGame.boardB)==False):
            try:
                userInput1, userInput2, userInput3 = input("Re-enter co-ordinates and o/b/?: ").split(" ");
                userInput = [int(userInput1)-1, int(userInput2)-1, userInput3];
            except ValueError:
                continue
        usedBlocks = 0;
        if(newGame.updateBoards(userInput, usedBlocks) == False):
            playAgain = input("Play again? y/n: ");    
            while(playAgain != "y" and playAgain!="n"):
                playAgain = input("Play again? y/n: ");
            if(playAgain == "y"):
                continueGame = False;
            else:
                break;
