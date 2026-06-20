


import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# =====================
# APP STATE
# =====================

sales_total = 0.0
expense_total = 0.0


# =====================
# FUNCTIONS
# =====================

def switch_page(name):

    for frame in pages.values():
        frame.place_forget()

    pages[name].place(
        x=300,
        y=30,
        width=850,
        height=720
    )


def update_dashboard():

    profit = sales_total - expense_total

    sales_value.config(
        text=f"Le {sales_total:.2f}"
    )

    expense_value.config(
        text=f"Le {expense_total:.2f}"
    )

    profit_value.config(
        text=f"Le {profit:.2f}"
    )


def add_sale():

    global sales_total

    try:

        product = sale_product.get()

        quantity = int(
            sale_qty.get()
        )

        price = float(
            sale_price.get()
        )

        amount = quantity * price

        sales_total += amount

        history.insert(
            tk.END,
            f"SALE | {product} | Le {amount:.2f}\n"
        )

        update_dashboard()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter valid sale values."
        )


def add_expense():

    global expense_total

    try:

        amount = float(
            expense_box.get()
        )

        expense_total += amount

        history.insert(
            tk.END,
            f"EXPENSE | Le {amount:.2f}\n"
        )

        update_dashboard()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter valid expense."
        )


def export_report():

    try:

        with open(
            "report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                history.get(
                    "1.0",
                    tk.END
                )
            )

        messagebox.showinfo(
            "Success",
            "Report exported."
        )

    except OSError:

        messagebox.showerror(
            "Error",
            "Unable to save."
        )


def show_profit():

    messagebox.showinfo(

        "Profit",

        f"Le {sales_total-expense_total:.2f}"
    )


def clear_all():

    global sales_total
    global expense_total

    sales_total = 0
    expense_total = 0

    history.delete(
        "1.0",
        tk.END
    )

    update_dashboard()


def update_clock():

    clock.config(

        text=

        datetime.now().strftime(
            "%d %b %Y | %H:%M:%S"
        )
    )

    root.after(
        1000,
        update_clock
    )


# =====================
# WINDOW
# =====================

root = tk.Tk()

root.geometry(
"1200x800"
)

root.title(
"Smart Business Manager"
)


canvas = tk.Canvas(
root,
bg="#141E30"
)

canvas.place(
relwidth=1,
relheight=1
)


# =====================
# SIDEBAR
# =====================

sidebar = tk.Frame(
root,
bg="#0F172A"
)

sidebar.place(
x=0,
y=0,
width=250,
height=800
)


tk.Label(

sidebar,

text=
"💼 Smart\nBusiness",

font=(
"Arial",
24,
"bold"
),

fg="white",

bg="#0F172A"

).pack(
pady=40
)


# =====================
# PAGES
# =====================

pages = {}

names = [

"Dashboard",

"Sales",

"Expenses",

"Reports",

"Settings"

]

for page in names:

    frame = tk.Frame(
        root,
        bg="white"
    )

    pages[page] = frame

    tk.Label(

        frame,

        text=page,

        font=(
            "Arial",
            20,
            "bold"
        ),

        bg="white"

    ).pack(
        pady=20
    )


# =====================
# DASHBOARD
# =====================

clock = tk.Label(
pages["Dashboard"],
bg="white"
)

clock.pack()


cards = tk.Frame(
pages["Dashboard"],
bg="white"
)

cards.pack()


sales_value = tk.Label(
cards,
text="Le 0",
width=20
)

sales_value.pack(
side=tk.LEFT
)


expense_value = tk.Label(
cards,
text="Le 0",
width=20
)

expense_value.pack(
side=tk.LEFT
)


profit_value = tk.Label(
cards,
text="Le 0",
width=20
)

profit_value.pack(
side=tk.LEFT
)


history = tk.Text(
pages["Dashboard"],
width=80,
height=20
)

history.pack(
pady=30
)


# =====================
# SALES PAGE
# =====================

sales_form = tk.Frame(
    pages["Sales"],
    bg="white"
)

sales_form.pack(
    pady=20
)


tk.Label(
    sales_form,
    text="Product Name",
    bg="white"
).pack()

sale_product = tk.Entry(
    sales_form,
    width=40
)

sale_product.pack(
    pady=6
)


tk.Label(
    sales_form,
    text="Quantity",
    bg="white"
).pack()

sale_qty = tk.Entry(
    sales_form,
    width=40
)

sale_qty.pack(
    pady=6
)


tk.Label(
    sales_form,
    text="Unit Price",
    bg="white"
).pack()

sale_price = tk.Entry(
    sales_form,
    width=40
)

sale_price.pack(
    pady=6
)


tk.Button(

    sales_form,

    text="Add Sale",

    command=add_sale,

    width=20,

    bg="#5B2EFF",

    fg="white"

).pack(
    pady=20
)

# =====================
# EXPENSE PAGE
# =====================

expense_box = tk.Frame(
pages["Expenses"],
bg="white"
)

expense_box.pack(
pady=20
)


def create_expense_input(text):

    tk.Label(

        expense_box,

        text=text,

        bg="white"

    ).pack()

    field = tk.Entry(

        expense_box,

        width=40

    )

    field.pack(
        pady=5
    )

    return field


expense_name_input = (
create_expense_input(
"Expense Name"
)
)


tk.Label(

expense_box,

text=
"Category",

bg="white"

).pack()


expense_category = (
tk.StringVar(
value="Transport"
)
)


