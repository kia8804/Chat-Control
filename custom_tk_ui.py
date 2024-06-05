from tkinter import *
from customtkinter import *
from PIL import Image # image processing

bot_name = "Chat Control"

# app = CTk()
# app.geometry("400x980")
# app.title("Chat Control")
# set_appearance_mode("dark")
# title_label = CTkLabel(app, text="Chat Control",font=CTkFont(family="Helvectica", size=25, weight='bold'))
# title_label.pack(padx=10, pady=(20,20))

class App():
    def __init__(self):
        self.app = CTk()
        self.app.geometry("400x980")
        self.app.title("Chat Control")
        self.title_label = CTkLabel(self.app, text="Chat Control",font=CTkFont(family="Helvectica", size=25, weight='bold'))
        self.title_label.pack(padx=10, pady=(20,20))
        self._setup_main_window()

    def send_message(self, event=None):
        msg1 = self.entry.get().strip()
        if msg1:
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"You: {msg1}\n")
            self.textbox.configure(state="disabled")
            self.textbox.see("end")
            self.entry.delete(0, "end")
            
            msg2 = "Hello! How may I assist you today?" # replace with chatbot output
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"CC: {msg2}\n")
            self.textbox.configure(state="disabled")
            self.textbox.see("end")

    def screenshot(self):
        # Not done yet
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"You sent a screenshot.\n")
        self.textbox.insert("end", "CC: Analyzing....\n") # replace with chatbot output
        self.textbox.configure(state="disabled")
        self.textbox.see("end")

    def _setup_main_window(self):
        self.send_icon = Image.open("airplane.png")
        self.btn = CTkButton(master=self.app, 
                        text="", 
                        hover_color="#4158D0", 
                        image=CTkImage(dark_image=self.send_icon, light_image=self.send_icon),
                        command=self.send_message)
        self.btn.place(relx=0.67, rely=0.90, relheight=0.06, relwidth=0.22)

        self.camera_icon = Image.open("camera.png")
        self.screenshot_btn = CTkButton(master=self.app, 
                                text="", 
                                hover_color="#4158D0", 
                                image=CTkImage(dark_image=self.camera_icon, light_image=self.camera_icon),
                                command=self.screenshot)

        self.screenshot_btn.place(relx=0.82, rely=0.90, relheight=0.06, relwidth=0.12,)


        self.entry = CTkEntry(master=self.app,
                        placeholder_text="Need help?",
                        width=300,
                        text_color="#FFFFFF")
        self.entry.place(relwidth=0.70, relheight=0.06, rely=0.90, relx=0.011)
        self.entry.bind("<Return>", self.send_message)
        # self.entry.focus_set()

        # textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16)
        self.textbox = CTkTextbox(master=self.app, scrollbar_button_color="#FFFFFF", corner_radius=16, state="disabled")
        self.textbox.place(relheight=0.80, relwidth=1, rely=0.10)

def create_app():
    app = App()
    set_appearance_mode("dark")
    app.app.mainloop()

if __name__ == "__main__":
    create_app()