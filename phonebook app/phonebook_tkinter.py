import tkinter as tk
from tkinter import messagebox

# Phone Book data
phone_book = {}

# Bubble Sort function
def bubble_sort_items(items, key_func):
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if key_func(items[j]) > key_func(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def insert_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return
    
    phone_book[name] = {"phone": phone, "email": email}
    messagebox.showinfo("Success", f"Contact '{name}' added.")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def search_contact():
    name = entry_name.get().strip()
    if name in phone_book:
        d = phone_book[name]
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"Name: {name}\nPhone: {d['phone']}\nEmail: {d['email']}\n")
    else:
        messagebox.showerror("Not Found", "Contact not found!")

def display_sorted_by_name():
    text_output.delete("1.0", tk.END)
    if not phone_book:
        text_output.insert(tk.END, "Phone book is empty.\n")
        return
    items = bubble_sort_items(list(phone_book.items()), key_func=lambda it: it[0].lower())
    text_output.insert(tk.END, "Contacts (Sorted by Name):\n")
    for name, d in items:
        text_output.insert(tk.END, f"{name} -> {d['phone']} | {d['email']}\n")

def display_sorted_by_phone():
    text_output.delete("1.0", tk.END)
    if not phone_book:
        text_output.insert(tk.END, "Phone book is empty.\n")
        return
    def phone_key(it):
        raw = it[1].get("phone", "")
        digits = "".join(filter(str.isdigit, raw))
        return int(digits) if digits else 0
    items = bubble_sort_items(list(phone_book.items()), key_func=phone_key)
    text_output.insert(tk.END, "Contacts (Sorted by Phone):\n")
    for name, d in items:
        text_output.insert(tk.END, f"{name} -> {d['phone']} | {d['email']}\n")

# GUI Window
root = tk.Tk()
root.title("📖 Phone Book App (with Sorting)")
root.geometry("500x500")

# Input Fields
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Buttons
tk.Button(root, text="Insert Contact", command=insert_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Show Contacts (By Name)", command=display_sorted_by_name).pack(pady=5)
tk.Button(root, text="Show Contacts (By Phone)", command=display_sorted_by_phone).pack(pady=5)

# Output Box
text_output = tk.Text(root, height=15, width=60)
text_output.pack(pady=10)

root.mainloop()
