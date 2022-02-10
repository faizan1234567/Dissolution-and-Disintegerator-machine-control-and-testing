from tkinter import *
import datetime
import time
import os
#import ds18b20_temp_sensor
# from threading import *
# import multiprocessing
# importing strftime function to
# retrieve system's time
import RPi.GPIO as GPIO
from time import strftime
#import max6675
import threading
import multiprocessing as mp
from PIL import Image, ImageTk
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
#
    
GPIO.setwarnings(False)

ledon = 3 #old value 11

channel = 11 # old value 13

motor_on =18

counter =0

#GPIO.setup(ledon , GPIO.OUT)
GPIO.setup(ledon, GPIO.OUT)
GPIO.setup(motor_on, GPIO.OUT)

GPIO.output(motor_on,GPIO.LOW)
#GPIO.output(motor_on,GPIO.HIGH)
#GPIO.setup(32, GPIO.OUT)
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(channel, GPIO.FALLING, callback=)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

root = Tk()
main_frame = LabelFrame(root, text = 'Test setting',width=800,height=480)
main_frame.pack()
        

oscillationvalue = StringVar()
test_type = StringVar()       

hh = StringVar()
mm = StringVar()


# frameoscillation = LabelFrame(main_frame,bg='light green',text='set oscillation',width=400,height=100)

img =Image.open("/home/pi/python programs/disoultion/images/oscillationFrame.jpg")
#img = img.resize((400, 100), Image.ANTIALIAS)
#img = ImageTk.PhotoImage(image.open(stim))
render = ImageTk.PhotoImage(img)



frameoscillation = LabelFrame(main_frame,text='Set Oscillation',bg='light blue',width=400,height=100)
frameoscillation.place(x=200,y=20)

lblimg = Label(frameoscillation,image=render,width=400,height=100)
lblimg.pack()
#frametime = LabelFrame(main_frame,bg='light blue',text='set time',width=400,height=100)
frametime = LabelFrame(main_frame, text = 'Set Time',bg='light blue',width=400,height=100)
frametime.place(x=200,y=140)

frametemperature = LabelFrame(main_frame,text= 'Set Temperature',bg='light blue',width=400,height=100)
frametemperature.place(x=200,y=260)

lbl = Label(frameoscillation,text="Oscillations :")
lbl['bg'] = frameoscillation['bg']
lbl.place(x=20,y=40)
        
oscillationEntry = Entry(frameoscillation,width=5,textvariable=oscillationvalue,justify='center')
oscillationEntry['bg'] =frameoscillation['bg']
oscillationEntry.place(x=120,y=40)
oscillationEntry.insert(0,'0')

lblcounter = Label(frameoscillation,text="0")
lblcounter['bg']=frameoscillation['bg']
lblcounter.place(x=200,y=40)


#------------- time frame
lbltimer = Label(frametime,text="Time : ")
lbltimer['bg'] = frametime['bg']
lbltimer.place(x=10,y=30)

#         hourEntry = Entry(main_frame,width=5 , textvariable=self.hh, validatecommand=self.callback_hour)

hourlabel = Label(frametime,text="hh")
hourlabel['bg'] = frametime['bg']
hourlabel.place(x=120,y=10)

hourEntry = Entry(frametime,width=5 , textvariable=hh ,justify='center')
hourEntry.place(x=105,y=30)
hourEntry.insert(0,0)

minutelabel = Label(frametime,text="mm" )
minutelabel['bg'] = frametime['bg']
minutelabel.place(x=180,y=10)

minuteEntry = Entry(frametime,width=5,textvariable=mm ,justify='center')
minuteEntry.place(x=170,y=30)
minuteEntry.insert(0,0)

totaltimelabel = Label(frametime,text="Total time in seconds : ")
totaltimelabel['bg'] = frametime['bg']
totaltimelabel.place(x=240,y=30)

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

# def read(ds18b20):
#     location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
#     tfile = open(location)
#     text = tfile.read()
#     tfile.close()
#     secondline = text.split("\n")[1]
#     temperaturedata = secondline.split(" ")[9]
#     temperature = float(temperaturedata[2:])
#     celsius = temperature / 1000
#     farenheit = (celsius * 1.8) + 32
#     return celsius, farenheit

def set_test_type(value):
    if value=='oscillation':
        print('oscillation option selected')
        
