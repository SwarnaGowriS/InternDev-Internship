import tkinter as tk
from tkinter import filedialog, Text

# Initialize the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a Text widget
text = Text(root, wrap='word')
text.pack(expand=1, fill='both')

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()
