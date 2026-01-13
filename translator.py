from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import messagebox

translator = Translator()

language_codes = list(LANGUAGES.keys())
language_names = [lang.lower() for lang in LANGUAGES.values()]

def translate_text():
    src = from_lang.get().lower()
    dest = to_lang.get().lower()
    text = word_entry.get()

    if not text:
        messagebox.showerror("Error", "Please enter text")
        return

    if ((src in language_codes or src in language_names) and
        (dest in language_codes or dest in language_names)):
        try:
            result = translator.translate(text, src=src, dest=dest).text
            output_label.config(text=result.capitalize())
        except:
            messagebox.showerror("Error", "Translation failed")
    else:
        messagebox.showerror("Error", "Invalid language code or name")

# UI setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("400x300")

tk.Label(root, text="Translate From").pack()
from_lang = tk.Entry(root)
from_lang.pack()

tk.Label(root, text="Text").pack()
word_entry = tk.Entry(root, width=40)
word_entry.pack()

tk.Label(root, text="Translate To").pack()
to_lang = tk.Entry(root)
to_lang.pack()

tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

output_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
output_label.pack()

root.mainloop()


