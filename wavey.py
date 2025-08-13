# wavey.py
import tkinter as tk
import wave
from hello_transalation import hello_translations

root = tk.Tk()
root.title("Wavey Chatbot - Hello Translator")
root.geometry("400x300")
root.configure(bg="#e6f7ff")
def translate():
    lang = entry.get()
    result = hello_translations.get(lang.lower(), "Sorry, I don't know that language yet!")
    output_label.config(text=f"Wavey says: {result}")

# GUI Elements

root.iconbitmap("wavey.ico")
root.geometry("400x400")

title = tk.Label(root, text=" Wavey Chatbot - Say Hello in Any Language!", font=("Arial", 14), bg="#e6f7ff")
title.pack(pady=10)

entry_label = tk.Label(root, text="Enter Language:", font=("Arial", 12), bg="#e6f7ff")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

translate_btn = tk.Button(root, text="Translate", font=("Arial", 12), command=translate, bg="#052444", fg="white")
translate_btn.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#003366")
output_label.pack(pady=20)




lang = input("Which language do you want to say Hello in? ").lower()

if lang in hello_translations:
    print(f"In {lang.title()}, 'Hello' is: {hello_translations[lang]}")

while True:
    lang = input("Enter a language (or type 'exit' to quit): ").lower()

    if lang == 'exit':
        print("Goodbye 👋")
        break

    if lang in hello_translations:
        print(f"In {lang.title()}, 'Hello' is: {hello_translations[lang]}")
    else:
        print("Sorry, I don't know that language yet!")
root.mainloop()