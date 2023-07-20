import board
import time
import busio
import displayio
import terminalio
import neopixel
from adafruit_display_text import label
from adafruit_st7789 import ST7789

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

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)


# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)


while True:
    pixels[0] = RED
    time.sleep(0.5)
    pixels[0] = GREEN
    time.sleep(0.5)
