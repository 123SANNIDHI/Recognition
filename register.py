import tkinter as tk
import re
import sqlite3
import page1
import page2
import page3
from PIL import ImageTk, Image
from tkinter import messagebox


# Function to handle user login
def login():


    username = entry_username.get()
    password = entry_password_login.get()

    # Connect to the database
    connection = sqlite3.connect("reg.db")
    cursor = connection.cursor()

    # Check if the username and password match
    query = "SELECT * FROM user WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result is not None:
        label_status.config(text="Login Successful", fg="green")
        switch_to_main_page()
    else:
        label_status.config(text="Invalid username or password", fg="red")

    # Close the database connection
    cursor.close()
    connection.close()

# Function to handle user registration
def register():
    # Your registration code here
    username = entry_username_reg.get()
    user_email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Validate email format
    if not validate_email(user_email):
        label_status.config(text="Invalid email format", fg="red")
        return

    # Validate password
    if not validate_password(password):
        label_status.config(text="Invalid password format", fg="red")
        return

    # Check if password matches confirm password
    if password != confirm_password:
        label_status.config(text="Passwords do not match", fg="red")
        return

    # Connect to the database
    connection = sqlite3.connect("reg.db")
    cursor = connection.cursor()

    # Check if the username is already taken
    query = "SELECT * FROM user WHERE username=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result is not None:
        label_status.config(text="Username already taken", fg="red")
    else:
        # Insert new user into the database
        insert_query = "INSERT INTO user (username, email, password, confirm_password) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_query, (username, user_email, password, confirm_password))
        connection.commit()
        label_status.config(text="Registration Successful", fg="green")

    # Close the database connection
    cursor.close()
    connection.close()

# Function to validate email format
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# Function to validate password format
def validate_password(password):
    # Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.fullmatch(pattern, password)

# Create the main window
window = tk.Tk()
window.title("User Login")
image = Image.open("bg1.jpg")
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_title = tk.Label(window, text="RECOGNER", font=("Italic", 20, "bold"),bg="lightblue",width=10,height=2)
label_title.grid(row=0,column=0,padx=10,pady=10)



# Create login frame
frame_login = tk.Frame(window, bg="light blue",padx=80,pady=60)
frame_login.grid(row=0, column=0,padx=350,pady=20)

# Set the width and height of the login frame
frame_login.grid_propagate(0)
frame_login.configure(width=500, height=450)         



# Create username label and entry in login frame
label_username_login = tk.Label(frame_login, text="Username :", font=("Montserrat",15,"bold"),bg="light blue")
label_username_login.grid(row=0, column=0,padx=10,pady=15)
entry_username = tk.Entry(frame_login,font=("Montserrat",13,"bold"))
entry_username.grid(row=0, column=1,padx=10,pady=15)

# Create password label and entry in login frame
label_password_login = tk.Label(frame_login, text="Password  :", font=("Montserrat",15,"bold"),bg="light blue")
label_password_login.grid(row=1, column=0,padx=10,pady=20)
entry_password_login = tk.Entry(frame_login, show="*",font=("Montserrat",13,"bold"))
entry_password_login.grid(row=1, column=1,padx=10,pady=15)

# Create login button in login frame
button_login = tk.Button(frame_login, text="Login", command=login, font=("Montserrat",15,"bold"),bg="light blue")
button_login.grid(row=2, column=0, columnspan=2,padx=10,pady=20)

# Create status label for displaying registration/login status
label_status = tk.Label(window, text="",font=("italic",8,"bold"),bg="light blue",padx=10,pady=10)
label_status.grid(padx=10,pady=10)


#Forgot password

def open_forgot_password_page():
    frame_login.grid_forget()  # Hide the login frame
    frame_forgot_password.grid(padx=400, pady=50)  # Show the forgot password frame

frame_forgot_password = tk.Frame(window, bg="light blue")
frame_forgot_password.grid_propagate(0)
frame_forgot_password.configure(width=500, height=400)


