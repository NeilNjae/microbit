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

display.scroll('Press', wait=False, loop=True)
last_sent_time = None

while True:
    if button_a.was_pressed():
        display_image = A_IMAGE
        last_sent_time = running_time()
        radio.on()
        radio.send('a')
        radio.off()
    if button_b.was_pressed():
        display_image = B_IMAGE
        last_sent_time = running_time()
        radio.on()
        radio.send('b')
        radio.off()
    if last_sent_time:
        dimness = (running_time() - last_sent_time) / 500
        if dimness > 9: dimness = 9
        display.show(display_image / dimness, wait=False)
        