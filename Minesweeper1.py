# Minesweeper

# Import libraries
import tkinter
import random

# Define global variables
gameOver = False
score = 0
squaresToClear = 0
size = int(input('Enter the size of your minefield: '))

def play_minefield():
    """ function to call the game """
    create_minefield(minefield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()

minefield = []

def create_minefield(minefield):
    """ generate a random minefield """
    global squaresToClear

    for row in range(0,size):
        rowList = []
        for column in range(0,size):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
        minefield.append(rowList)
        
    #printfield(minefield)

def printfield(minefield):
    """ print row list in minefield """
    for rowList in minefield:
        print(rowList)


def layout_window(window):
    """ set up the GUI window """
    for rowNumber, rowList in enumerate(minefield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg= "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg= "lightgrey")
            else:
                square = tkinter.Label(window, text = "    ", bg= "green")
            square.grid(row = rowNumber, column = columnNumber, ipadx = 7, ipady = 7)
            square.bind("<Button-1>", on_click)


def on_click(event):
    """ left mouse click control """
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if minefield[row][column] == 1:
            gameOver = True
            square.config(bg = "red")
            print("Game Over! You hit a mine!")
            print("Your score was: ", score)
        elif currentText == "    ":
            square.config(bg = "yellow")
            totalmines = 0
 
            if row < size-1:
                if minefield[row+1][column] == 1:
                    totalmines = totalmines + 1
            
            if row > 0:
                if minefield[row-1][column] == 1:
                    totalmines = totalmines + 1
            
            if column > 0:
                if minefield[row][column-1] == 1:
                    totalmines = totalmines + 1
             
            if column < size-1:
                if minefield[row][column+1] == 1:
                    totalmines = totalmines + 1
             
            if row > 0 and column > 0:
                if minefield[row-1][column-1] == 1:
                    totalmines = totalmines +1
             
            if row < size-1 and column > 0:
                if minefield[row+1][column-1] == 1:
                    totalmines = totalmines + 1
              
            if row > 0 and column < size-1:
                if minefield[row-1][column+1] == 1:
                    totalmines = totalmines + 1
            
            if row < size-1 and column < size-1:
                if minefield[row+1][column+1] == 1:
                    totalmines = totalmines + 1


            square.config(text = " " + str(totalmines) + " ")
            squaresToClear = squaresToClear -1
            score = score +1
            if squaresToClear ==0:
                gameOver = True
                print("Well done! You found all the safe squares!")
                print("Your score was:", score)

# Call the game function
play_minefield()                
                   
           
        
            
                
            


