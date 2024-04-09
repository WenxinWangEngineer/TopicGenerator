import tkinter as tk 
from tkinter import filedialog, Text

import Main


def select_topics():
    topics = topics_entry.get()
    Main.main(topics.split(','))


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

topics_label = tk.Label(frame, text="Enter topics (comma-separated):")
topics_label.pack()

topics_entry = tk.Entry(frame)
topics_entry.pack()

start_button = tk.Button(frame, text="Start", padx=10, pady=5,
                         fg="white", bg="#263D42", command=select_topics)
start_button.pack()

root.mainloop()
