from pynput import mouse
from pynput.keyboard import Key, Controller

keyboard = Controller()

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        # keyboard.press(Key.esc)
        # keyboard.release(Key.esc)
        #after pressing the esc-key: stopPropagation(middle mouse click should not be forwarded to windows)
        print('hello')
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)

# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()   