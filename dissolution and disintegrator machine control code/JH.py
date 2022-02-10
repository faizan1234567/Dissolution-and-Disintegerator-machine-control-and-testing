from tkinter import *

#import ds18b20_temp_sensor
# from threading import *
# import multiprocessing
# importing strftime function to
# retrieve system's time

from time import strftime
#import max6675

from PIL import Image, ImageTk

#GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
#
    


#GPIO.setup(ledon , GPIO.OUT)

#GPIO.output(motor_on,GPIO.HIGH)
#GPIO.setup(32, GPIO.OUT)
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(channel, GPIO.FALLING, callback=)


root = Tk()
main_frame = LabelFrame(root, text = 'Test setting',width=800,height=480)
main_frame.pack()
oscillationvalue = StringVar()
test_type = StringVar()       

hh = StringVar()
mm = StringVar()

img = Image.open("/home/pi/python programs/disoultion/images/oscillationFrame.jpg")
render = ImageTk.PhotoImage(img)

oscillationframe = LabelFrame(main_frame, text = 'Set oscillations', bg = 'light blue', width =400, height = 100)
oscillationframe.place(x=200,y=20)


lblimg = Label(oscillationframe,image=render,width=400,height=100)
lblimg.pack()


timeframe = LabelFrame(main_frame, text = 'Set Time', bg = 'light blue', width = 400, height =100)
timeframe.place(x=200, y = 160)


temperatureframe = LabelFrame(main_frame, tex = 'Set Temperature', bg = 'light blue', width = 400, height = 100)
temperatureframe.place(x=200, y = 280)


lbl = Label(oscillationframe, text = 'Oscillations', bg = 'light blue')
lbl.place(x=20, y=40)















if __name__ == "__main__":
    
  #try:
#       root = Tk()
#     obj = SpindleSettingForm(root)
#     
#     p=multiprocessing.Process(target = obj.run)
#     p.start()
#       input_state = GPIO.input(channel)
#       if input_state == True:
#           GPIO.add_event_detect(13, GPIO.BOTH, callback=mycounter())
    
    #       obj.p2.run()
          #obj.p1.join()
          
    #       input_state = GPIO.input(channel)
    #       if input_state==True:
    #         #self.mycounter()
    #           
    #           obj.p2.run()
          
          #obj.p1.join()
        #p=multiprocessing.Process(target = obj.run)
        #p.start()
        #self.Threading()
        #showtime()
        
    #       serialNum = sensor()
    #       loop(serialNum)
    root.mainloop()
    