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
font.LoadFont("fonts/10x20.bdf")
text_color = graphics.Color(0, 255, 0)

try:
    while True:
        currentTime = time.strftime("%H:%M:%S", time.gmtime())

        canvas.Clear()
        graphics.DrawText(canvas, font, 64-len(currentTime)*5, 32+6, text_color, currentTime)

        canvas = matrix.SwapOnVSync(canvas)
except KeyboardInterrupt:
    matrix.Clear()

