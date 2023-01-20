import psutil
import tkinter as tk 

root = tk.Tk() 
root.geometry("200x50")
root.title("Battery percentage")

battery = psutil.sensors_battery() 

if battery: 
    plugged = battery.power_plugged
    percent = battery.percent 

    if plugged: 
        label_text = f"Battery percentage: {percent}% (Plugged in)"
    else: 
        label_text = f"Battery percentage: {percent}% (Not plugged in)"
else: 
    label_text = "Battery information is not available"

label = tk.Label(root, text=label_text)
label.pack() 

root.mainloop()