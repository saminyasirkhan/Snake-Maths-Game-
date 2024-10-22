#Initialasiations
from tkinter import *
from PIL import Image
from tkinter import messagebox
import ast
from pygame.locals import *
from subprocess import call



#File conversions:
input_png = 'LogInIcon.png'
output_ico = 'LogInIcon.ico'
input_jpg = 'RegisterImage.jpeg'
output_ico2 = 'RegisterImage.ico'

# Open the PNG file
Icon_img = Image.open(input_png)

# Save the icon as an ICO file
Icon_img.save(output_ico)

input_png = 'LogInIcon.png'
output_ico = 'LogInIcon.ico'

# Open the PNG file
Icon_img = Image.open(input_png)

# Save it as an ICO file
Icon_img.save(output_ico)


window = Tk()
window.title('Login')
icon_path = 'LogInIcon.ico'
window.iconbitmap(default=icon_path)
window.geometry('925x500+300+200')
window.configure(bg="#606060")
window.resizable(False,False)


def enter_digit(digit):
    current_pin = pin_entry.get()
    if len(current_pin) < 4:
        pin_entry.insert(END, str(digit))

def clear_pin():
    pin_entry.delete(0, END)

def check_pin():
    entered_pin = pin_entry.get()
    PIN = '1234'

    if entered_pin.isdigit() and len(entered_pin) == 4 and entered_pin == PIN:
        result_label.config(text="PIN Accepted")
        window2.destroy()
        set_up()  # Call your set up function
    else:
        result_label.config(text="Invalid PIN")

def create_pin_entry_window():
    global window2
    # Create the window
    window2 = Tk()
    window2.title("PIN Entry")

    window2.geometry(f"{200}x{300}+{700}+{400}")
    window2.configure(bg="#2f2f30")

    # Create and place widgets
    pin_label = Label(window2, text="Enter 4-digit PIN:", bg="#2f2f30", fg="white")
    pin_label.pack(pady=10)

    global pin_entry
    pin_entry = Entry(window2, show="*", bg="white", fg="black", justify="center", font=("Helvetica", 16))  
    pin_entry.pack(pady=10)

    # Create number buttons
    button_frame = Frame(window2, bg="#2f2f30")
    for i in range(1, 10):
        button = Button(button_frame, text=str(i), command=lambda i=i: enter_digit(i), width=4, height=2,bg='orange')
        button.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

    zero_button = Button(button_frame, text="0", command=lambda: enter_digit(0), width=4, height=2,bg='orange')
    zero_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = Button(button_frame, text="Clear", command=clear_pin, width=4, height=2,bg='orange')
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    submit_button = Button(button_frame, text="OK", bg='orange', command=check_pin,width=4, height=2)
    submit_button.grid(row=3, column=2, padx=5, pady=5)

    button_frame.pack()

    

    

    global result_label
    result_label = Label(window2, text="", bg="#2f2f30", fg="white")
    result_label.pack(pady=10)

    # Run the main loop
    window2.mainloop()


def login():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    try:
        file = open('datasheet.txt', 'r')
        data = file.read()
        user_data = ast.literal_eval(data)
        file.close()

        if username in user_data and password == user_data[username]:
            # Close the login window
            window.destroy()
        else:
            messagebox.showerror('Invalid', 'Invalid username or password')
    except Exception as e:
        messagebox.showerror('Error', 'An error occurred: ' + str(e))


    if username in r.keys() and password == r[username]:

        try:
           
            window.destroy()
        except:
            pass

        try:
           
            window2.destroy()
        except:
            pass



        from subprocess import call
        call(["python", "main 2.py", "--username", username])

    else:
        messagebox.showerror('Invalid','invalid username or password')
def on_login_button_pressed():
    # window.destroy()
    pass

