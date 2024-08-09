moisture = 0
first_digit = 0

def on_forever():
    global moisture, first_digit
    moisture = pins.analog_read_pin(AnalogPin.P1)
    serial.write_number(moisture)
    if moisture < 400:
        serial.write_string("too low")
    else:
        serial.write_string("ok")
    serial.write_string("" + ("\n"))
    first_digit = Math.floor(moisture / 100)
    basic.show_number(first_digit)
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(5000)
basic.forever(on_forever)
