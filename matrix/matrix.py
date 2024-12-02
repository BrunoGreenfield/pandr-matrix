from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

# Options (the flags that we used in the examples)
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm' 
options.gpio_slowdown = 4
options.pwm_bits = 8

matrix = RGBMatrix(options=options)

canvas = matrix.CreateFrameCanvas()

font = graphics.Font()
font.LoadFont("fonts/7x13.bdf")
text_color = graphics.Color(0, 255, 0)

text = "PANDR-Matrix"

try:
    while True:
        graphics.DrawText(canvas, font, 0, 32, text_color, text)
        
        canvas = matrix.SwapOnVSync(canvas)
except KeyboardInterrupt:
    matrix.Clear()

