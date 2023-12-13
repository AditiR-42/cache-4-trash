# Edge Impulse - OpenMV Image Classification Example

import sensor, time, os, tf, gc
import pyb
from pyb import Pin

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None

try:
    # Load built in model
    labels, net = tf.load_builtin_model('trained')
except Exception as e:
    raise Exception(e)


led1 = Pin("PA9", pyb.Pin.OUT_PP)
led2 = Pin("PB9", pyb.Pin.OUT_PP)
manual_recycling = Pin("PF3", pyb.Pin.OUT_PP)
manual_trash = Pin("PG12", pyb.Pin.OUT_PP)
clock = time.clock()

while(True):
    clock.tick()

    # user input to tilt to recycling
    if manual_recycling.value():
        print("manual recycling")
        led1.on()
        time.sleep(3)
        led1.off()
        time.sleep(1)
        pass
    # user input to tilt to non-recycling
    elif manual_trash.value():
        print("manual trash")
        led2.on()
        time.sleep(3)
        led2.off()
        time.sleep(1)
        pass

    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in net.classify(img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))

        for i in range(len(predictions_list)):
            print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

        non_recycling_chance = float(predictions_list[0][1])
        blank_chance = float(predictions_list[1][1])
        recycling_chance = float(predictions_list[2][1])

        print(non_recycling_chance, blank_chance, recycling_chance)

        # no motion (no trash)
        if blank_chance >= recycling_chance and blank_chance >= non_recycling_chance:
            led1.off()
            led2.off()
            continue
        # tilt right (recycling)
        elif recycling_chance >= non_recycling_chance:
            led1.on()
            time.sleep(3)
            led1.off()
        # tilt left (non-recycling)
        else:
            led2.on()
            time.sleep(3)
            led2.off()

    time.sleep(1)
    print(clock.fps(), "fps")
