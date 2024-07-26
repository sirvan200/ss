import tkinter as tk

# دیکشنری برای نگاشت حروف فارسی به انگلیسی
persian_to_english = {
    'ا': 'a', 'ب': 'f', "پ": '"\"', 'ت': 'j', 'ث': 'e', 'ج': '[', 'چ': ']', 'ح': 'p',
    'خ': 'o', 'د': 'n', 'ذ': 'b',   'ر': 'v', 'ز': 'c', 'ژ': 'c', 'س': 's', 'ش': 'a',
    'ص': 'w', 'ض': 'q', 'ط': 'x'  , 'ظ': 'z', 'ع': 'u', 'غ': 'y', 'ف': 't', 'ق': 'r',
    'ک': ';', 'گ': '"""', 'ل': 'g', 'م': 'l', 'ن': 'k', 'و': ',', 'ه': 'i', 'ی': 'd',
    'ا':'h','ئ':'m',
    ' ': ' ', '\n': '\n'
}

# دیکشنری برای نگاشت حروف انگلیسی به فارسی
english_to_persian = {v: k for k, v in persian_to_english.items()}

def translate_text():
    input_text = input_textbox.get("1.0", "end-1c").strip()  # دریافت متن ورودی
    if input_text:  # اگر متن ورودی خالی نباشد
        # تشخیص زبان متن
        if any(char in persian_to_english for char in input_text):
            # تبدیل فارسی به انگلیسی
            translated_text = ''.join(persian_to_english.get(char, char) for char in input_text)
        else:
            # تبدیل انگلیسی به فارسی
            translated_text = ''.join(english_to_persian.get(char, char) for char in input_text)
    else:
        translated_text = "متن ورودی خالی است"

    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", translated_text)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Bidirectional Translator")

# ایجاد لیبل و جعبه متنی برای ورودی
input_label = tk.Label(root, text="Enter text:")
input_label.pack(pady=5)

input_textbox = tk.Text(root, height=10, width=50)
input_textbox.pack(pady=5)

# ایجاد دکمه برای ترجمه
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# ایجاد لیبل و جعبه متنی برای خروجی
output_label = tk.Label(root, text="Translated text:")
output_label.pack(pady=5)

output_textbox = tk.Text(root, height=10, width=50)
output_textbox.pack(pady=5)

# اجرای حلقه اصلی برنامه
root.mainloop()
