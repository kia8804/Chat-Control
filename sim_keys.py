import pyautogui
import time

import pyautogui

def simulate_key_input(key_input: str):
    """
    Simulates pressing a single key or a combination of keys.

    Parameters:
    key_input (str): The key or combination of keys to simulate pressing.
                     For combinations, keys should be separated by spaces. Example: 'ctrl home'
    """
    try:
        keys = key_input.split()
        if len(keys) > 1:
            pyautogui.hotkey(*keys)
            print(f"Successfully pressed the combination: {', '.join(keys)}")
        else:
            pyautogui.press(keys[0])
            print(f"Successfully pressed the '{keys[0]}' key.")
    except Exception as e:
        print(f"An error occurred: {e}")

def multi_key_press(str):
    keys = str.rsplit("\n")
    for key in keys:
        key = key.strip()
        simulate_key_input(key)
        time.sleep(0.1)
    print(f"Successfully pressed the '{str}' key.")

# # Example usage:
# simulate_key_input('a')         # This will simulate pressing the 'a' key.
# simulate_key_input('ctrl home') # This will simulate pressing Ctrl + Home.
# # simulate_key_input('shift home') # This will simulate pressing Ctrl + Home.

# multi_key_press("""ctrl a
#                 ctrl c""")