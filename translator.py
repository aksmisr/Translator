from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import ttk, messagebox

translator = Translator()

# Create language mapping
lang_name_to_code = {name.title(): code for code, name in LANGUAGES.items()}
language_names = sorted(lang_name_to_code.keys())

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    from_language = from_lang.get()
    to_language = to_lang.get()

    if not text:
        messagebox.showerror("Error", "Please enter text to translate")
        return

    try:
        src_code = lang_name_to_code[from_language]
        dest_code = lang_name_to_code[to_language]

        translated = translator.translate(
            text, src=src_code, dest=dest_code
        ).text

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", "Translation failed")

# UI setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x420")

tk.Label(root, text="Translate From").pack()
from_lang = ttk.Combobox(root, values=language_names, state="readonly")
from_lang.pack()
from_lang.set("English")

tk.Label(root, text="Translate To").pack(pady=(10, 0))
to_lang = ttk.Combobox(root, values=language_names, state="readonly")
to_lang.pack()
to_lang.set("Hindi")

tk.Label(root, text="Enter Text").pack(pady=(10, 0))
input_text = tk.Text(root, height=5, width=55)
input_text.pack()

tk.Button(root, text="Translate", command=translate_text).pack(pady=12)

tk.Label(root, text="Translated Text").pack()
output_text = tk.Text(root, height=5, width=55)
output_text.pack()

root.mainloop()