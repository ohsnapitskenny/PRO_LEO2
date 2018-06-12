import time
from flask import Flask
from flask_cors import CORS
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

app = Flask(__name__)
CORS(app)

def expectsRain(ring, color, wait_ms=10):
    for t in range(0, 5, 1):
        colorWipe(ring, color, wait_ms)
        colorWipe(ring, BLACK, wait_ms)

# ColorFX's
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def resetLeds(ring, color, wait_ms=10):
    for i in range(ring.numPixels()):
        ring.setPixelColor(i, color)
        ring.show()


@app.route('/')
def hello_world():
    return 'Use /happy & /sad'

@app.route('/rain')
def expectRain():
    expectsRain(ring, RED, WAIT_MS)
    resetLeds(ring, BLACK)
    return 'Rain'

@app.route('/lost')
def lostDevice():
    expectsRain(ring, BLUE, WAIT_MS)
    resetLeds(ring, BLACK)
    return 'Lost'

@app.route('/return')
def returnDevice():
    expectsRain(ring, GREEN, WAIT_MS)
    resetLeds(ring, BLACK)
    return 'Lost'


if __name__ == '__main__':
    ring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    ring.begin()
    app.run(host='0.0.0.0')
