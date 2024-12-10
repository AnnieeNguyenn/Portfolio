
#Annie Nguyen
#Note app
#Password for a lock screen in my app is :
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from ctypes import windll
import sv_ttk

windll.shcore.SetProcessDpiAwareness(1)

tasks = []

def show_second_screen():
    """Move from lock screen to function screen."""
    user_password = password.get()
    if user_password == "123456":
        lock_frame.pack_forget()
        main_tab_frame.pack(fill='both', expand=True)
    else:
        title["text"] = "Please type it again!"
        title.config(foreground="red")

def add_task():
    """Creat a screen which get user's information and add it to a "tasks" list."""
    def save_task():
        title = title_entry.get()
        due_date = cal.get_date()
        importance = importance_var.get()

        if title and due_date and importance:
            tasks.append({"title": title, "due_date": due_date, "importance": importance})
            add_task_frame.pack_forget()
            main_tab.select(0)
        else:
            error_label.config(text="Please complete all fields", foreground="red")

    def return_to_main():
        add_task_frame.pack_forget()
        main_tab.select(0)

    add_task_frame = ttk.Frame(main_tab)
    add_task_frame.pack(fill='both', expand=True)

    for i in range(5):
        add_task_frame.grid_rowconfigure(i, weight=1)
    for i in range(2):
        add_task_frame.grid_columnconfigure(i, weight=1)

    title_label = ttk.Label(add_task_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    title_entry = ttk.Entry(add_task_frame, width=30)
    title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    cal = Calendar(add_task_frame, selectmode="day", year=2024, month=6, day=2)
    cal.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    importance_label = ttk.Label(add_task_frame, text="Importance:")
    importance_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    importance_var = tk.StringVar()
    importance_combobox = ttk.Combobox(add_task_frame, width=27, textvariable=importance_var, state="readonly")
    importance_combobox["values"] = ("Low", "Medium", "High")
    importance_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    error_label = ttk.Label(add_task_frame, text="", foreground="red")
    error_label.grid(row=3, column=0, columnspan=2)

    button_frame = ttk.Frame(add_task_frame)
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    save_button = ttk.Button(button_frame, text="Save", command=save_task)
    save_button.grid(row=0, column=0, padx=5)

    return_button = ttk.Button(button_frame, text="Return", command=return_to_main)
    return_button.grid(row=0, column=1, padx=5)

def view_task():
    """Show user which tasks they have saved (it won't show the task which user marked)."""
    def return_to_main():
        view_task_frame.pack_forget()
        main_tab.select(0)

    view_task_frame = ttk.Frame(main_tab)
    view_task_frame.pack(fill='both', expand=True)

    for i in range(len(tasks) + 1):
        view_task_frame.grid_rowconfigure(i, weight=1)
    for i in range(4):
        view_task_frame.grid_columnconfigure(i, weight=1)

    for i, task in enumerate(tasks, start=1):
        ttk.Label(view_task_frame, text=f"Task {i}").grid(row=i-1, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(view_task_frame, text=f"Title: {task["title"]}").grid(row=i-1, column=1, padx=10, pady=5, sticky="w")
        ttk.Label(view_task_frame, text=f"Due Date: {task["due_date"]}").grid(row=i-1, column=2, padx=10, pady=5, sticky="w")
        ttk.Label(view_task_frame, text=f"Importance: {task["importance"]}").grid(row=i-1, column=3, padx=10, pady=5, sticky="w")

    return_button = ttk.Button(view_task_frame, text="Return", command=return_to_main)
    return_button.grid(row=len(tasks), column=0, columnspan=4, pady=10)

def mark_task():
    """let user mark which tasks they have complete. After marked and saved, those tasks will be remove."""
    def save_marked_tasks():
        global tasks
        tasks = [task for task in tasks if not task["marked"].get()]
        mark_task_frame.pack_forget()
        main_tab.select(0)

    mark_task_frame = ttk.Frame(main_tab)
    mark_task_frame.pack(fill='both', expand=True)

    for i in range(len(tasks) + 1):
        mark_task_frame.grid_rowconfigure(i, weight=1)
    for i in range(4):
        mark_task_frame.grid_columnconfigure(i, weight=1)

    for i, task in enumerate(tasks, start=1):
        task["marked"] = tk.BooleanVar(value=False)
        ttk.Checkbutton(mark_task_frame, variable=task["marked"]).grid(row=i-1, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(mark_task_frame, text=f"Title: {task["title"]}").grid(row=i-1, column=1, padx=10, pady=5, sticky="w")
        ttk.Label(mark_task_frame, text=f"Due Date: {task["due_date"]}").grid(row=i-1, column=2, padx=10, pady=5, sticky="w")
        ttk.Label(mark_task_frame, text=f"Importance: {task["importance"]}").grid(row=i-1, column=3, padx=10, pady=5, sticky="w")

    save_button = ttk.Button(mark_task_frame, text="Save", command=save_marked_tasks)
    save_button.grid(row=len(tasks), column=0, columnspan=4, pady=10)

diary_list = []

def change_cal_box(event=None):
    """Change date box of diary's screen to let user know which date they have chosen."""
    selected_date = dical.get_date()
    cal_box.config(text=selected_date)


def add_new_diary():
    """Add new diary up to the date user choosen. If user didn't choose a date, ask them to choose one."""
    if dical.get_date():
        def save_task_diary():
            """Save all information which user put in into the list."""
            title_diary = title_entry_diary.get()
            diary_date = dical.get_date()
            weather = weather_var.get()
            note = note_diary.get("1.0", "end-1c")

            if title_diary and diary_date and weather:
                diary_list.append({"title_diary": title_diary, "diary_date": diary_date,
                                   "weather": weather, "note": note})
                diary_frame_add.pack_forget()
                main_tab.select(0)
            else:
                diary_error_label.config(text="Please complete all fields", foreground="red")

        def return_to_main_diary():
            """Return to the main screen if user don't want to continue they work."""
            diary_frame_add.pack_forget()
            main_tab.select(0)

        diary_frame_add = ttk.Frame(main_tab)
        diary_frame_add.pack(fill='both', expand=True)

        for i in range(6):
            diary_frame_add.grid_rowconfigure(i, weight=1)
        for i in range(3):
            diary_frame_add.grid_columnconfigure(i, weight=1)

        title_label_diary = ttk.Label(diary_frame_add, text="Title:", font=font_chosen)
        title_label_diary.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        title_entry_diary = ttk.Entry(diary_frame_add, width=30)
        title_entry_diary.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        diary_date_add = ttk.Label(diary_frame_add, text="Date:", font=font_chosen)
        diary_date_add.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        diary_date_date = ttk.Label(diary_frame_add, text=dical.get_date())
        diary_date_date.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        weather_label = ttk.Label(diary_frame_add, text="Weather:", font=font_chosen)
        weather_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        weather_var = tk.StringVar()
        wearther_diary = ttk.Combobox(diary_frame_add, width=27, textvariable=weather_var,
                                      state="readonly", values=["Sunny", "Cloudy", "Rainy", "Snowy"])
        wearther_diary.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        note_diary = tk.Text(diary_frame_add, width=50, height=20, font=("Courier", 10))
        note_diary.grid(row=3, columnspan=2, padx=10, pady=5)

        diary_error_label = ttk.Label(diary_frame_add, text="", foreground="red")
        diary_error_label.grid(row=4, column=0, columnspan=2)

        button_frame_diary = ttk.Frame(diary_frame_add)
        button_frame_diary.grid(row=5, column=0, columnspan=2, pady=10)

        save_button1 = ttk.Button(button_frame_diary, text="Save", command=save_task_diary)
        save_button1.grid(row=0, column=0, padx=5)

        return_button1 = ttk.Button(button_frame_diary, text="Return", command=return_to_main_diary)
        return_button1.grid(row=0, column=1, padx=5)

    else:
        diary_label["text"] = "Choose a day before the next step!"
        diary_label.config(foreground="red")

def view_diary():
    """See all tasks which user saved in a specific day. If that day don't have anything, show nothing.
    If user haven't chosen a day, ask them to choose one."""
    selected_date = dical.get_date()
    if not selected_date:
        diary_label["text"] = "Please choose a day!"
        diary_label.config(foreground="red")
        return

    diaries_for_date = [diary for diary in diary_list if diary["diary_date"] == selected_date]

    if not diaries_for_date:
        diary_label["text"] = "No diary found for this date!"
        diary_label.config(foreground="red")
        return

    def return_to_main_diary():
        view_diary_frame.pack_forget()
        main_tab.select(0)

    view_diary_frame = ttk.Frame(main_tab)
    view_diary_frame.pack(fill='both', expand=True)

    for i, diary in enumerate(diaries_for_date, start=1):
        ttk.Label(view_diary_frame, text=f"Diary {i}").grid(row=i-1, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(view_diary_frame, text=f"Title: {diary["title_diary"]}").grid(row=i-1, column=1, padx=10, pady=5, sticky="w")
        ttk.Label(view_diary_frame, text=f"Weather: {diary["weather"]}").grid(row=i-1, column=2, padx=10, pady=5, sticky="w")
        ttk.Label(view_diary_frame, text=f"Note: {diary.get("note", "")}").grid(row=i-1, column=3, padx=10, pady=5, sticky="w")

    return_button = ttk.Button(view_diary_frame, text="Return", command=return_to_main_diary)
    return_button.grid(row=len(diaries_for_date), column=0, columnspan=4, pady=10)
    
    # Reconfigure rows and columns to handle resizing
    for i in range(len(diaries_for_date) + 1):
        view_diary_frame.grid_rowconfigure(i, weight=1)
    for i in range(4):
        view_diary_frame.grid_columnconfigure(i, weight=1)

def show_first_screen():
    """Help user log out and go back to the lock screen."""
    main_tab_frame.pack_forget()
    lock_frame.pack()
    password.delete(0, tk.END)
    title["text"] = "Enter your password"
    if theme_button["text"] == "Day mode":
        title.config(foreground="white")
    else:
        title.config(foreground="black")

def day_night_mode():
    """Switch between day mode and night mode (It will change button's name)."""
    if theme_button["text"] == "Day mode":
        sv_ttk.set_theme("light")
        theme_button["text"] = "Night mode"
    else:
        sv_ttk.set_theme("dark")
        theme_button["text"] = "Day mode"

font_chosen = ("Comic Sans MS", 10, "bold") #I planned to make a font function but it have a lot of bug so maybe i will finish it later

# Main program loop
root = tk.Tk()
root.title("Note")
root.minsize(700, 500)

# Lock screen
lock_frame = ttk.Frame(root)
lock_frame.pack()

title = ttk.Label(lock_frame, text="Enter your password", font=("Comic Sans MS", 20, "bold"))
title.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

password = ttk.Entry(lock_frame, width=20)
password.grid(row=1, column=0, padx=10, pady=2, sticky="nsew")

password_button = ttk.Button(lock_frame, text="Enter", width=30, command=show_second_screen)
password_button.grid(row=2, column=0, padx=10, pady=2, sticky="nsew")

# After lock screen
main_tab_frame = ttk.Frame(root)
main_tab = ttk.Notebook(main_tab_frame, width=700, height=500)
main_tab.pack(fill='both', expand=True)

# To-do list
to_do_list = ttk.Frame(main_tab)
main_tab.add(to_do_list, text="To-do list")
tdl = ttk.Label(to_do_list, text="Notice: choose what you need and check tab bar!", font=("Comic Sans MS", 14, "bold"))
tdl.grid(row=0, column=0, padx=2, pady=10)

# add task
add_task_button = ttk.Button(to_do_list, text="Add tasks", width=15, command=add_task)
add_task_button.grid(row=1, padx=2, column=0, pady=2)

# view task
view_task_button = ttk.Button(to_do_list, text="View tasks", width=15, command=view_task)
view_task_button.grid(row=2, padx=2, column=0, pady=2)

# mark task
mark_task_button = ttk.Button(to_do_list, text="Mark tasks", width=15, command=mark_task)
mark_task_button.grid(row=3, padx=2, column=0, pady=2)

# Diary
diary = ttk.Frame(main_tab)
main_tab.add(diary, text="Diary")

diary_frame = ttk.Frame(diary)
diary_frame.pack(fill='both', expand=True)

diary_label = ttk.Label(diary_frame, text="Choose day!", font=("Comic Sans MS", 14, "bold"))
diary_label.grid(row=0, columnspan=2, sticky="nsew", pady=10)

dical = Calendar(diary_frame, selectmode="day", year=2024, month=6)
dical.grid(rowspan=3, column=0, padx=10, pady=10)

cal_box = ttk.Label(diary_frame, text = "__/__/____", font=("Comic Sans MS", 10, "bold"))
cal_box.grid(row=1, column=1, padx=10, pady=10)

di_add = ttk.Button(diary_frame, text="New diary", width=20, command=add_new_diary)
di_add.grid(row=2, column=1, padx=10, pady=10)

di_view = ttk.Button(diary_frame, text="View diary", width=20, command=view_diary)
di_view.grid(row=3, column=1, padx=10, pady=10)

dical.bind("<<CalendarSelected>>", change_cal_box)

# Setting page
setting_page = ttk.Frame(main_tab)
main_tab.add(setting_page, text="Setting")

# Theme
theme_instruction = ttk.Label(setting_page, text="Change theme of your screen", font=font_chosen)
theme_instruction.grid(row=0, column=0, padx=10, pady=2, sticky="w")

theme_button = ttk.Button(setting_page, text="Night mode", width=10, command=day_night_mode)
theme_button.grid(row=0, column=1, padx=10, pady=2)

# Log out
log_out_instruction = ttk.Label(setting_page, text="Do you need to log out?", font=font_chosen)
log_out_instruction.grid(row=1, column=0, padx=10, pady=2, sticky="w")

log_out_button = ttk.Button(setting_page, text="Log out", width=10, command=show_first_screen)
log_out_button.grid(row=1, column=1, padx=10, pady=2)

root.mainloop()
