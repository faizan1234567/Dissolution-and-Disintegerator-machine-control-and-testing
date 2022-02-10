import gpiozero
button = gpiozero.Button(18)

while True:
    if button.is_pressed:
        print('button is pressed')
        
    else:
        print('no')