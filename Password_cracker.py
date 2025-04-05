import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sys
import threading

def start_cracking(zip_path, dict_path):
    try:
        with open(dict_path, "r") as file:
            passwords = [line.strip() for line in file]
            progress = 100 / len(passwords)
            info_label["text"] = "Postęp przetwarzania hasła"
            for i, password in enumerate(passwords):
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.setpassword(password.encode('utf-8'))
                        if zip_ref.testzip() is None:
                            print(f"Znaleziono hasło! {password}")
                            progress_bar["value"] = 100
                            info_label["text"] = f"Znaleziono hasło! {password}"
                            return
                        else:
                            print(f"Testowane hasło: {password}")
                            progress_bar["value"] += progress
                except RuntimeError as e:
                    if "Bad password" in str(e):
                        print(f"Testowane hasło: {password}")
                        progress_bar["value"] += progress
                    else:
                        print("Prawdopodobnie próbowałeś oszukać program, poprzez niepoprawny słownik!")
                        break
                except FileNotFoundError:
                    print(f"Nie znaleziono podanej ścieżki dla pliku zip")
                    info_label["text"] = "Nie znaleziono podanej ścieżki dla pliku zip"
            print("Nie znaleziono działającego hasła")
            info_label["text"] = "Nie znaleziono działającego hasła."
    except FileNotFoundError:
        print("Nie znaleziono podanej ścieżki dla słownika")
        info_label["text"] = "Nie znaleziono podanej ścieżki dla słownika"
    except Exception as e:
        print(f"{e}")
        info_label["text"] = f"{e}"
def select_zip_file():
    zip_file_path = filedialog.askopenfilename(filetypes=[("Zip Files", "*.zip")])
    zip_file_entry.delete(0, tk.END)
    zip_file_entry.insert(0, zip_file_path)

def select_txt_file():
    txt_file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    txt_file_entry.delete(0, tk.END)
    txt_file_entry.insert(0, txt_file_path)

def start_thread():
    crack_thread = threading.Thread(target=start_cracking, args=(zip_file_entry.get(), txt_file_entry.get()))
    crack_thread.daemon = True
    crack_thread.start()

def closing_gui():
    window.destroy()

window = tk.Tk()
window.title("Password cracker")

zip_file_label = tk.Label(window, text="Ścieżka do pliku zip:")
zip_file_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
zip_file_entry = tk.Entry(window, width=50)
zip_file_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
zip_file_button = tk.Button(window, text="Browse", command=select_zip_file)
zip_file_button.grid(row=0, column=2, padx=10, pady=5)

txt_file_label = tk.Label(window, text="Ścieżka do słownika:")
txt_file_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
txt_file_entry = tk.Entry(window, width=50)
txt_file_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
txt_file_button = tk.Button(window, text="Browse", command=select_txt_file)
txt_file_button.grid(row=1, column=2, padx=10, pady=5)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

info_label = ttk.Label(window, text="Kliknij 'Start', aby rozpocząć.")
info_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

ok_button = tk.Button(window, text="Start", command=start_thread)
ok_button.grid(row=4, column=0, columnspan=3, pady=10)

end_button = tk.Button(window, text="End", command=closing_gui)
end_button.grid(row=5, column=0, columnspan=3, pady=10)

window.mainloop()