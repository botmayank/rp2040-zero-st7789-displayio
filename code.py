# SPDX-FileCopyrightText: 2023 botmayank
# SPDX-License-Identifier: MIT

"""
Display an in memory bitmap on the display
"""

import board
import time
import busio
import displayio
import terminalio
import neopixel
from adafruit_display_text import label
from adafruit_st7789 import ST7789

IMAGE_PATHS = ["images/nvidia.bmp", "images/ryzen.bmp", "images/traces.bmp"]
TIME_BETWEEN_IMAGES = 1

# Onboard neopixel LED
# Note, order is GRB not RGB for wiring
GREEN = 0x100000
RED = 0x001000
BLUE = 0x000010

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# DISPLAY settings
DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 135
DISPLAY_ROWSTART = 40
DISPLAY_COLSTART = 53
DISPLAY_ROTATION = 270

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00

SPI_CLK = board.GP2  # SPI0 clock
SPI_MOSI = board.GP3  # SPI0 TX - to drive display
SPI_MISO = board.GP0  # SPI0 RX - not needed for display, but will use for SD card
TFT_RST = board.GP4  # Reset for display
TFT_CS = board.GP1  # Chip Select for display
TFT_DC = board.GP5  # Data/Cmd for display
SPI_CLOCK_RATE = 1000000

displayio.release_displays()

spi = busio.SPI(SPI_CLK, SPI_MOSI, SPI_MISO)

display_bus = displayio.FourWire(
    spi, command=TFT_DC, chip_select=TFT_CS, reset=TFT_RST, baudrate=SPI_CLOCK_RATE
)

display = ST7789(
    display_bus,
    rotation=DISPLAY_ROTATION,
    width=DISPLAY_WIDTH,
    height=DISPLAY_HEIGHT,
    rowstart=DISPLAY_ROWSTART,
    colstart=DISPLAY_COLSTART,
)


print("Let's get this display started!")

while True:
    pixels[0] = RED
    time.sleep(0.5)
    pixels[0] = GREEN
    time.sleep(0.5)
    
    for image in IMAGE_PATHS:
        bitmap = displayio.OnDiskBitmap(image)

        # Create a TileGrid to hold the bitmap
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

        # Create a Group to hold the TileGrid
        group = displayio.Group()

        # Add the TileGrid to the Group
        group.append(tile_grid)

        # Add the Group to the Display
        display.show(group)
        
        time.sleep(TIME_BETWEEN_IMAGES)

