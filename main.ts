let moisture = 0
let first_digit = 0
basic.forever(function () {
    moisture = pins.analogReadPin(AnalogPin.P1)
    serial.writeNumber(moisture)
    if (moisture < 400) {
        serial.writeString("too low")
    } else {
        serial.writeString("ok")
    }
    serial.writeString("" + ("\n"))
    first_digit = Math.floor(moisture / 100)
    basic.showNumber(first_digit)
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(5000)
})
