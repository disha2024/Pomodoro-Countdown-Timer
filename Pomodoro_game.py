import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
pink = "#e2979c"
red = "#e7305b"
green = "#9bdeac"
yellow = "#eada2b"
font_name = "Courier"
work_min = 25
short_break = 5
long_break = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=green)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = work_min * 60
    short_break_sec = short_break * 60
    long_break_sec = long_break * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=red)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=pink)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=green)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=yellow)

title_label = tk.Label(text="Timer", fg=green, bg=yellow, font=(font_name, 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(font_name, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(text="", bg=yellow, fg=green, font=(font_name, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
