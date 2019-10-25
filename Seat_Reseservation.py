book=True
makebooking=False
changebooking=False

def drawscreen():#draws the screen out
    text_file=open('seatRes.txt','r+')
    print (text_file.read())
    text_file.close()

def bookseat(seat,row,letter):#books the seat
    text_file=open('seatRes.txt','r+')
    seekpos=((row-1)*8)+(seat+(row-1))
    text_file.seek(seekpos-1)
    text_file.write(letter)
    
def checkseat(seat,row):#checks to see if the seat is available
    text_file=open('seatRes.txt','r+')
    seekpos=((row-1)*8)+(seat+(row-1))
    text_file.seek(seekpos-1)
    check=text_file.read(1)
    if check=='N'or check=='B':
        print ("you cannot book a seat here")
        text_file.close()
    else:
        text_file.close()
        bookseat(seat,row,'B')
        drawscreen()

def makeabooking(makebooking,changebooking):#makes a booking 
    while makebooking==True:
        print ("which seat would you like to book?")
        row=int(input("Which row?"))#asks user the seat
        seat=int(input("Which seat?"))
        checkseat(seat,row)#checks to see if the seat is available
        checkAgain=input("Perform another task? Y or N")#checks to perform another task
        if checkAgain=="Y" or checkAgain=='y':
            makebooking=False
        else:
            makebooking=False
            changebooking=False
            book=False

def changeabooking(makebooking,changebooking):
    while changebooking==True:
        print ("Which seat would you like to change?")#asks the seat to change
        row=int(input("Which row?"))#asks user the seat
        seat=int(input("Which seat?"))
        bookseat(seat,row,'0')
        drawscreen()
        checkAgain=input("Perform another task? Y or N")#checks to perform another task
        if checkAgain=="Y" or checkAgain=='y':
            changebooking=False
        else:
            makebooking=False
            changebooking=False
            book=False


print ("Welcome to the cinema booking system\nPlease see the layout below\n")
drawscreen()

while book==True:
    mode=input("Press 1 make a booking, Press 2 to change a booking, any other key to exit\n")
    if mode=='1':
        makebooking=True
        changebooking=False
        makeabooking(makebooking,changebooking)
    elif mode=='2':
        changebooking=True
        makebooking=False
        changeabooking(makebooking,changebooking)
    else:
        makebooking=False
        changebooking=False
        book=False
drawscreen()
