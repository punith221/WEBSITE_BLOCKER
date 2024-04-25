from tkinter import *
import customtkinter as ctk
import login_window as LoginWindow
import signup_window as SignupWindow
from PIL import Image

ctk.set_appearance_mode("dark")


class MasterWindow(ctk.CTk):
    width = 900
    height = 600

    def __init__(self):
        super().__init__()
        self.title('Website Blocker')
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.bg_image = ctk.CTkImage(Image.open('login.png'), size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_image_label.pack(padx=0, pady=0)

        self.home_frame = ctk.CTkFrame(self.bg_image_label, width=625, height=180, corner_radius=10, fg_color='white', )
        self.home_frame.place(x=130, y=70)

        self.home_label = ctk.CTkLabel(self.home_frame, text='Website Blocker',
                                       font=('Helvetica', 75), text_color='#57a1f8')
        self.home_label.place(x=45, y=45)

        self.login_Button = ctk.CTkButton(self.bg_image_label, width=180, height=55, text="Login", fg_color='white',
                                          text_color='#2f6395', font=('Helvetica', 35), hover_color='#c1ecee',
                                          command=self.openLogin)
        self.login_Button.place(x=230, y=320)

        self.signup_Button = ctk.CTkButton(self.bg_image_label, width=180, height=55, text="Sign-up", fg_color='white',
                                           text_color='#2f6395', font=('Helvetica', 35), hover_color='#c1ecee',
                                           command=self.openSignup)
        self.signup_Button.place(x=480, y=320)

        self.Login_window = None
        self.su_window = None

    def openLogin(self):

        if self.su_window:
            self.su_window.destroy()

        if not self.Login_window or not self.Login_window.winfo_exists():
            self.Login_window = LoginWindow.LoginWindow(self)
        else:
            self.Login_window.focus()

    def openSignup(self):

        if self.Login_window:
            self.Login_window.destroy()
        if not self.su_window or not self.su_window.winfo_exists():
            self.su_window = SignupWindow.SignupWindow(self)
        else:
            self.su_window.focus()


if __name__ == "__main__":
    app = MasterWindow()
    app.mainloop()