tk.OptionMenu(

expense_box,

expense_category,

"Transport",

"Utilities",

"Salary",

"Food",

"Inventory",

"Other"

).pack()


expense_qty = (
create_expense_input(
"Quantity"
)
)


expense_cost = (
create_expense_input(
"Unit Cost"
)
)


tk.Label(

expense_box,

text=
"Notes",

bg="white"

).pack()


expense_notes = tk.Text(

expense_box,

width=35,

height=4

)

expense_notes.pack(
pady=10
)


tk.Button(

expense_box,

text=
"Add Expense",

command=
add_expense,

bg="#FF477E",

fg="white",

width=20

).pack(
pady=10
)

# =====================
# REPORT PAGE
# =====================

reports_panel = tk.Frame(
    pages["Reports"],
    bg="white"
)

reports_panel.pack(
    pady=20
)


report_output = tk.Text(
    reports_panel,
    width=70,
    height=18,
    font=("Arial", 11)
)

report_output.pack(
    pady=15
)


def generate_report():

    report_output.delete(
        "1.0",
        tk.END
    )

    profit = (
        sales_total -
        expense_total
    )

    if profit > 0:
        status = "PROFIT 📈"

    elif profit < 0:
        status = "LOSS 📉"

    else:
        status = "BREAK EVEN ⚖️"

    report_output.insert(

        tk.END,

f"""
SMART BUSINESS REPORT
==============================

Date:
{datetime.now().strftime("%d %b %Y")}

--------------------------------

TOTAL SALES:
Le {sales_total:.2f}

TOTAL EXPENSES:
Le {expense_total:.2f}

NET PROFIT:
Le {profit:.2f}

BUSINESS STATUS:
{status}

--------------------------------

RECENT TRANSACTIONS

{history.get("1.0", tk.END)}

==============================
END OF REPORT
"""
    )


def save_report():

    generate_report()

    try:

        with open(
            "business_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(

                report_output.get(
                    "1.0",
                    tk.END
                )
            )

        messagebox.showinfo(
            "Success",
            "Report exported."
        )

    except OSError:

        messagebox.showerror(
            "Error",
            "Unable to export."
        )


def report_summary():

    profit = (
        sales_total -
        expense_total
    )

    messagebox.showinfo(

        "Quick Summary",

f"""
Sales:
Le {sales_total:.2f}

Expenses:
Le {expense_total:.2f}

Profit:
Le {profit:.2f}
"""
    )


controls = tk.Frame(
    reports_panel,
    bg="white"
)

controls.pack()


buttons = [

("Generate Report", generate_report),

("Quick Summary", report_summary),

("Export Report", save_report)

]


for text, command in buttons:

    tk.Button(

        controls,

        text=text,

        width=18,

        command=command,

        bg="#5B2EFF",

        fg="white"

    ).pack(
        side=tk.LEFT,
        padx=8
    )

# =====================
# SETTINGS FUNCTIONS
# =====================

dark_mode = False


def toggle_dark_mode():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:

        bg = "#181818"
        fg = "white"

    else:

        bg = "white"
        fg = "black"

    for frame in pages.values():

        frame.configure(
            bg=bg
        )

        for widget in frame.winfo_children():

            try:

                widget.configure(
                    bg=bg,
                    fg=fg
                )

            except tk.TclError:
                pass


def reset_totals():

    global sales_total
    global expense_total

    answer = messagebox.askyesno(
        "Reset",
        "Reset all business totals?"
    )

    if answer:

        sales_total = 0
        expense_total = 0

        update_dashboard()

        messagebox.showinfo(
            "Success",
            "Totals reset."
        )


def clear_history():

    answer = messagebox.askyesno(
        "Clear",
        "Delete transaction history?"
    )

    if answer:

        history.delete(
            "1.0",
            tk.END
        )

        messagebox.showinfo(
            "Done",
            "History cleared."
        )


def business_status():

    profit = (
        sales_total -
        expense_total
    )

    if profit > 0:

        status = "Business is profitable 📈"

    elif profit < 0:

        status = "Business is operating at loss 📉"

    else:

        status = "Business is neutral ⚖️"

    messagebox.showinfo(
        "Business Status",
        status
    )


def app_info():

    messagebox.showinfo(

        "About",

"""
Smart Business Manager Pro

Version 2.0

Features:
• Dashboard
• Sales
• Expenses
• Reports
• Settings
"""
    )


# =====================
# SETTINGS PAGE
# =====================

settings_panel = tk.Frame(
    pages["Settings"],
    bg="white"
)

settings_panel.pack(
    pady=30
)


buttons = [

("🌙 Dark Mode", toggle_dark_mode),

("🔄 Reset Totals", reset_totals),

("🧹 Clear History", clear_history),

("📄 Export Report", export_report),

("📊 Business Status", business_status),

("ℹ️ About App", app_info)

]


for text, command in buttons:

    tk.Button(

        settings_panel,

        text=text,

        width=28,

        height=2,

        command=command,

        bg="#243B55",

        fg="white"

    ).pack(
        pady=10
    )

# =====================
# SIDEBAR BUTTONS
# =====================

for page in names:

    tk.Button(

        sidebar,

        text=page,

        width=18,

        bg="#172033",

        fg="white",

        command=
        lambda p=page:
        switch_page(p)

    ).pack(
        pady=10
    )


update_dashboard()

update_clock()

switch_page(
"Dashboard"
)

root.mainloop()