def set_up():
    global window
    window = Toplevel(window)
    window.title("Register")
    window.geometry('925x500+300+200')
    window.configure(bg='#606060')
    window.resizable(False,False)


    def register():
        username=user.get()
        password=code.get().strip()
        conform_password=confirm_code.get().strip()
        # Condition 1: Password must contain 6 charecters
        if len(password) < 6:
            messagebox.showerror('Invalid', 'Password must be at least 6 characters long')
            return
        # Condition 2: Password must contain an uppercase letter
        if not any(char.isupper() for char in password):
            messagebox.showerror('Invalid', 'Password must contain at least one uppercase letter')
            return

        # Condition 3: Password must contain a number
        if not any(char.isdigit() for char in password):
            messagebox.showerror('Invalid', 'Password must contain at least one number')
            return



        if password == conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Register','Successefully registered')
        
            except:
                file=open('datasheet.txt','w')
                pp=str({'username':'password'})
                file.close()
        else:
            messagebox.showerror('Invalid', 'Both Passwords have to match')

   

    window.title("Register")
    window.geometry('925x500+300+200')
    icon_path = 'LogInIcon.ico'
    window.iconbitmap(default=icon_path)
    window.configure(bg='#606060')
    window.resizable(False,False)


    img = PhotoImage(file = 'RegisterImage.png')
    img = img.subsample(4)
    Label(window,image=img,border=0,bg='#606060').place(x=50,y=90)

    frame = Frame(window, width=350, height = 390,bg='#313131')
    frame.place(x=480,y=50)

    heading = Label(frame,text='Register', fg='orange',bg = '#2f2f30', font=('Mincrosoft Yahei UI Light', 23,'bold'))
    heading.place(x=100,y=5)

    def accessing(e):
        user.delete(0,'end')
        user.config(fg='orange')

    def departing(e):
        if user.get()=='':
            user.insert(0, 'username')
            user.config(fg='orange')

    user = Entry(frame,width=25,fg='orange',border=2,bg='#2f2f30',font=('Mincrosoft Yahei UI Light', 11))
    user.place(x=30,y=90)
    user.insert(0,'username')
    user.bind("<FocusIn>",accessing)
    user.bind("<FocusOut>",departing)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def accessing(e):
        code.delete(0,'end')
        code.config(fg='orange')


    def departing(e):
        if code.get()=='':
            code.insert(0, 'password')
            code.config(fg='orange')



    code = Entry(frame,width=25,fg='orange',border=2,bg='#2f2f30',font=('Mincrosoft Yahei UI Light', 11))
    code.place(x=30,y=150)
    code.insert(0,'password')
    code.bind("<FocusIn>",accessing)
    code.bind("<FocusOut>",departing)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=110)

    def accessing(e):
        confirm_code.delete(0,'end')
        confirm_code.config(fg='orange')


    def departing(e):
        if confirm_code.get()=='':
            confirm_code.insert(0, 'Confirm password')
            confirm_code.config(fg='orange')

    confirm_code = Entry(frame,width=25,fg='orange',border=2,bg='#2f2f30',font=('Mincrosoft Yahei UI Light', 11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,'Confirm password')
    confirm_code.bind("<FocusIn>",accessing)
    confirm_code.bind("<FocusOut>",departing)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    Button(frame,width=39,pady=7,text='Register',bg='orange',fg='black',border=0, command=register).place(x=35,y=280)
    label=Label(frame,text='I already have an account -->', fg='white',bg='#2f2f30',font=('Mincrosoft YaHei UI Light',9))
    label.place(x=35,y=340)

    login = Button(frame,width=6,text='Sign in',border=0,bg='#2f2f30',cursor='hand2',fg='orange',command=on_login_button_pressed)
    login.place(x=200,y=340)

    window.mainloop()


frame=Frame(window,width=350,height=350,bg="#313131")
frame.place(x=300,y=70)

heading=Label(frame,text = 'Log in',fg='orange',bg='#2f2f30',font=('Mincrosoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=0)


user = Entry(frame,width=25,fg='orange',border=2,bg="#2f2f30",font=('Mincrosoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'username')


def departing(e):
    name=code.get()
    if name == '':
        user.insert(0,'Password')


def accessing(e):
    user.delete(0,'end')

user.bind('<FocusIn>', accessing)
user.bind('<FocusOut>', departing)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)



def departing(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')



def accessing(e):
    code.delete(0,'end')


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)



register = Button(frame,width=6,text='Register', border=0,bg='#2f2f30',cursor='hand2',fg='orange', command = create_pin_entry_window)
register.place(x=215,y=270)


Button(frame,width=39,pady=7,text='Log in',bg='orange',fg='black',border=0,command=login,font=('Mincrosoft YaHei UI Light',9)).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='white',bg='#2f2f30',font=('Mincrosoft YaHei UI Light',9))
label.place(x=75,y=270)


code = Entry(frame,width=25,fg='orange',border=2,bg="#2f2f30",font=('Mincrosoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', accessing)
code.bind('<FocusOut>', departing)


window.mainloop()