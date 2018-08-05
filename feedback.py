from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText


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

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')


    def submit(self):
        email='timbo.timberman@gmail.com'
        password='mydgfnpanqmfydhf'
        email2= self.entry_email.get()
        name=self.entry_name.get()

        subject="Feedback from " + self.entry_name.get()
        message= self.text_comments.get(1.0, 'end')

        subject2="Feedback"
        message2= "Dear {},<br/><br/>We received your feedback. Thank you for staying in touch.<br/><br/>Best regards, Administration<br/>".format(name)

        msg=MIMEText(message, 'html')
        msg['Subject']=subject
        msg['To']=email
        msg['From']=email2

        msg2=MIMEText(message2, 'html')
        msg2['Subject']=subject2
        msg2['To']=email2
        msg2['From']=email

        try:
            gmail=smtplib.SMTP('smtp.gmail.com',587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(email, password)
            gmail.send_message(msg)
            gmail.send_message(msg2)
            gmail.close()
            self.clear()
            messagebox.showinfo(title = 'Feedback', message = 'You feedack was successfuly sent!')
        except:
            messagebox.showinfo(title = 'Feedback', message = 'Something went wrong!')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
