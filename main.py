import tkinter as tk
import pyperclip
from generate import generate_password


def get_password():
    # clean errors
    copy.set('Copy')
    error.set('')
    lbl_error.forget()

    # get the parameters
    if not length.get().isdigit():
        # if the entry is not a digit, we return an error
        lbl_error.grid(column=0, row=4)
        error.set('You have to enter the password length')
        password.set('error!')
        return

    my_password = generate_password(length=int(length.get()), capitals=capitals.get(), especial=especial.get())
    password.set(my_password)
    return


def copy_password():
    pyperclip.copy(password.get())
    copy.set('Copied!')
    print('Copied')


if __name__ == '__main__':
    # tkinter instance
    root = tk.Tk()

    # we create a canvas to set all the elements
    canvas = tk.Canvas(root, width=600, height=400)
    # canvas.grid()

    # Title text
    lbl_title = tk.Label(root, text='Password Generator', fg='#F46242', font=('Arial', 24, 'bold'))
    lbl_title.grid(column=0, row=0, columnspan=3, pady=20, padx=100)

    # instructions
    instructions = tk.Label(root, text='Choose the characteristics you want your password to have', font='Arial')
    instructions.grid(column=0, row=1, columnspan=3, pady=10, padx=100)

    # password characteristics
    lbl_length = tk.Label(root, text='Password length:')
    lbl_length.grid(column=0, row=2)
    length = tk.StringVar()
    length.set('10')
    ent_length = tk.Entry(root, textvariable=length, justify='center')
    ent_length.grid(column=0, row=3)
    error = tk.StringVar()
    lbl_error = tk.Label(root, textvariable=error, fg='#EA2828')

    capitals = tk.BooleanVar()
    chk_capitals = tk.Checkbutton(root, text='Capitals', variable=capitals, onvalue=True, offvalue=False)
    chk_capitals.grid(column=1, row=3)

    especial = tk.BooleanVar()
    chk_especial = tk.Checkbutton(root, text='Especial characters', variable=especial, onvalue=True, offvalue=False)
    chk_especial.grid(column=2, row=3)

    # Button
    btn_generate = tk.Button(root, text='Generate', font='Arial', bg='#F46242', fg='white', height=1, width=15,
                             command=lambda: get_password())
    btn_generate.grid(column=0, row=5, columnspan=3, pady=20)

    # Password
    password = tk.StringVar()
    password.set('...')
    lbl_password = tk.Label(root, textvariable=password, font='Arial')
    lbl_password.grid(column=0, row=6, columnspan=3, pady=10)

    # Copy Button
    copy = tk.StringVar()
    copy.set('Copy')
    btn_copy = tk.Button(root, textvariable=copy, font='Arial', bg='#F46242', fg='white', height=1, width=10,
                         command=lambda: copy_password())
    btn_copy.grid(column=0, row=7, columnspan=3, pady=5)

    root.mainloop()
