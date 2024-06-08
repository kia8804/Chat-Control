from tkinter import *
from customtkinter import *
from PIL import Image # image processing
import mss
from openai import OpenAI
# import base64
# # import key
import sim_keys
from main import take_screenshot, encode_image_to_base64, send_image_to_gpt4o


bot_name = "Chat Control"
key = "42"

class App():
    def __init__(self):
        self.app = CTk()
        self.app.geometry("400x980")
        self.app.title("Chat Control")
        self.title_label = CTkLabel(self.app, text="Chat Control",font=CTkFont(family="Helvectica", size=25, weight='bold'))
        self.title_label.pack(padx=10, pady=(20,20))
        self._setup_main_window()
        
        self.client = OpenAI(api_key=key)
        self.messages = [
            {
                "role": "system",
                "content": """Give me a list of key presses, one key per line to do this. 
                If you need to use 2 keys simultaneously/holding 2 down at the same time put them on the same line (like "ctrl a")
                Don't use the shift key. List all your key commands after a line with the text.""",
            }
        ]
        self.image_path = ""
        self.screenshot_taken = False

    def ask_bot(self, question):
        # Sends user input to gpt chatbot and gets back input
        # Screenshots user excel sheet (or just main display) to aid output relevancy
        if not self.screenshot_taken:
            self.image_path = take_screenshot()
            self.screenshot_taken = True
        base64_image = encode_image_to_base64(self.image_path)

        # For exiting chat screen.
        sim_keys.multi_key_press("alt tab")
        self.messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
                ],
            }
        )

        response = send_image_to_gpt4o(self.client, self.messages)
        self.screenshot_taken = False
        if response.choices:
            output = response.choices[-1].message.content
            print("API Response:", output)
            sim_keys.multi_key_press(output)
            return output
        return "Sorry, could not process message."

    def send_message(self, event=None):
        msg1 = self.entry.get().strip()
        if msg1:
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"You: {msg1}\n")
            self.textbox.configure(state="disabled")
            self.textbox.see("end")
            self.entry.delete(0, "end")
            
            # msg2 = "Hello! How may I assist you today?" # replace with chatbot output
            msg2 = self.ask_bot(msg1)
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"CC: {msg2}\n")
            self.textbox.configure(state="disabled")
            self.textbox.see("end")

    def screenshot(self):
        # Not done yet
        self.image_path = take_screenshot() 
        self.screenshot_taken = True
        
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"You sent a screenshot.\n")
        self.textbox.insert("end", "You can type what you need help with or press the button again for a new screenshot.\n") 
        self.textbox.configure(state="disabled")
        self.textbox.see("end")

    def _setup_main_window(self):
        try:
            self.send_icon = Image.open("airplane.png")
        except:
            self.send_icon = Image.open("InQubate-Hackathon/airplane.png")
        self.btn = CTkButton(master=self.app, 
                        text="", 
                        hover_color="#4158D0", 
                        image=CTkImage(dark_image=self.send_icon, light_image=self.send_icon),
                        command=self.send_message)
        self.btn.place(relx=0.67, rely=0.90, relheight=0.06, relwidth=0.22)

        
        try:
            self.camera_icon = Image.open("camera.png")
        except:
            self.camera_icon = Image.open("InQubate-Hackathon/camera.png")
        
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
        self.textbox = CTkTextbox(master=self.app, scrollbar_button_color="#FFFFFF", corner_radius=16, state="normal")
        self.textbox.place(relheight=0.80, relwidth=1, rely=0.10)
        # self.textbox.configure(state="normal")
        self.textbox.insert("end", f"CC: {'How may I assist you today?'}\n")
        self.textbox.configure(state="disabled")
        self.textbox.see("end")
        
def create_app():
    app = App()
    set_appearance_mode("dark")
    app.app.mainloop()

if __name__ == "__main__":
    create_app()