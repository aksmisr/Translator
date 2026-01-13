from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import ttk, messagebox

# Translator instance
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

    except Exception:
        messagebox.showerror("Error", "Translation failed")

# ================= UI SETUP =================

root = tk.Tk()
root.title("Language Translator")
root.geometry("500x430")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("default")

style.configure(
    "TCombobox",
    fieldbackground="#2a2a3d",
    background="#2a2a3d",
    foreground="#ffffff"
)

style.configure(
    "TButton",
    background="#4f46e5",
    foreground="#ffffff",
    font=("Segoe UI", 10, "bold"),
    padding=6
)

style.map(
    "TButton",
    background=[("active", "#4338ca")]
)

label_style = {
    "bg": "#1e1e2f",
    "fg": "#f1f1f1",
    "font": ("Segoe UI", 10)
}

# ================= UI ELEMENTS =================

tk.Label(root, text="Translate From", **label_style).pack()
from_lang = ttk.Combobox(root, values=language_names, state="readonly")
from_lang.pack(pady=4)
from_lang.set("English")

tk.Label(root, text="Translate To", **label_style).pack(pady=(10, 0))
to_lang = ttk.Combobox(root, values=language_names, state="readonly")
to_lang.pack(pady=4)
to_lang.set("Hindi")

tk.Label(root, text="Enter Text", **label_style).pack(pady=(10, 0))
input_text = tk.Text(
    root,
    height=5,
    width=55,
    bg="#2a2a3d",
    fg="#ffffff",
    insertbackground="white",
    relief="flat"
)
input_text.pack(pady=4)

ttk.Button(root, text="Translate", command=translate_text).pack(pady=14)

tk.Label(root, text="Translated Text", **label_style).pack()
output_text = tk.Text(
    root,
    height=5,
    width=55,
    bg="#2a2a3d",
    fg="#ffffff",
    insertbackground="white",
    relief="flat"
)
output_text.pack(pady=4)

# ================= RUN APP =================

root.mainloop()