label_back_to_login = tk.Label(frame_forgot_password, text="Back to Login", fg="blue", cursor="hand2",font=("italic", 12, "bold"), bg="light blue")
label_back_to_login.grid(row=5, column=0, columnspan=2, padx=20,pady=15)
label_back_to_login.bind("<Button-1>", lambda e: switch_to_forgotto_login())

def switch_to_forgotto_login():
    frame_forgot_password.grid_forget()  # Hide the forgot password frame
    frame_login.grid(padx=350,pady=20)  # Show the login frame


label_username_forgot = tk.Label(frame_forgot_password, text="Username:", font=("Italic", 13, "bold"),bg="lightblue")
label_username_forgot.grid(row=0, column=0,padx=20,pady=18)
entry_username_forgot = tk.Entry(frame_forgot_password, font=("Italic", 15))
entry_username_forgot.grid(row=0, column=1)

label_new_password = tk.Label(frame_forgot_password, text="New Password:", font=("Italic", 13, "bold"),bg="lightblue")
label_new_password.grid(row=1, column=0,padx=20,pady=18)
entry_new_password = tk.Entry(frame_forgot_password, show="*", font=("Italic", 15))
entry_new_password.grid(row=1, column=1)

label_confirm_new_password = tk.Label(frame_forgot_password, text="Confirm New Password:", font=("Italic", 13, "bold"),bg="lightblue")
label_confirm_new_password.grid(row=2, column=0,padx=20,pady=18)
entry_confirm_new_password = tk.Entry(frame_forgot_password, show="*", font=("Italic", 15))
entry_confirm_new_password.grid(row=2, column=1)

def update_password():
    username = entry_username_forgot.get()
    new_password = entry_new_password.get()
    confirm_new_password = entry_confirm_new_password.get()

    # Validate new password
    if not validate_password(new_password):
        messagebox.showerror("Password Update", "Invalid password format")
        return

    # Check if new password and confirm password match
    if new_password != confirm_new_password:
        messagebox.showerror("Password Update", "New password and confirm password do not match")
        return

    # Connect to the database
    connection = sqlite3.connect("reg.db")
    cursor = connection.cursor()

    # Check if the username exists
    query = "SELECT * FROM user WHERE username=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result is not None:
        # Update the password
        update_query = "UPDATE user SET password=? WHERE username=?"
        cursor.execute(update_query, (new_password, username))
        connection.commit()
        messagebox.showinfo("Password Update", "Password updated successfully")
    else:
        messagebox.showerror("Password Update", "Invalid username")

    # Close the database connection
    cursor.close()
    connection.close()



    # Check if the username and current password match
def validate_password(password):
    # Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.fullmatch(pattern, password)


button_update_password = tk.Button(frame_forgot_password, text="Update Password", font=("Italic", 15, "bold"),bg="lightblue", command=update_password)
button_update_password.grid(row=4, column=0, columnspan=2, padx=20,pady=25)


label_forgot_password = tk.Label(frame_login, text="Forgot Password?", fg="blue", cursor="hand2", font=("italic", 12, "bold"), bg="light blue")
label_forgot_password.grid(row=5, column=0, columnspan=2, padx=50, pady=10)
label_forgot_password.bind("<Button-1>", lambda e: open_forgot_password_page())


# Function to switch to the registration page
def switch_to_registration():
    frame_login.grid_forget()  # Hide the login frame
    frame_registration.grid(padx=400, pady=50)  # Show the registration frame

# Create register button in login frame
label_login = tk.Label(frame_login, text="Create a New Account",font=("italic",9,"bold"),bg="light blue",padx=20,pady=1)
label_login.grid(row=3, column=0, columnspan=2,padx=20, pady=1)

register_link = tk.Label(frame_login, text="Register", fg="blue", cursor="hand2",font=("italic",12,"bold"),bg="light blue")
register_link.grid(row=4, column=0, columnspan=2,padx=50, pady=10)
register_link.bind("<Button-1>", lambda e: switch_to_registration())

# Create registration frame
frame_registration = tk.Frame(window, bg="light blue",padx=80,pady=60)

# Set the width and height of the registration frame
frame_registration.grid_propagate(0)
frame_registration.configure(width=550, height=400)


