import st7789py as st7789
from machine import Pin, SPI
import time
import fancy_font as ff
import config

spi = SPI(1, baudrate=40000000, polarity=1, phase=1, sck=Pin(config.SCK), mosi=Pin(config.MOSI))
tft = st7789.ST7789(spi, 170, 320, reset=Pin(config.RESET), dc=Pin(config.DC), cs=Pin(config.CS), rotation=3)

tft.init()
tft.fill(st7789.BLACK)
tft.text(ff.font, "HELLO WORLD!", 20, 60, st7789.RED)
tft.text(ff.font, "MicroPython Rocks!", 20, 100, st7789.GREEN)
tft.text(ff.font, "LilyGo T-Embed", 20, 140, st7789.YELLOW)

while True:
    time.sleep(1)