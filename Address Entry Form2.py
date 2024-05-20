import tkinter as tk

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack(fill = tk.BOTH, expand=True)

# Create the Label and Entry widgets for "First Name"
lbl_first_name = tk.Label(master=frm_form, text="First Name:")
ent_first_name = tk.Entry(master=frm_form, width=50)
# Use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the
# first row of the grid
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)
frm_form.columnconfigure(lbl_first_name, weight=1)
frm_form.rowconfigure(lbl_first_name, weight=1)
frm_form.columnconfigure(ent_first_name, weight=1)
frm_form.rowconfigure(ent_first_name, weight=1)


# Create the Label and Entry widgets for "Last Name"
lbl_last_name = tk.Label(master=frm_form, text="Last Name:")
ent_last_name = tk.Entry(master=frm_form, width=50)
# Place the widgets in the second row of the grid
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)
frm_form.columnconfigure(lbl_last_name, weight=1)
frm_form.rowconfigure(lbl_last_name, weight=1)
frm_form.columnconfigure(ent_last_name, weight=1)
frm_form.rowconfigure(ent_last_name, weight=1)

# Create the Label and Entry widgets for "Address Line 1"
lbl_address1 = tk.Label(master=frm_form, text="Address Line 1:")
ent_address1 = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_address1.grid(row=2, column=0, sticky="e")
ent_address1.grid(row=2, column=1)
frm_form.columnconfigure(lbl_address1, weight=1)
frm_form.rowconfigure(lbl_address1, weight=1)
frm_form.columnconfigure(ent_address1, weight=1)
frm_form.rowconfigure(ent_address1, weight=1)

# Create the Label and Entry widgets for "Address Line 2"
lbl_address2 = tk.Label(master=frm_form, text="Address Line 2:")
ent_address2 = tk.Entry(master=frm_form, width=50)
# Place the widgets in the fourth row of the grid
lbl_address2.grid(row=3, column=0, sticky=tk.E)
ent_address2.grid(row=3, column=1)
frm_form.columnconfigure(lbl_address2, weight=1)
frm_form.rowconfigure(lbl_address2, weight=1)
frm_form.columnconfigure(ent_address2, weight=1)
frm_form.rowconfigure(ent_address2, weight=1)



# Create the Label and Entry widgets for "City"
lbl_city = tk.Label(master=frm_form, text="City:")
ent_city = tk.Entry(master=frm_form, width=50)
# Place the widgets in the fifth row of the grid
lbl_city.grid(row=4, column=0, sticky=tk.E)
ent_city.grid(row=4, column=1)
frm_form.columnconfigure(lbl_city, weight=1)
frm_form.rowconfigure(lbl_city, weight=1)
frm_form.columnconfigure(ent_city, weight=1)
frm_form.rowconfigure(ent_city, weight=1)


# Create the Label and Entry widgets for "State/Province"
lbl_state = tk.Label(master=frm_form, text="State/Province:")
ent_state = tk.Entry(master=frm_form, width=50)
# Place the widgets in the sixth row of the grid
lbl_state.grid(row=5, column=0, sticky=tk.E)
ent_state.grid(row=5, column=1)
frm_form.columnconfigure(lbl_state, weight=1)
frm_form.rowconfigure(lbl_state, weight=1)
frm_form.columnconfigure(ent_state, weight=1)
frm_form.rowconfigure(ent_state, weight=1)


# Create the Label and Entry widgets for "Postal Code"
lbl_postal_code = tk.Label(master=frm_form, text="Postal Code:")
ent_postal_code = tk.Entry(master=frm_form, width=50)
# Place the widgets in the seventh row of the grid
lbl_postal_code.grid(row=6, column=0, sticky=tk.E)
ent_postal_code.grid(row=6, column=1)
frm_form.columnconfigure(lbl_postal_code, weight=1)
frm_form.rowconfigure(lbl_postal_code, weight=1)
frm_form.columnconfigure(ent_postal_code, weight=1)
frm_form.rowconfigure(ent_postal_code, weight=1)


# Create the Label and Entry widgets for "Country"
lbl_country = tk.Label(master=frm_form, text="Country:")
ent_country = tk.Entry(master=frm_form, width=50)
# Place the widgets in the eight row of the grid
lbl_country.grid(row=7, column=0, sticky=tk.E)
ent_country.grid(row=7, column=1)
frm_form.columnconfigure(lbl_country, weight=1)
frm_form.rowconfigure(lbl_country, weight=1)
frm_form.columnconfigure(ent_country, weight=1)
frm_form.rowconfigure(ent_country, weight=1)



# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    
# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
def saved_data():
   text_file = open("test.txt", "a")
   text_file.write(ent_first_name.get()+"\n")
   text_file.write(ent_last_name.get()+"\n")
   text_file.write(ent_address1.get()+"\n")
   text_file.write(ent_address2.get()+"\n")
   text_file.write(ent_city.get()+"\n")
   text_file.write(ent_state.get()+"\n")
   text_file.write(ent_postal_code.get()+"\n")
   text_file.write(ent_country.get()+"\n")
   text_file.close()


def handle_clicked(event):
   saved_data()
   print("the data was saved to: test.txt")
   clear_text()
    
btn_submit = tk.Button(master=frm_buttons, command=saved_data , text="Submit")
btn_submit.bind("<Button-1>", handle_clicked)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
def clear_text():
    ent_first_name.delete(0, "end")
    ent_last_name.delete(0, "end")
    ent_address1.delete(0, "end")
    ent_address2.delete(0, "end")
    ent_city.delete(0, "end")
    ent_state.delete(0, "end")
    ent_postal_code.delete(0, "end")
    ent_country.delete(0, "end")
def clicked(event):
    clear_text()
    print("Cleared")

btn_clear = tk.Button(master=frm_buttons, command=clear_text, text="Clear")
btn_clear.bind("<Button-1>", clicked)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

def leaving():
   clear_text()
   print("Goodbye")
   quit()
def leave(event):
   leaving()
btn_submit = tk.Button(master=frm_buttons, command=leaving , text="quit")
btn_submit.bind("<Button-1>", leave)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Start the application
window.mainloop()
