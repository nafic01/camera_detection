import tkinter as tk
from tkinter import ttk
import object_counter  
from object_counter import run
import handtracker
colour = 0

# Open handtracker.py
def run_hand_tracker():
    handtracker.main()
    print("Running Hand Tracker...")

# Function to handle colour selection
def set_colour(val, popup): # Popup is used in the paraemeter of this function because we want to destroy the popup after the user selects a colour.
    global colour
    colour = val
    print("Colour variable set to", colour)
    object_counter.run(colour)
    popup.destroy()


# Pop up function
def ColourSelect():
    """
    Creates a popup window with buttons to select a colour.
    """
    popup = tk.Toplevel()
    popup.title("Select Colour")
    popup.geometry("250x150")

    popup_label = ttk.Label(popup, text="Select a colour to detect:")
    popup_label.pack(pady=10)

    red_button = ttk.Button(
        popup, 
        text="Red", 
        command=lambda: set_colour(1, popup)
    ) 
    red_button.pack(pady=5)

    green_button = ttk.Button(
        popup, 
        text="Green", 
        command=lambda: set_colour(2, popup)
    )
    green_button.pack(pady=5)

    blue_button = ttk.Button(
        popup, 
        text="Blue", 
        command=lambda: set_colour(3, popup)
    )
    blue_button.pack(pady=5)

# Calls the object_counter.py when the "Object Counter" button is clicked
def on_object_counter():
    """
    Run the object_counter program and print a message.
    """
    object_counter.run()  # Make sure your object_counter.py has a run() function
    print("Running Object Counter...")

# -- GUI stuff --
# Create the main application window
root = tk.Tk()
root.focus_force()  # Ensure the window is focused when it opens
root.title("Object and Hand Gesture Detection")
root.geometry("400x250")

# Main frame
mainframe = ttk.Frame(root, padding=30)
mainframe.pack(expand=True)

# Title
title = ttk.Label(mainframe, text="Object and Hand Gesture Detection")
title.pack(pady=(0, 15))

# Options label
options_label = ttk.Label(mainframe, text="Options")
options_label.pack(pady=(0, 10))

# Buttons
# Object Counter button opens the colour selection popup
object_button = ttk.Button(
    mainframe,
    text="Object Counter",
    command=ColourSelect,
    width=25
)
object_button.pack(pady=5)

# Hand Gesture Detection button (currently just prints a message)
hand_gesture_button = ttk.Button(
    mainframe,
    text="Hand Gesture Detection",
    command=run_hand_tracker,
    width=25
)
hand_gesture_button.pack(pady=5)

# Start the main Tkinter event loop
root.mainloop()