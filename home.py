import tkinter as tk
import page1
import page2
import page3

window = tk.Tk()
window.title("User Login")

frame_logout = tk.Frame(window)
def navigate_to_page1():
    page1.show()
def navigate_to_page2():
    page2.show()

def navigate_to_page3():
    page3.show()


# Create buttons
button1 = tk.Button(frame_logout, text="Face expression detection", command=navigate_to_page1, padx=70, pady=20)
button1.pack(padx=70, pady=20)
    

button2 = tk.Button(frame_logout, text="Hand gesture detection", command=navigate_to_page2, padx=70, pady=20)
button2.pack(padx=70, pady=20)

button3 = tk.Button(frame_logout, text="Colour detection", command=navigate_to_page3, padx=70, pady=20)
button3.pack(padx=70, pady=20)

button4 = tk.Button(frame_logout, text="Logout",  padx=10, pady=20)
button4.pack(padx=300, pady=20)
frame_logout.bind("<Button-1>", lambda e:frame_login())


frame_logout.pack()
# Start the GUI event loop
window.geometry("1024x1984")
window.mainloop()
