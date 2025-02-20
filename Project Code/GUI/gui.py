import customtkinter as ctk
from LeftFrame.left_frame import LeftFrame
from RightFrame.right_frame import RightFrame

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('600x400')

        self.left_frame = LeftFrame(self)
        self.right_frame = RightFrame(self)

        self.left_frame.pack(side='left', fill='y', padx=5)
        self.right_frame.pack(side='right', fill='both', expand=True, padx=5)

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()