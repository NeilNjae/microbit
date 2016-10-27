from microbit import *
import radio

A_IMAGE = Image('09909:'
                '90090:'
                '99990:'
                '90090:'
                '90090')

B_IMAGE = Image('99909:'
                '90090:'
                '99900:'
                '90090:'
                '99900')

C_IMAGE = Image('00009:'
                '09990:'
                '90000:'
                '90000:'
                '09990')

D_IMAGE = Image('00009:'
                '00009:'
                '09999:'
                '90009:'
                '09999')

images = {'a': A_IMAGE, 'b': B_IMAGE, 'c': C_IMAGE, 'd': D_IMAGE}

display.scroll('Press', wait=False, loop=True)
last_message_time = None

radio.on()

def send(message):
        radio.send(message)
        return running_time()

while True:
    message = radio.receive()    
    if message:
        last_message_time = running_time()
        if message in images:
            display_image = images[message]

    if button_a.was_pressed():
        display_image = A_IMAGE
        last_message_time = send('a')
    if button_b.was_pressed():
        display_image = B_IMAGE
        last_message_time = send('b')

    if last_message_time:
        dimness = (running_time() - last_message_time) / 500
        if dimness > 9: dimness = 9
        display.show(display_image / dimness , wait=False)
        