#         frametime.visible=False
#         frameoscillation.visible=True
        #frametime.pack_forget()
        #frameoscillation.show()

    elif value =='time':
        print('time option selected')
        #frametime.visible=True
        #frameoscillation.visible=False
        
r1=Radiobutton(main_frame, text='Set Oscillation', value='oscillation', variable = test_type , command=lambda:set_test_type(test_type.get()))
r1.place(x=10,y=50)

r2=Radiobutton(main_frame, text='Set Time', value='time', variable = test_type , command=lambda:set_test_type(test_type.get()))
r2.place(x=10,y=80)

test_type.set('oscillation')
def countdown(time_sec):
    print('counterdown function called')
    print(time_sec)
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = '{:02d} : {:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        totaltimelabel.config(text=timeformat)
        time.sleep(1)
        time_sec-=1
    print('stop counter, test completed')
def mycounter():
    global counter
    
    osvalue =oscillationvalue.get()
    #print('oscillation vlaue: {}'.format(osvalue))
    
    #print(hh.get())
    if hh.get() != "":
        h =int(hh.get()) * 3600
    else:
        h=0
    if mm.get() != "":    
        m =int(mm.get()) * 60
    else:
        m = 0
    totaltime = h + m
    #countdown(totaltime)
    if int(osvalue) > 0:
        #print('oscillation value is greater than zero')
        if int(counter) < int(osvalue): 
            print("2. mycounter function starting by oscillation...")
            
            input_state = GPIO.input(channel) #Read and store value of input to a variable
            print("3. Input State Value is "+ str(input_state))
            if input_state == True:     #Check whether pin is grounded
                #print('Button Pressed')   #Print 'Button Pressed'
                #time.sleep(0.1)           #Delay of 0.3s
        #             self.counter +=1
        #             print(self.counter)
                counter +=1
                lblcounter.config(text=str(counter)) 
                print('4. mycounter increamented. ' + str(counter))
            else:
                print('5. no value added..')
            print("6. mycounter function end.\n")
        else:
            print("Test completed.")
    elif totaltime > 0:
        print("2. mycounter function starting by time...")
            
        input_state = GPIO.input(channel) #Read and store value of input to a variable
        print("3. Input State Value is "+ str(input_state))
        if input_state == True:     #Check whether pin is grounded
            #print('Button Pressed')   #Print 'Button Pressed'
            #time.sleep(0.1)           #Delay of 0.3s
    #             self.counter +=1
    #             print(self.counter)
            counter +=1
            lblcounter.config(text=str(counter)) 
            print('4. mycounter increamented. ' + str(counter))
        else:
            print('5. no value added..')
        print("6. mycounter function end.\n")
    else:
        print('set oscillation value or set time must be greater than zero')
    
GPIO.remove_event_detect(channel)
GPIO.add_event_detect(channel, GPIO.RISING, callback=lambda x:mycounter(),bouncetime=500)

class SpindleSettingForm: 
    def __init__(self, root, sen_num):
        self.root = root
        self.sen_num = sen_num
        self.root.geometry("1000x550+0+0")
        self.root.title("Disintegration")
        
#         self.cs = 23 #chip select old value 7, cable color Green
#         self.sck = 21 # data out (DO) old value 22 blue
#         self.so = 22 #clock old value 18 color yellow
#         
        self.counter=0
        
        #self.oscillationvalue = StringVar()
        # max6675.set_pin(CS, SCK, SO, unit)   [unit : 0 - raw, 1 - Celsius, 2 - Fahrenheit]
#         max6675.set_pin(self.cs, self.sck, self.so, 1)
        
