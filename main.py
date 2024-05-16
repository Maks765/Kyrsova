import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv


def show_contacts_window(contacts_data):
    contacts_window = tk.Toplevel()
    contacts_window.title("Контакти")
    contacts_window.geometry("800x300")

    tk.Label(contacts_window, text="ПІБ", font=("Time new roman", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(contacts_window, text="Адреса", font=("Time new roman", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(contacts_window, text="Електронна пошта", font=("Time new roman", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
    tk.Label(contacts_window, text="Мобільний телефон", font=("Time new roman", 10, "bold")).grid(row=0, column=3, padx=5, pady=5)

    if contacts_data:  
        for i, contact in enumerate(contacts_data, start=1):
            tk.Label(contacts_window, text=contact[0]).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(contacts_window, text=contact[1]).grid(row=i, column=1, padx=5, pady=5)
            tk.Label(contacts_window, text=contact[2]).grid(row=i, column=2, padx=5, pady=5)
            tk.Label(contacts_window, text=contact[3]).grid(row=i, column=3, padx=5, pady=5)
    else:
        messagebox.showinfo("Контакти", "Список контактів порожній")


def view_contacts():
    with open('contacts.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        contacts.sort(key=lambda x: x[0])  

    if contacts:
        show_contacts_window(contacts)
    else:
        messagebox.showinfo("Контакти", "Список контактів порожній")


def add_contact():
    name = simpledialog.askstring("Додати контакт", "Введіть ПІБ:")
    address = simpledialog.askstring("Додати контакт", "Введіть адресу:")
    email = simpledialog.askstring("Додати контакт", "Введіть електронну пошту:")
    mobile_phone = simpledialog.askstring("Додати контакт", "Введіть мобільний телефон:")

    if name and address and email and mobile_phone:
        with open('contacts.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name, address, email, mobile_phone])

        messagebox.showinfo("Успіх", "Контакт успішно доданий")
    else:
        messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля")


def delete_contact():
    name_to_delete = simpledialog.askstring(
        "Видалення контакту", "Введіть ПІБ контакту, якого бажаєте видалити:")
    if name_to_delete:
        with open('contacts.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        updated_contacts = [
            contact for contact in contacts if contact[0] != name_to_delete
        ]

        with open('contacts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts)

        messagebox.showinfo("Успіх", "Контакт успішно видалений")
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть ПІБ контакту")


def search_contact():
    search_param = simpledialog.askstring(
        "Пошук контакту", "Введіть ПІБ або номер телефону для пошуку:")
    if search_param:
        with open('contacts.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        found_contacts = [
            contact for contact in contacts if search_param.lower() in contact[0].lower()
            or search_param in contact[3]
        ]

        if found_contacts:
            show_contacts_window(found_contacts)
        else:
            messagebox.showinfo("Пошук контакту", "Контакт не знайдений")
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть параметр пошуку")




def edit_contact():
    global name_entry, address_entry, email_entry, mobile_entry  

    name_to_edit = simpledialog.askstring(
        "Редагування контакту", "Введіть ПІБ контакту, якого бажаєте відредагувати:")
    if name_to_edit:
        with open('contacts.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        for contact in contacts:
            if contact[0] == name_to_edit:
                edit_window = tk.Toplevel()  
                edit_window.title("Редагування контакту")
                edit_window.geometry("350x200")

               
                tk.Label(edit_window, text="ПІБ:").grid(row=0, column=0, padx=5, pady=5)
                tk.Label(edit_window, text="Адреса:").grid(row=1, column=0, padx=5, pady=5)
                tk.Label(edit_window, text="Електронна пошта:").grid(row=2, column=0, padx=5, pady=5)
                tk.Label(edit_window, text="Мобільний телефон:").grid(row=3, column=0, padx=5, pady=5)

                name_entry = tk.Entry(edit_window)
                name_entry.grid(row=0, column=1, padx=5, pady=5)
                name_entry.insert(0, contact[0])

                address_entry = tk.Entry(edit_window)
                address_entry.grid(row=1, column=1, padx=5, pady=5)
                address_entry.insert(0, contact[1])

                email_entry = tk.Entry(edit_window)
                email_entry.grid(row=2, column=1, padx=5, pady=5)
                email_entry.insert(0, contact[2])

                mobile_entry = tk.Entry(edit_window)
                mobile_entry.grid(row=3, column=1, padx=5, pady=5)
                mobile_entry.insert(0, contact[3])

                
                save_button = ttk.Button(edit_window, text="Зберегти", command=save_changes)
                save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

                break
        else:
            messagebox.showinfo("Пошук контакту", "Контакт не знайдений")
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть ПІБ контакту")


def save_changes():
    new_name = name_entry.get()
    new_address = address_entry.get()
    new_email = email_entry.get()
    new_mobile_phone = mobile_entry.get()

    

    messagebox.showinfo("Успіх", "Інформація успішно оновлена")

My_window = tk.Tk()
My_window.title("Телефонна довідник ")
My_window.geometry("350x200")

add_button = ttk.Button(My_window, text="Додати контакт", style="TButton", command=add_contact)
add_button.grid(row=5, column=0, columnspan=1, padx=100, pady=5, sticky="ew")


edit_button = ttk.Button(My_window,text="Редагувати контакт", style="TButton", command=edit_contact)
edit_button.grid(row=6, column=0, columnspan=1, padx=100, pady=5, sticky="ew")


view_button = ttk.Button(My_window, text="Переглянути контакти", style="TButton", command=view_contacts)
view_button.grid(row=7, column=0, columnspan=1, padx=100, pady=5, sticky="ew")


delete_button = ttk.Button(My_window, text="Видалити контакт", style="TButton", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=1, padx=100, pady=5, sticky="ew")


search_button = ttk.Button(My_window, text="Пошук контакту", style="TButton", command=search_contact)
search_button.grid(row=9, column=0, columnspan=1, padx=100, pady=5, sticky="ew")

My_window.mainloop()
