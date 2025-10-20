def on_gesture_tilt_left():
    radio.send_number(2)
    basic.show_icon(IconNames.SMALL_HEART)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    radio.send_number(1)
    basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_number(4)
    basic.show_icon(IconNames.TSHIRT)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_gesture_logo_up():
    radio.send_number(3)
    basic.show_icon(IconNames.YES)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

radio.set_group(228)

def on_forever():
    pass
basic.forever(on_forever)
