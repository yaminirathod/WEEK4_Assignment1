# Import tk interface libraries
from tkinter import *
from tkinter import messagebox

def reverseOrderName():

    # Define a class
    class myCalculator:

        def __init__(self):
            # Setup TK interface window
            self.window = Tk()
            self.window.title("My Calculator")
            self.window.geometry("500x400")

            # Define frames to arrange the layout
            self.top_frame = Frame()
            self.bottom_frame = Frame()
            self.result_frame = Frame()

            # Define the top frame with welcome message and user input
            self.welcome_label1 = Label(self.top_frame, text="Welcome to Reverse Name Program")
            self.welcome_label2 = Label(self.top_frame, text="Designed By: Yamini Rathod C0796390")

            self.prompt_label1 = Label(self.top_frame, text="Please enter the first name : ")
            self.fname = Entry(self.top_frame)

            self.prompt_label2 = Label(self.top_frame, text="Please enter the last name : ")
            self.lname = Entry(self.top_frame)

            # Define the frame for buttons
            self.calc_buttom1 = Button(self.bottom_frame, text="Get Reverse", padx=10, command=self.rev)
            self.cancel_button = Button(self.bottom_frame, text="Exit", padx=10, command=self.window.destroy)

            # Define frame to display the result
            self.result = StringVar()
            self.result.set("Result: N/A")
            self.result_label = Label(self.result_frame, textvariable=self.result, bg="yellow", fg="green")

            # Pack the frames together and apply padding to make layout more readable
            self.welcome_label1.pack(padx=10, pady=10)
            self.welcome_label2.pack(padx=10, pady=10)
            self.prompt_label1.pack(padx=10, pady=10)
            self.fname.pack(padx=10, pady=10)
            self.prompt_label2.pack(padx=10, pady=10)
            self.lname.pack(padx=10, pady=10)

            # Pack the buttons
            self.calc_buttom1.pack(side="left", padx=10, pady=10)
            self.cancel_button.pack(side="left", padx=10, pady=10)
            self.result_label.pack(side="left", padx=10, pady=10)

            # Pack all the frames
            self.top_frame.pack()
            self.bottom_frame.pack()
            self.result_frame.pack()

            mainloop()

        # Function to reverse the order
        def rev(self):
            try:
                firstname = self.fname.get()
                lastname = self.lname.get()

                self.result.set(f'The reverse output is : {lastname} {firstname}')
            except:
                messagebox.showerror("Input Error", "The input is invalid! Please try again!")

    myWindow = myCalculator()