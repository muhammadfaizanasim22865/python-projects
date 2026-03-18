



import tkinter as tk
from tkinter import ttk
import speedtest

# Function to test internet speed
def test_speed():
    label_status.config(text="Testing... Please wait.", foreground="#00aaff")
    root.update()

    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download = st.download() / 1_000_000  
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        label_download.config(text=f"Download Speed: {download:.2f} Mbps")
        label_upload.config(text=f"Upload Speed: {upload:.2f} Mbps")
        label_ping.config(text=f"Ping: {ping:.2f} ms")
        label_status.config(text="Test Completed", foreground="#00ff00")

    except Exception as e:
        label_status.config(text=f"Error: {e}", foreground="#ff5555")

# Setup root window
root = tk.Tk()
root.title("Internet Speed Tester (Dark Mode)")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#121212")  # Dark background

# Style ttk widgets for dark mode
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton",
                foreground="#ffffff",
                background="#333333",
                font=("Helvetica", 12),
                padding=10)
style.map("TButton",
          background=[('active', '#555555')])

# Heading label
label_title = tk.Label(root, text="Internet Speed Tester", font=("Helvetica", 16, "bold"),
                       bg="#121212", fg="#ffffff")
label_title.pack(pady=15)

# Speed result labels
label_download = tk.Label(root, text="Download Speed: -- Mbps", font=("Helvetica", 12),
                          bg="#121212", fg="#bbbbbb")
label_download.pack(pady=5)

label_upload = tk.Label(root, text="Upload Speed: -- Mbps", font=("Helvetica", 12),
                        bg="#121212", fg="#bbbbbb")
label_upload.pack(pady=5)

label_ping = tk.Label(root, text="Ping: -- ms", font=("Helvetica", 12),
                      bg="#121212", fg="#bbbbbb")
label_ping.pack(pady=5)

# Status label
label_status = tk.Label(root, text="", font=("Helvetica", 10),
                        bg="#121212", fg="#00aaff")
label_status.pack(pady=10)

# Test button
btn_test = ttk.Button(root, text="Start Test", command=test_speed)
btn_test.pack(pady=20)

# Run the GUI
root.mainloop()
