import customtkinter as ctk

class NpcFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        #widgets
        temp_label = ctk.CTkLabel(self, 
                                       text='NPC Frame')
        stats_frame = StatsFrame(self)
        generate_button = ctk.CTkButton(self, 
                                             text='Generate NPC',
                                             command=lambda: setHP(10))

        #packing
        temp_label.pack()
        stats_frame.pack(side='right', 
                              fill='y', 
                              padx=5, 
                              pady=5)
        generate_button.pack(side='bottom', 
                                  pady=10)
        
    def setHP(hp):
        stats_frame.setHP(hp)
        

class StatsFrame(ctk.CTkFrame):

    HP = 0

    def __init__(self, master):
        super().__init__(master)

        #widgets
        self.temp_label = ctk.CTkLabel(self, 
                           text='Stats Frame')
        self.temp_data_label = ctk.CTkLabel(self,
                                            text=f'HP: {self.HP}')

        #packing
        self.temp_label.pack()
        self.temp_data_label.pack()

    def setHP(self, hp):
        self.HP = hp
        self.temp_data_label.config(text=f'HP: {self.HP}')

    