
import customtkinter as ctk
from PIL import Image

from blocker_window import BlockerWindow
import db_operations


class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master=None, geometry="800x600"):
        super().__init__(master)

        self.db_connection = db_operations.get_db_connection()

        self.geometry(geometry)
        self.resizable(False, False)

        self.bg_image = ctk.CTkImage(Image.open('login.png'), size=(800, 600))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_image_label.pack(padx=0, pady=0)

        self.loginFrame = ctk.CTkFrame(self, width=400, height=350, fg_color='white')
        self.loginFrame.place(x=200, y=110)

        self.loginHeading = ctk.CTkLabel(self.loginFrame, text='Login',
                                         font=('Helvetica', 75), text_color='#57a1f8')
        self.loginHeading.place(x=110, y=20)

        self.username = ctk.CTkEntry(self.loginFrame, width=300, height=50, fg_color='#57a1f8',
                                     font=('Helvetica', 11), text_color='white')
        self.username.place(x=50, y=130)
        self.username.insert(0, 'username')
        self.username.bind('<FocusIn>', self.on_enter)
        self.username.bind('<FocusOut>', self.on_leave)

        self.password = ctk.CTkEntry(self.loginFrame, width=300, height=50, fg_color='#57a1f8',
                                     font=('Helvetica', 11), text_color='white')
        self.password.place(x=50, y=200)
        self.password.insert(0, 'password')
        self.password.bind('<FocusIn>', self.on_enter)
        self.password.bind('<FocusOut>', self.on_leaveP)

        self.login_button = ctk.CTkButton(self.loginFrame, width=100, height=50, text="Login", fg_color='#57a1f8',
                                          text_color='white', font=('Helvetica', 16),
                                          command=self.login)
        self.login_button.place(x=150, y=270)
        self.bw = None

    @staticmethod
    def on_enter(e):
        widget = e.widget
        widget.delete(0, 'end')

    @staticmethod
    def on_leave(e):
        widget = e.widget
        name = widget.get()
        if name == '':
            widget.insert(0, 'Username')

    @staticmethod
    def on_leaveP(e):
        widget = e.widget
        passw = widget.get()
        if passw == '':
            widget.insert(0, 'Password')

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if self.check_credentials(username, password):
            self.destroy()
            bw = BlockerWindow(self.master)
            bw.mainloop()
            print("username and password are correct")
            self.destroy()
        else:
            print("username or password is invalid!")

    def check_credentials(self, username, password):
        query = """ SELECT username, password FROM user_data where username = %s and password = %s """
        values = (username, password)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        res = cursor.fetchone()
        db_operations.close_db_connection(cursor, self.db_connection)
        return res is not None
