##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("Authentication")

def test_my_button():
    print ("click!")
    frame_auth.tkraise()
    password = ent_password.get()
    print(password)
    lbl_display_pass.config( text= password)
# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack(padx=100)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=1)

lbl_password = tk.Label(frame_login, text='Password:', font='Courier')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show='v')
ent_password.pack(pady=1)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_display_pass = tk.Label(frame_auth, text='Sample', font='Courier')
lbl_display_pass.pack(padx=100)


frame_login.tkraise()

root.mainloop()