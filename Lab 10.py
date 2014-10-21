##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# House Outline
housebase = drawpad.create_rectangle(250,250,500,500)
roof1 = drawpad.create_line(375,125,500,250)
roof2 = drawpad.create_line(250,250,375,125)
#Windows and Door
window1 = drawpad.create_rectangle(280,300,320,350)
window2 = drawpad.create_rectangle(430,300,470,350)
door = drawpad.create_rectangle(350,400,400,500)
#Doorknob and Chimney
doorknob = drawpad.create_oval(390,440,400,450)
chimney = drawpad.create_rectangle(450,150,500,250)
#Green Grass and Fill Red
grass = drawpad.create_rectangle(0,450,800,600, fill = 'green')
redhouse = drawpad.create_rectangle(250,250,500,500, fill = 'red')
window1 = drawpad.create_rectangle(280,300,320,350, fill = 'lightblue')
window2 = drawpad.create_rectangle(430,300,470,350, fill = 'lightblue')
door = drawpad.create_rectangle(350,400,400,500, fill = 'tan')
root.mainloop()
