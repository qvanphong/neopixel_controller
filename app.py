from flask import Flask
import board
import neopixel

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('on')
def turn_on():
    neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    return 'success'


@app.route('off')
def turn_off():
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    pixels.fill((0, 0, 0))
    return 'success'


if __name__ == '__main__':
    app.run()
