import ctypes
import time
import pygetwindow as gw

# Constants for setting window transparency
WS_EX_LAYERED = 0x80000
LWA_ALPHA = 0x2

# Getting the handle of the window
def get_window_handle(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        return windows[0]._hWnd  # Get the handle (HWND) of the window
    return None

# Function to make a window transparent
def make_window_transparent(window_title, transparency=150):
    hwnd = get_window_handle(window_title)
    if hwnd:
        # Get the current window style
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        # Add layered style
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, style | WS_EX_LAYERED)
        # Set the transparency level (0 = fully transparent, 255 = opaque)
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)
        print(f"Window '{window_title}' transparency set to {transparency}.")
    else:
        print(f"Window '{window_title}' not found.")

# Example: Make Notepad transparent (if running)
if __name__ == "__main__":
    window_name = "New Tab - Google Chrome"  # Change this to your target window title
    time.sleep(2)  # Waiting for opening the app
    make_window_transparent(window_name, transparency=150)  # Adjusting transparency (0-255)
