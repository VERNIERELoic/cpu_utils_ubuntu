########################
# Author: Loïc VERNIERE
__version__ = "1.0.0"
########################

import tkinter as tk
import psutil
import GPUtil
from threading import Timer

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{round(bytes, 2)}{unit}B"
        bytes /= 1024
    return f"{round(bytes, 2)}PB"

def get_cpu_temperature():
    try:
        # Tente de lire la température du CPU
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return f"{temps['coretemp'][0].current} °C"
        else:
            return "N/A"
    except:
        return "N/A"


def update_info():
    # RAM
    ram = psutil.virtual_memory()
    total_ram.set(f"Total RAM: {get_size(ram.total)}")
    used_ram.set(f"Used RAM: {get_size(ram.used)}")
    percent_ram.set(f"RAM Usage: {ram.percent}%")
    

    # CPU
    cpu_usage.set(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    # Mise à jour de la température du CPU
    cpu_temperature.set(f"CPU Temperature: {get_cpu_temperature()}")

    # GPU
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_name.set(f"GPU: {gpu.name}")
        gpu_load.set(f"GPU Load: {gpu.load*100}%")
        gpu_free_memory.set(f"GPU Free Memory: {get_size(gpu.memoryFree)}")
        gpu_used_memory.set(f"GPU Used Memory: {get_size(gpu.memoryUsed)}")
        gpu_total_memory.set(f"GPU Total Memory: {get_size(gpu.memoryTotal)}")
        gpu_temperature.set(f"GPU Temperature: {gpu.temperature} °C")
    else:
        gpu_name.set("GPU: Not Found")

    # Mise à jour toutes les secondes
    root.after(1000, update_info)

# Création de la fenêtre
root = tk.Tk()
root.title(f"System Information Tool - Version {__version__}")
root.wait_visibility(root)
root.wm_attributes('-alpha',0.6)

total_ram = tk.StringVar()
used_ram = tk.StringVar()
percent_ram = tk.StringVar()
cpu_usage = tk.StringVar()
cpu_temperature = tk.StringVar()
gpu_name = tk.StringVar()
gpu_load = tk.StringVar()
gpu_free_memory = tk.StringVar()
gpu_used_memory = tk.StringVar()
gpu_total_memory = tk.StringVar()
gpu_temperature = tk.StringVar()

tk.Label(root, textvariable=total_ram).pack()
tk.Label(root, textvariable=used_ram).pack()
tk.Label(root, textvariable=percent_ram).pack()
tk.Label(root, textvariable=cpu_usage).pack()
tk.Label(root, textvariable=cpu_temperature).pack()
tk.Label(root, textvariable=gpu_name).pack()
tk.Label(root, textvariable=gpu_load).pack()
tk.Label(root, textvariable=gpu_free_memory).pack()
tk.Label(root, textvariable=gpu_used_memory).pack()
tk.Label(root, textvariable=gpu_total_memory).pack()
tk.Label(root, textvariable=gpu_temperature).pack()



update_info()  # Première mise à jour des informations

# Démarrer la boucle principale de l'interface
root.mainloop()
