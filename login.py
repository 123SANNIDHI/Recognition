import tkinter as tk
import sqlite3

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database
    connection = sqlite3.connect("reg.db")
    cursor = connection.cursor()

    # Check if the username and password match
    query = "SELECT * FROM user WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result is not None:
        label_status.config(text="Login Successful", fg="green")
    else:
        label_status.config(text="Invalid username or password", fg="red")

    # Close the database connection
    cursor.close()
    connection.close()
def open_registration_form():
    registration_window = tk.Toplevel(window)
    registration_window.title("Registration")

    # Create username label and entry in registration form
    label_username_reg = tk.Label(registration_window, text="Username:")
    label_username_reg.pack()
    entry_username_reg = tk.Entry(registration_window)
    entry_username_reg.pack()

    # Create email label and entry in registration form
    label_email = tk.Label(registration_window, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(registration_window)
    entry_email.pack()

    # Create password label and entry in registration form
    label_password = tk.Label(registration_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.pack()

    # Create confirm password label and entry in registration form
    label_confirm_password = tk.Label(registration_window, text="Confirm Password:")
    label_confirm_password.pack()
    entry_confirm_password = tk.Entry(registration_window, show="*")
    entry_confirm_password.pack()

    # Create registration button in registration form
    button_register = tk.Button(registration_window, text="Register", command=lambda: register(registration_window, entry_username_reg.get(), entry_email.get(), entry_password.get(), entry_confirm_password.get()))
    button_register.pack()

    # Create status label for displaying registration status in registration form
    label_status = tk.Label(registration_window, text="")
    label_status.pack()

def register(registration_window, username, email, password, confirm_password):
    # Connect to the database
    connection = sqlite3.connect("reg.db")
    cursor = connection.cursor()

    # Check if the username already exists
    query = "SELECT * FROM user WHERE username=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result is not None:
        label_status.config(text="Username already exists", fg="red")
    else:
        # Check if the email is already registered
        query = "SELECT * FROM user WHERE email=?"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result is not None:
            label_status.config(text="Email already registered", fg="red")
        elif password != confirm_password:
            label_status.config(text="Passwords do not match", fg="red")
        else:
            # Insert new user into the database
            insert_query = "INSERT INTO user (username, email, password) VALUES (?, ?, ?)"
            cursor.execute(insert_query, (username, email, password))
            connection.commit()
            label_status.config(text="Registration Successful", fg="green")

    # Close the database connection
    cursor.close()
    connection.close()

    # Close the registration window
    registration_window.destroy()

# Create the main window
window = tk.Tk()
window.title("User Login")

# Create username label and entry in the main window
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Create password label and entry in the main window
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create login button in the main window
button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

# Create register button in the main window
button_register = tk.Button(window, text="Register", command=open_registration_form)
button_register.pack()

# Create status label for displaying login status in the main window
label_status = tk.Label(window, text="")
label_status.pack()

# Start the GUI event loop
window.geometry("1024x1984")
window.mainloop()
