from feedfinder2 import find_feeds

import tkinter
import tkinter.messagebox
import customtkinter

import os, sys

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RSS Checker")
        self.geometry(f"{1100}x{580}")

        path = customtkinter.filedialog.askopenfile().name
        self.check_feeds(path)

        path = customtkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt").name
        self.save(path)

    def check_feeds(self, path):
        with open(os.path.join(sys.path[0], "output.txt"), 'x') as output:
            for url in open(path, 'r'):
                if (find_feeds(url)):
                    print(url)
                    output.write(url)

    def save(self, path):
        os.replace(os.path.join(sys.path[0], "output.txt"), path)


if __name__ == "__main__":
    app = App()
    app.mainloop()
