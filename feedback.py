from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage



class Feedback:

    def __init__(self, master):

        self.background = '#76C2AF'
        master.title('Feedback')
        master.resizable(False, False)
        master.configure(background = self.background)

        self.style = ttk.Style()
        self.style.configure('TFrame', background = self.background)
        self.style.configure('TButton', background = self.background)
        self.style.configure('TLabel', background = self.background, font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'computer.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Welcome!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 200,
                  text = (" This is a simple app to get user's feedback.\n Type your message below and we will reach you back soon.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Password:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_password = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

        self.entry_email.grid(row = 1, column = 0, padx = 5)
        self.entry_password.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')


    def submit(self):
        print('Email: {}'.format(self.entry_email.get()))
        print('Password: {}'.format(self.entry_password.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        # msg = EmailMessage()
        # msg['Subject'] = 'Feedback'
        # msg['From'] = self.entry_email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(self.entry_email.get(), self.entry_password.get())
        server.sendmail(self.entry_email.get(), "timbo.timberman@gmail.com", self.text_comments)
        server.send_message(self.text_comments)
        server.quit()
        self.clear()
        messagebox.showinfo(title = 'Feedback', message = 'Comments Submitted!')


    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
