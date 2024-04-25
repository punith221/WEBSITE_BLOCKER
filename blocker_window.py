import customtkinter as ctk
from PIL import Image
import blocker
from datetime import datetime
import pytz


class BlockerWindow(ctk.CTkToplevel):
    def __init__(self, master=None, geometry="800x600"):
        super().__init__(master)

        self.geometry(geometry)
        self.resizable(False, False)

        self.bg_image = ctk.CTkImage(Image.open('login.png'), size=(800, 600))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_image_label.pack(padx=0, pady=0)

        self.home_frame = ctk.CTkFrame(self.bg_image_label, width=550, height=150, fg_color='white')
        self.home_frame.place(x=120, y=70)

        self.home_label = ctk.CTkLabel(self.home_frame, text='Website Blocker',
                                       font=('Helvetica', 62), text_color='#57a1f8')
        self.home_label.place(x=45, y=43)

        self.label1 = ctk.CTkLabel(self, text='Website url:', font=('Helvetica', 19),
                                   fg_color='#2f6395', corner_radius=4, bg_color='#57a1f8',
                                   width=50, height=47, text_color='white')
        self.label1.place(x=130, y=270)

        self.enter_Website = ctk.CTkEntry(self, placeholder_text="Enter url here ...", height=47,
                                          placeholder_text_color='#57a1f8',
                                          width=340,
                                          border_width=0, corner_radius=4, bg_color='#57a1f8',
                                          fg_color='white', text_color='#57a1f8', font=('Helvetica', 19))
        self.enter_Website.place(x=310, y=270)

        self.block_btn = ctk.CTkButton(self, width=130, height=30, text="Block", fg_color='white',
                                       text_color='#2f6395', font=('Helvetica', 31), hover_color='#c1ecee',
                                       command=self.block_action)

        self.block_btn.place(x=200, y=350)

        self.unBlock_btn = ctk.CTkButton(self, width=130, height=30, text="UnBlock", fg_color='white',
                                         text_color='#2f6395', font=('Helvetica', 31), hover_color='#c1ecee',
                                         command=self.unblock_action)

        self.unBlock_btn.place(x=400, y=350)

    def block_action(self):
        curr_datetime = datetime.utcnow()
        timezone = pytz.timezone('Asia/Kolkata')
        curr_datetime_timezone = curr_datetime.astimezone(timezone)
        urls = self.enter_Website.get()
        b = blocker.Blocker(urls)
        b.block(curr_datetime_timezone)
        self.display_label("Blocked 👍👍👍")

    def unblock_action(self):
        urls = self.enter_Website.get()
        b = blocker.Blocker(urls)
        b.unblock()
        self.display_label("UnBlocked all websites👍")

    def display_label(self, msg):
        label = ctk.CTkLabel(self, text=msg, font=('Helvetica', 19),
                             fg_color='white', corner_radius=4, bg_color='#57a1f8',
                             width=50, height=47, text_color='black')
        label.place(x=300, y=430)
        self.update()

        self.after(2000, label.destroy())