# Create username label and entry in registration frame
label_username_reg = tk.Label(frame_registration, text="Username:", font=("italic", 15,"bold"),bg="light blue")
label_username_reg.grid(row=0, column=0,padx=1,pady=2)
entry_username_reg = tk.Entry(frame_registration, font=("Italic", 15))
entry_username_reg.grid(row=0, column=1)

# Create email label and entry in registration frame
label_email = tk.Label(frame_registration, text="Email:", font=("Italic", 15,"bold"),bg="light blue")
label_email.grid(row=1, column=0,padx=10,pady=15)
entry_email = tk.Entry(frame_registration, font=("Italic", 15))
entry_email.grid(row=1, column=1,padx=10,pady=15)

# Create password label and entry in registration frame
label_password = tk.Label(frame_registration, text="Password:", font=("Italic", 15,"bold"),bg="light blue")
label_password.grid(row=2, column=0,padx=10,pady=8)
entry_password = tk.Entry(frame_registration, show="*",font=("Italic",15))
entry_password.grid(row=2, column=1,padx=10,pady=8)

# Create confirm password label and entry in registration frame
label_confirm_password = tk.Label(frame_registration, text="Confirm Password:", font=("Italic", 15,"bold"),bg="light blue")
label_confirm_password.grid(row=3, column=0,padx=10,pady=10)
entry_confirm_password = tk.Entry(frame_registration, show="*",font=("Italic",15))
entry_confirm_password.grid(row=3, column=1)

# Create registration button in registration frame
button_register = tk.Button(frame_registration, text="Register", command=register, font=("Italic", 15,"bold"),bg="light blue")
button_register.grid(row=4, column=0, columnspan=2,padx=10,pady=15)

def switch_to_login():
    frame_registration.grid_forget()  # Hide the registration frame
    frame_login.grid(padx=350,pady=20)  # Show the login frame

# Create login link in registration frame
label_login = tk.Label(frame_registration, text="Already have an account?",font=("Italic", 8,"bold"),bg="light blue")
label_login.grid(row=5, column=0, columnspan=2)
login_link = tk.Label(frame_registration, text="Login", fg="blue", cursor="hand2",font="bold")
login_link.grid(row=6, column=0, columnspan=2)
login_link.bind("<Button-1>", lambda e: switch_to_login())

# Initially show the login frame
frame_login.grid()

# Function to switch to the main page after successful login
def switch_to_main_page():
    frame_login.grid_forget()  # Hide the login frame
    frame_main_page.grid(padx=300, pady=50)  # Show the main page frame

# Create main page frame
frame_main_page = tk.Frame(window, bg="light blue")
# Set the width and height of the login frame
frame_main_page.grid_propagate(0)
frame_main_page.configure(width=600, height=450)


# Set the width and height of the main page frame

# Create buttons in the main page
button1 = tk.Button(frame_main_page, text="Face expression detection", command=page1.show, font=("Italic", 18,"bold"),bg="light blue",padx=1, pady=10)
button1.grid(row=0, column=0, padx=160, pady=23)

button2 = tk.Button(frame_main_page, text="   Hand gesture detection   ", command=page2.show, font=("Italic", 18,"bold"),bg="light blue",padx=0, pady=10)
button2.grid(row=1, column=0, padx=160, pady=23)

button3 = tk.Button(frame_main_page, text="        Colour detection     ", command=page3.show,font=("Italic", 18,"bold"),bg="light blue",padx=0, pady=10)
button3.grid(row=2, column=0, padx=160, pady=23)

def switch_to_logout():
    frame_main_page.grid_forget()  # Hide the main page frame
    frame_login.grid( padx=350,pady=20)  # Show the login frame

# Create logout button in the main page
button_logout = tk.Button(frame_main_page, text="Logout", command=switch_to_logout, font=("Italic", 18,"bold"),bg="light blue",fg="dark blue")
button_logout.grid(row=3, column=0, padx=160, pady=23)

# Start the GUI event loop
window.geometry("1900x1900")
window.mainloop()
