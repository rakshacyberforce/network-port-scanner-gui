import tkinter as tk
from tkinter import ttk, filedialog
import socket
import threading
import time

# ---------------- SERVICES ----------------
services = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3",
    143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    3389: "RDP", 5900: "VNC", 8080: "HTTP-Alt"
}

stop_scan = False
open_ports = []

# ---------------- SCAN PORT ----------------
def scan_port(port, target):
    global open_ports
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        if s.connect_ex((target, port)) == 0:
            service = services.get(port, "Unknown")
            result = f"[+] Port {port} OPEN ({service})\n"
            result_box.insert(tk.END, result)
            open_ports.append(result)

        s.close()
    except:
        pass

# ---------------- START SCAN ----------------
def start_scan():
    global stop_scan, open_ports
    stop_scan = False
    open_ports = []

    target = target_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    result_box.delete(1.0, tk.END)
    progress['value'] = 0

    total_ports = end_port - start_port + 1
    scanned = 0

    def run():
        nonlocal scanned
        start_time = time.time()

        for port in range(start_port, end_port + 1):
            if stop_scan:
                break

            t = threading.Thread(target=scan_port, args=(port, target))
            t.start()

            scanned += 1
            progress['value'] = (scanned / total_ports) * 100

        end_time = time.time()
        result_box.insert(tk.END, f"\nScan Completed in {round(end_time - start_time, 2)} sec\n")

    threading.Thread(target=run).start()

# ---------------- STOP SCAN ----------------
def stop():
    global stop_scan
    stop_scan = True

# ---------------- SAVE RESULTS ----------------
def save_results():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            for line in open_ports:
                f.write(line)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Network Port Scanner | Rakshacyber Force")
root.geometry("600x520")

# Heading
tk.Label(root, text="Network Port Scanner", font=("Arial", 16, "bold")).pack(pady=5)
tk.Label(root, text="By Kunj Patel | Rakshacyber Force", font=("Arial", 10)).pack()

# Inputs
tk.Label(root, text="Target IP / Host").pack()
target_entry = tk.Entry(root)
target_entry.pack()

tk.Label(root, text="Start Port").pack()
start_port_entry = tk.Entry(root)
start_port_entry.insert(0, "1")
start_port_entry.pack()

tk.Label(root, text="End Port").pack()
end_port_entry = tk.Entry(root)
end_port_entry.insert(0, "1024")
end_port_entry.pack()

# Buttons
tk.Button(root, text="Start Scan", command=start_scan).pack(pady=5)
tk.Button(root, text="Stop", command=stop).pack(pady=5)
tk.Button(root, text="Save Results", command=save_results).pack(pady=5)

# Progress Bar
progress = ttk.Progressbar(root, length=400, mode='determinate')
progress.pack(pady=10)

# Result Box
result_box = tk.Text(root, height=15)
result_box.pack()

# Footer
tk.Label(root, text="Developed by Kunj Patel (Rakshacyber Force)", font=("Arial", 9)).pack(pady=5)

root.mainloop()