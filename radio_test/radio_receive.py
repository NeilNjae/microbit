from microbit import *
import radio

A_IMAGE = Image('00009:'
                '09990:'
                '90090:'
                '90090:'
                '09999')

B_IMAGE = Image('90009:'
                '90000:'
                '99900:'
                '90090:'
                '99900')

radio.on()

display.scroll('Ready', wait=False, loop=True)
last_receive_time = None
display_image = None

while True:
    message = radio.receive()
    if message:
        last_receive_time = running_time()
        if message == 'a':
            display_image = A_IMAGE
        if message == 'b':
            display_image = B_IMAGE
    elif last_receive_time:
        dimness = (running_time() - last_receive_time) / 500
        if dimness > 9: dimness = 9
        display.show(display_image / dimness , wait=False)
