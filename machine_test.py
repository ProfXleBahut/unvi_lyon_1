import os
import psutil
import platform
import shutil
from GPUtil import getGPUs

def analyze_system_resources():
    # Informations sur le système
    system_info = platform.uname()
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}\n")

    # Mémoire (RAM)
    ram = psutil.virtual_memory()
    print(f"Total RAM: {ram.total / (1024**3):.2f} GB")
    print(f"Available RAM: {ram.available / (1024**3):.2f} GB\n")

    # CPU
    cpu_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    print(f"CPU Cores: {cpu_count}")
    print(f"CPU Frequency: {cpu_freq.max:.2f} MHz\n")

    # Disque
    disk = shutil.disk_usage("/")
    print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024**3):.2f} GB\n")

    # GPU
    gpus = getGPUs()
    if gpus:
        for gpu in gpus:
            print(f"GPU Name: {gpu.name}")
            print(f"  Total Memory: {gpu.memoryTotal:.2f} MB")
            print(f"  Free Memory: {gpu.memoryFree:.2f} MB")
            print(f"  Load: {gpu.load * 100:.1f}%\n")
    else:
        print("No GPU detected.\n")

    # Évaluation des capacités
    print("### Evaluation ###")
    if ram.total / (1024**3) < 8:
        print("Warning: Limited RAM (<8 GB). Resource-intensive tasks may fail.")
    if disk.free / (1024**3) < 20:
        print("Warning: Limited Disk Space (<20 GB). Check available space.")
    if cpu_freq.max < 2000:
        print("Warning: Low CPU frequency (<2 GHz). Tasks may be slow.")
    if not gpus:
        print("Warning: No GPU detected. Tasks requiring GPU acceleration won't be possible.")
    else:
        gpu_memory_free = min([gpu.memoryFree for gpu in gpus])
        if gpu_memory_free < 2000:
            print("Warning: Limited GPU memory (<2 GB). Large models may not fit into memory.")

    print("\nSystem check complete.")


if __name__ == "__main__":
    analyze_system_resources()
