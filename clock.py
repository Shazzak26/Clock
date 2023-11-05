from tkinter import *
from tkinter.ttk import *
from time import strftime, localtime

root = Tk()
root.overrideredirect(True)  # Remove window decorations (title bar)
root.attributes('-transparentcolor', 'black')  # Set the background color to be transparent
root.attributes('-topmost', True)  # Make the window stay on top

# Set the window size and position near the taskbar
window_width = 180
window_height = 40
taskbar_offset = 30  # Adjust this value based on your screen resolution
root.geometry(f"{window_width}x{window_height}+{root.winfo_screenwidth() - window_width}+{root.winfo_screenheight() - window_height - taskbar_offset - 60}")

canvas = Canvas(root, width=window_width, height=window_height, background="black", highlightthickness=0)
canvas.pack()

def update_time():
    current_time = strftime('%H:%M:%S', localtime())
    current_date = strftime('%a, %b %d', localtime())  # Adjusted date format

    canvas.delete("clock")  # Clear previous clock drawings
    canvas.create_text(window_width // 2, window_height // 2 - 5, text=current_time, font=("DS-DIGIB", 18), fill="#003366", tag="clock")  # Dark Blue

    canvas.create_text(window_width // 2, window_height // 2 + 15, text=current_date, font=("DS-DIGIB", 10), fill="#005699", tag="clock_date")  # Lighter Blue

    root.after(1000, update_time)

update_time()

root.mainloop()
