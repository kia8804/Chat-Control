from tkinter import *
# from tkinter.ttk import *

test_response = "Response successful!"

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

bot_name = "Chat Control"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=250, height=450)
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat Control")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(
            self.window, 
            bg=BG_COLOR, 
            fg=TEXT_COLOR, 
            text="Welcome to Chat Control!", 
            font=FONT_BOLD, 
            pady=10
        )  
        head_label.place(relwidth=1) # label should take whole width of parent window
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widgit
        self.text_widget = Text(
            self.window, 
            width=20, 
            height=2, 
            bg=BG_COLOR, 
            fg=TEXT_COLOR,
            font=FONT, 
            padx=5, 
            pady=5
        )
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget) # inherits all size attributes from text widgit
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825) 
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus() # start typing by default
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        self.photoicon = PhotoImage(file=r"airplane.png").subsample(10, 10)
        send_button = Button(
            bottom_label, 
            # text="Send", 
            image=self.photoicon,
            compound=LEFT,
            font=FONT_BOLD, 
            width=20, 
            bg=BG_GRAY,
            command=lambda: self._on_enter_pressed(None)
        )
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get() # gets string representation of current text
        self._insert_message(msg, "You")
   
    def _insert_message(self, msg, sender):
        if not msg:
            return # no text message
        
        self.msg_entry.delete(0, END) # clears message box
        msg1 = f"{sender}: {msg}\n"   
        self.text_widget.configure(cursor="arrow", state=NORMAL) # temporarily allow text input (our text)
        self.text_widget.insert(END, msg1)  
        self.text_widget.configure(cursor="arrow", state=DISABLED) # temporarily allow text input (our text)
    
        msg2 = f"{bot_name}: Successfully processed message.\n"   
        self.text_widget.configure(cursor="arrow", state=NORMAL) # temporarily allow text input (our text)
        self.text_widget.insert(END, msg2)  
        self.text_widget.configure(cursor="arrow", state=DISABLED) # temporarily allow text input (our text)

        self.text_widget.see(END) # scroll to the end


if __name__ == "__main__":
    app = ChatApplication()
    app.run()