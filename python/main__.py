import signal
import time
from neopixel import *

# NeoPixel
LED_COUNT = 12  # Number of LED PIXELS
LED_PIN = 18  # GPIO 18 / PIN 12
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest

# FX
WAIT_MS = 40

# COLORS
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)

continue_reading = True


def end_read(signal, frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    resetLeds(ring, BLACK)
    pass


def expectsRain(ring, color, wait_ms=10):
    for t in range(0, 5, 1):
        colorWipe(ring, color, wait_ms)
        colorWipe(ring, BLACK, wait_ms)

    # breathing(ring, color, wait_ms)


# ColorFX's
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def stroboscopeEffect(strip, color, wait_ms=50, iterations=10):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


# def breathing(strip, color, wait_ms=50):
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, color)
#
#     strip.show()
#     time.sleep(wait_ms / 1000.0)


def resetLeds(ring, color, wait_ms=10):
    for i in range(ring.numPixels()):
        ring.setPixelColor(i, color)
        ring.show()


signal.signal(signal.SIGINT, end_read)

if __name__ == '__main__':
    ring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    ring.begin()

    while continue_reading:
        expectsRain(ring, RED, WAIT_MS)
        stroboscopeEffect(ring, RED, WAIT_MS)
        resetLeds(ring, BLACK)
        time.sleep(5)
        expectsRain(ring, GREEN, WAIT_MS)
        stroboscopeEffect(ring, GREEN, WAIT_MS)
        resetLeds(ring, BLACK)
        time.sleep(5)
        expectsRain(ring, BLUE, WAIT_MS)
        stroboscopeEffect(ring, BLUE, WAIT_MS)
        resetLeds(ring, BLACK)
        time.sleep(5)
