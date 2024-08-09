from microbit import *
moisture = 0

def on_forever():
    global moisture
    moisture = pins.analog_read_pin(AnalogPin.P1)
    serial.write_number(moisture)
    serial.write_string("\n")
    first_digit = (int)moisture / 100
    display.show_number(first_digit)
    basic.pause(200)
basic.forever(on_forever)
