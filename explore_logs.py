import tkinter as tk
from tkinter import ttk, filedialog
import os
from datetime import datetime

class LogViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Log Explorer")
        self.root.geometry("800x600")

        # Create directory selection frame
        self.dir_frame = ttk.Frame(self.root)
        self.dir_frame.pack(side="top", fill="x")

        self.dir_label = ttk.Label(self.dir_frame, text="Directory:")
        self.dir_label.pack(side="left", padx=5, pady=5)

        self.dir_entry = ttk.Entry(self.dir_frame, width=50)
        self.dir_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.dir_button = ttk.Button(self.dir_frame, text="Browse", command=self.browse_directory)
        self.dir_button.pack(side="left", padx=5, pady=5)

        self.scan_button = ttk.Button(self.dir_frame, text="Scan Logs", command=self.scan_logs)
        self.scan_button.pack(side="left", padx=5, pady=5)

        # Create log list and details frame
        self.split_frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.split_frame.pack(fill="both", expand=True)

        self.log_list_frame = ttk.Frame(self.split_frame)
        self.split_frame.add(self.log_list_frame, weight=1)

        self.log_list = ttk.Treeview(
            self.log_list_frame, columns=("size", "modified"), show="headings"
        )
        self.log_list.heading("size", text="Size (KB)")
        self.log_list.heading("modified", text="Last Modified")
        self.log_list.bind("<<TreeviewSelect>>", self.display_log_content)
        self.log_list.pack(fill="both", expand=True)

        self.log_content_frame = ttk.Frame(self.split_frame)
        self.split_frame.add(self.log_content_frame, weight=3)

        self.log_content = tk.Text(self.log_content_frame, wrap="none", state="disabled")
        self.log_content.pack(fill="both", expand=True)

    def browse_directory(self):
        directory = filedialog.askdirectory(initialdir="/var/log")
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)

    def scan_logs(self):
        directory = self.dir_entry.get()
        if not os.path.isdir(directory):
            self.display_error("Invalid directory.")
            return

        self.log_list.delete(*self.log_list.get_children())
        for root, _, files in os.walk(directory):
            for file in files:
                if "log" in file:
                    file_path = os.path.join(root, file)
                    size = os.path.getsize(file_path) // 1024
                    modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
                    self.log_list.insert("", "end", values=(file_path, size, modified))

    def display_log_content(self, event):
        selected_item = self.log_list.selection()
        if not selected_item:
            return

        file_path = self.log_list.item(selected_item[0])["values"][0]
        try:
            with open(file_path, "r") as file:
                content = file.read()
        except Exception as e:
            content = f"Error reading file: {e}"

        self.log_content.config(state="normal")
        self.log_content.delete("1.0", tk.END)
        self.log_content.insert("1.0", content)
        self.log_content.config(state="disabled")

    def display_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_label = ttk.Label(error_window, text=message, foreground="red")
        error_label.pack(padx=10, pady=10)
        dismiss_button = ttk.Button(error_window, text="OK", command=error_window.destroy)
        dismiss_button.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = LogViewer(root)
    root.mainloop()