#         lbl = Label(main_frame,text="Oscillations :")
#         lbl.place(x=50,y=80)
              
        
        #GPIO.setmode(GPIO.BCM)
        # GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
        #

        GPIO.setwarnings(False)
        
        #GPIO.output(32,GPIO.HIGH)
        GPIO.output(motor_on,GPIO.LOW)
        label_font = font.Font(family = "Helvetica", 
                                         size = 12, 
                                         weight = "bold")
        
        lbltemperature = Label(frametemperature,text="Range Limit (0-50)",fg='blue',font=label_font)
        #frametemperature.wm_attributes("-transparentcolor", 'grey')
        #lbltemperature.attributes('-alpha',0.5)
        #topFrame['bg'] = topFrame.master['bg']
        lbltemperature['bg'] = frametemperature['bg']
        
        lbltemperature.place(x=20,y=10)
        
        Desired_font = font.Font( family = "Helvetica", 
                                         size = 24, 
                                         weight = "bold")
        self.temperatureEntry = Entry(frametemperature,width=5,font=Desired_font)
        self.temperatureEntry.place(x=40,y=30)
        self.temperatureEntry.configure(justify='center')
        self.temperatureEntry.insert(0,"30")
        
        
        lbltolerance = Label(frametemperature,text="Tolerance (+/-)",fg='blue',font=label_font)
        lbltolerance['bg'] = frametemperature['bg']
        lbltolerance.place(x=170,y=10)
        
        toleranceEntry = Entry(frametemperature,width=5,font=Desired_font,justify='center')
        toleranceEntry.place(x=175,y=30)
        toleranceEntry.insert(0,"2")
        
        
        lblcurrentvalue = Label(frametemperature,text="Current Value",fg='blue',font=label_font)
        lblcurrentvalue['bg'] = frametemperature['bg']
        lblcurrentvalue.place(x=290,y=10)
        
        self.currentValueEntry = Entry(frametemperature,width=5,font=Desired_font,justify='center')
        self.currentValueEntry.place(x=300,y=30)
        #currentValueEntry.insert(0,"40")        
        # Create an object of type Font from tkinter.
        Desired_font = font.Font( family = "Helvetica", 
                                         size = 24, 
                                         weight = "bold")
        self.lblcurrentTime=Label(main_frame,font=Desired_font,bg="black",fg="yellow")
        #self.lblcurrentTime.place(x=10,y=10)
        #self.Threading()
        self.currentTemp =0.0
        self.setValue=0.0
        #self.motor = mp.Process(target=self.startTest)
        #motorbutton = Button(main_frame,bg='green',text="Start Motor",width=20,height=5,command=threading.Thread(target= self.startTest).start())
        #motorbutton = Button(main_frame,bg='green',text="Start Test",width=15,height=5,command=threading.Thread(target=self.startTest,args=()))
        motorbutton = Button(main_frame,bg='green',text="Start Test",width=15,height=5,command=self.startTest)        
        motorbutton.place(x=5,y=260)
        
        #self.showtime()
        #self.p1 = threading.Thread(target=self.showtime)
        self.p1 = mp.Process(target=self.showtime)
        
#         input_state = GPIO.input(channel)
#         if input_state == True:
#             GPIO.add_event_detect(channel, GPIO.BOTH, callback=mycounter())
        
#     def callback_hour(self):
#         print(self.hh)
    def message(self):
        print("counter function called")
    def motoron(self):
            
        print("Test started")
        starttime= time.perf_counter()
        
        #print(starttime)
        GPIO.output(motor_on,GPIO.HIGH)
        #GPIO.output(motor_on,GPIO.LOW)
        
        #print('Hours ' , self.hh.get())
        #print('minutes ', self.mm.get())
        print('Hours ' , hh.get())
        print('minutes ', mm.get())
        h =int(hh.get())*3600
        m =int(mm.get())*60
        totaltime = h + m
        
        #countdown(totaltime)
#         print('motor on for seconds ',totaltime)
#         totaltimelabel.config(text ='motor on for '+ str(totaltime) + ' seconds' )
        
        #time.sleep(totaltime)
        while totaltime:
            mins,secs = divmod(totaltime,60)
            timeformat='{:02d} : {:02d}'.format(mins,secs)
            totaltimelabel.config(text=timeformat)
            time.sleep(1)
            totaltime-=1
        
        GPIO.output(motor_on,GPIO.LOW)
        #GPIO.output(motor_on,GPIO.HIGH)    
        endtime= time.perf_counter()
        duration = endtime - starttime
        print("Total Duration : " + str(format(duration,'.2f')))
        totaltimelabel.config(text ='Test Completed.')
        print('Total Oscillation ' + str(counter))
        print("Test completed.")

    def startTest(self):
        global counter
        lblcounter.config(text=str(0))
        
        counter = 0
        h =int(hh.get())*3600
        m =int(mm.get())*60
        totaltime = h + m
        print('Test started for seconds ',totaltime)
        
        totaltimelabel.config(text ='Test started for '+ str(totaltime) + ' seconds' )
        if totaltime > 0:
            #m = mp.Process(target=self.motoron)
            #m.start()
            #m.join()
            #m.run()
            m = threading.Thread(target=self.motoron)
            m.start()
    
            
            #c = threading.Thread(target=countdown,args=(totaltime, ))
            #c.start()
