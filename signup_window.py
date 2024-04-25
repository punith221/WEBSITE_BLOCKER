import customtkinter as ctk
from PIL import Image
import db_operations


class SignupWindow(ctk.CTkToplevel):
    def __init__(self, master=None, geometry="800x600"):
        super().__init__(master)

        self.db_connection = db_operations.get_db_connection()

        self.geometry(geometry)
        self.resizable(False, False)

        self.bg_image = ctk.CTkImage(Image.open('login.png'), size=(800, 600))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_image_label.pack(padx=0, pady=0)

        self.signupFrame = ctk.CTkFrame(self, width=400, height=330, fg_color='white')
        self.signupFrame.place(x=200, y=110)

        self.signupHeading = ctk.CTkLabel(self.signupFrame, text='Sign-Up',
                                          font=('Helvetica', 60), text_color='#57a1f8')
        self.signupHeading.place(x=90, y=20)

        self.username = ctk.CTkEntry(self.signupFrame, width=300, height=50, fg_color='#57a1f8',
                                     font=('Microsoft YaHei UI Light', 11), text_color='white')
        self.username.place(x=50, y=110)
        self.username.insert(0, 'username')
        self.username.bind('<FocusIn>', self.on_enter)
        self.username.bind('<FocusOut>', self.on_leave)

        self.password = ctk.CTkEntry(self.signupFrame, width=300, height=50, fg_color='#57a1f8',
                                     font=('Microsoft YaHei UI Light', 11), text_color='white')
        self.password.place(x=50, y=180)
        self.password.insert(0, 'password')
        self.password.bind('<FocusIn>', self.on_enter)
        self.password.bind('<FocusOut>', self.on_leaveP)

        self.signup_button = ctk.CTkButton(self.signupFrame, width=100, height=50, text="sign-up", fg_color='#57a1f8',
                                           text_color='white', font=('Helvetica', 16),
                                           command=self.signup)
        self.signup_button.place(x=150, y=250)

    def signup(self):
        username = self.username.get()
        password = self.password.get()

        if not self.check(username):
            self.create(username, password)
            print("Signup successful")
        else:
            print("username not exists")

    def check(self, username):
        query = "SELECT * FROM user_data WHERE username= %s"
        values = (username,)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        res = cursor.fetchone()
        cursor.close()
        return res is not None

    def create(self, username, password):
        query = "INSERT INTO user_data (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        db_operations.close_db_connection(cursor, self.db_connection)

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
