#!/usr/bin/python3
# deserttosea_surveyform.py by Dolu Obatusin
# This is an exercise to design a survey
'''
Survey Form Requirements: Part 1
1. It will display a logo and instructions to user.
2. It will have user input fields for:
    Name
    Email address
    Multiline comments
3. It will have two buttons: submit and clear
4. Pressing Submit will:
    Print contents of input fields to the console.
    Empty content of input field
    Notify the user that comments were submitted
5. Pressing Clear will:
    Empty the input fields
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        master.title("Explore California Feedback")
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('.', background = '#e1d8b9')
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Ariel', 18, 'bold'))



    # Add Top Frame
        self.topframe = ttk.Frame(master)
        self.topframe.pack()


        # Add logo, and text
        self.logo = PhotoImage(file  = '/Users/mosadoluwaobatusin/Documents/Projects/PythonGUIDevelopment/Ex_Files_Python_Tkinter/Exercise Files/Ch08/tour_logo.gif')
        ttk.Label(self.topframe, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.topframe, text = "Thanks for Exploring!", style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.topframe, wraplength = 300, style = 'TLabel',
                  text = ("We're glad you chose Explore California for your recent adventure."
                                       "Please tell us what you thought about the 'Deser to Sea' trip.")).grid(row = 1, column = 1)


        # Add Bottom Frame
        self.bottomframe = ttk.Frame(master)
        self.bottomframe.pack()

        # Add entry fields for name, email, comment
        ttk.Label(self.bottomframe, text = "Name:").grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        self.name = ttk.Entry(self.bottomframe, width = 24, font = ('Arial', 10))
        self.name.grid(row = 1, column = 0)

        ttk.Label(self.bottomframe, text = "Email:").grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        self.email = ttk.Entry(self.bottomframe, width = 24, font = ('Arial', 10))
        self.email.grid(row = 1, column = 1)

        ttk.Label(self.bottomframe, text = "Comment:").grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        self.comment = Text(self.bottomframe, width = 50, height = 10, font = ('Arial', 10))
        self.comment.grid(row = 3, column = 0, columnspan = 2)

        # Add clear button
        ttk.Button(self.bottomframe, text = "Clear" , command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')

        # Add submit button
        ttk.Button(self.bottomframe, text = "Submit", command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')



    def submit(self):
        """
        Print contents of input fields to the console.
        Empty content of input field
        Notify the user that comments were submitted
        """
        print("Name: {}".format(self.name.get()))
        print("Email: {}".format(self.email.get()))
        print("Comments: {}".format( self.comment.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Explore California Feedback',
                            message = "Comments Submitted")


    def clear(self):
        """
        Empty the input fields
        """
        self.name.delete(0, 'end')
        self.email.delete(0, 'end')
        self.comment.delete(1.0, 'end')


def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
