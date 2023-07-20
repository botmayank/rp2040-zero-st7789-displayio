# Waveshare RP2040 Zero + Adafruit 1.14" TFT display 

## Hardware used
- Waveshare RP2040 Zero: https://www.waveshare.com/wiki/RP2040-Zero
- Adafruit 1.14" TFT + SDcard display using ST7789: https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout

## Wiring

| Display  | RP2040 Zero|  Comment  |
|----------|------------|-----------|
|  Vin     |     3V3    |   3-5V    |
|  GND     |     GND    |   Ground  |
|  SCK     |     GP2    |  SPI0 SCK |
|  MISO    |     GP0    |  SPI0 RX  |
|  MOSI    |     GP3    |  SPI0 TX  |
|  TFTCS   |     GP1    |  SPI0 CSn |
|  RST     |     GP4    |ScreenReset|
|  DC      |     GP5    |  DataCmd  |
|  SDCS    |     NC     | SDcard CS |
|  LIT     |     NC     | Backlight |


## Instructions

1. Install CircuitPython for the RP2040-Zero from here: https://circuitpython.org/board/waveshare_rp2040_zero/

https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

2. Install the Mu code editor https://codewith.mu/en/download

3. Move files onto the RP2040 over USB
It should show up as a storage device on your host machine. 
Move `code.py` to `CIRCUITPY/code.py` 
Move `libs/`  to `CIRCUITPY/libs`

4. Hit save inside the IDE and you should see Hello World! and the LED blinking red/green like this:

![Hello World Display + Neopixel](images/helloworld.gif "Hello World Display + Neopixel")


## References
1. https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout/circuitpython-displayio-quickstart

2. https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus

3. https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage#spi-initialization-3040957

4. https://docs.circuitpython.org/projects/neopixel/en/latest/api.html