#             
            #m.join()
            #c.join()
            #m.join()
#     def read(ds18b20):
#         
#         location = '/sys/bus/w1/devices/'+ds18b20+'/w1_slave'
#         tfile = open(location)
#         text = tfile.read()
#         tfile.close()
#         secondline = text.split("\n")[1]
#         temperaturedata = secondline.split(" ")[9]
#         temperature = float(temperaturedata[2:])
#         celsius = temperature / 1000
#         farenheit = (celsius * 1.8) + 32
#         return celsius, farenheit
#     
#     def loop(self.sen_num):
#         while True:
#             if read(self.sen_num) != None:
#                 return read(ds18b20)[0]
        


    def showtime(self):
        def mytime():
            try:
                def read(ds18b20):
        
                    location = '/sys/bus/w1/devices/'+ds18b20+'/w1_slave'
                    tfile = open(location)
                    text = tfile.read()
                    tfile.close()
                    secondline = text.split("\n")[1]
                    temperaturedata = secondline.split(" ")[9]
                    temperature = float(temperaturedata[2:])
                    celsius = temperature / 1000
                    farenheit = (celsius * 1.8) + 32
                    return celsius, farenheit
                string = strftime('%H:%M:%S %p')
          
                self.lblcurrentTime.place(x=0,y=0)
                self.lblcurrentTime.config(text = string)
                #time.sleep(1000)
                #self.lblcurrentTime.after(1000, time)
                #self.lblcurrentTime.after(1000, self.showtime)
                self.lblcurrentTime.after(1000, mytime)
                #self.currentTemp = read(self.sen_num)[0]
                self.currentTemp =read(self.sen_num)[0]
                #print(self.currentTemp)
#                 print('i am working')
                #print(self.sen_num)
#               print 
#                 
#                 
                
                
                #self.currentTemp = max6675.read_temp(self.cs)
                

                # print temperature
                #print (self.currentTemp)

                # when there are some errors with sensor, it return "-" sign and CS pin number
                # in this case it returns "-22" 
                self.currentValueEntry.delete(0,END)
                self.currentValueEntry.insert(0,format(self.currentTemp, '.2f')  )
                
                self.setValue =round( float(self.temperatureEntry.get()),2)
                
                #print("Set Value is " + setValue + "current temp " + currentTemp)         
                
                #GPIO.setup(ledon, GPIO.OUT)
                
                if self.setValue > float(self.currentTemp):
                    #print ("Set Value is greater then Current Value")
                    GPIO.output(ledon,GPIO.HIGH)
                    
                    #GPIO.output(pulsecounter,GPIO.HIGH)
                    
                    #self.pulsecounter +=1
                    
                else:
                    #print("Current Value is greater than set value")
                    GPIO.output(ledon,GPIO.LOW)
                                
            except:
                #print(sys.exc_info()[0])
                print('passing')
        
#         input_state = GPIO.input(channel)
#         if input_state==True:
#             #self.mycounter()
#             #self.p2 = mp.Process(target=self.mycounter)
#             self.p2.run()
        mytime()
        
#         input_state = GPIO.input(channel)
#         if input_state == True:
#             GPIO.add_event_detect(channel, GPIO.BOTH, callback=mycounter())
#         input_state = GPIO.input(channel) #Read and store value of input to a variable
#         if input_state == False:     #Check whether pin is grounded
#             print('Button Pressed')   #Print 'Button Pressed'
#             time.sleep(0.3)           #Delay of 0.3s
#             self.counter +=1
#             print(self.counter)


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
    serialNum = sensor()
          #print('serial number: {}'.format(serialNum))
    obj = SpindleSettingForm(root, serialNum)
          
          #obj.p1.start()
    obj.p1.run()
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
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=lambda x:mycounter(),bouncetime=200)
    root.mainloop()
    GPIO.output(ledon,GPIO.LOW)
    GPIO.cleanup()

