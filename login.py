import tkinter as tk
from typing import Text

root = tk.Tk()

sign_in_username_var = tk.StringVar()
register_username_var = tk.StringVar()
sign_in_password_var = tk.StringVar()
register_password_var = tk.StringVar()

canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(columnspan=3, rowspan=3)

#Register
register = tk.Label(root, text = "Register now", font=('Calibri', 20))
register.place(relwidth=0.95, relheight=0.2, relx=0.01)

register_frame = tk.Frame(root, bg='light gray')
register_frame.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.25)

register_username_text = tk.Label(register_frame, text = "Username", bg='light gray', font='Arial, 10')
register_username_text.pack()

register_username_entry = tk.Entry(register_frame, bg='white', textvariable=register_username_var)
register_username_entry.pack()

sign_in_password_text = tk.Label(register_frame, text = "Password", bg='light gray', font='Arial, 10')
sign_in_password_text.pack()

register_password_entry = tk.Entry(register_frame, bg='white', textvariable=register_password_var)
register_password_entry.pack()


def validate_register():
    global register_password
    global register_username

    register_password = register_password_var.get()
    register_username = register_username_var.get()

    register_username_entry.delete(0, 'end')
    register_password_entry.delete(0, 'end')

register = tk.Button(register_frame, command = validate_register, text='Register', font='Arial, 8' )
register.place(rely= 0.75, relx=0.4)


#Sign in
sign_in_now = tk.Label(root, text = "Please sign in", font=('Calibri', 20))
sign_in_now.place(relwidth=0.95, relheight=0.2, rely=0.45, relx=0.01)

sign_in_frame = tk.Frame(root, bg='light gray')
sign_in_frame.place(relx=0.25, rely=0.60, relwidth=0.5, relheight=0.25)

sign_in_username_text = tk.Label(sign_in_frame, text = "Username", bg='light gray', font='Arial, 10')
sign_in_username_text.pack()

sign_in_username_entry = tk.Entry(sign_in_frame, bg='white', textvariable=sign_in_username_var)
sign_in_username_entry.pack()

sign_in_password_text = tk.Label(sign_in_frame, text = "Password", bg='light gray', font='Arial, 10')
sign_in_password_text.pack()

sign_in_password_entry = tk.Entry(sign_in_frame, bg='white', textvariable=sign_in_password_var)
sign_in_password_entry.pack()

def validate():
    sign_in_password = sign_in_password_var.get()
    sign_in_username = sign_in_username_var.get()

    if sign_in_password == register_password and sign_in_username == register_username:
        msg = tk.Label(root, text='You signed in succesfully!', fg='green')
        msg.place(rely=0.9, relx=0.35)
        return
    else:
        msg = tk.Label(root, text='Your password or username doesnt match', fg='red')
        msg.place(rely=0.9, relx=0.28)
        return

sign_in = tk.Button(sign_in_frame, command = validate, text='Sign in', font='Arial, 8' )
sign_in.place(rely= 0.75, relx=0.4)

root.mainloop()




