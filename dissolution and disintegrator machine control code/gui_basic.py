from tkinter import *

root = TK()
#creating a label widget
myLabel = Label(root, text = 'hello world')
#shoving it onto the screen
myLabel.pack()

oscillationvalue = StringVar()
test_type = StringVar()       

hh = StringVar()
mm = StringVar()

if __name__ == '__main__':
    
    
    root.mainloop()
