import os
from dotenv import load_dotenv
import customtkinter as ctk
from openai import OpenAI
import requests
import shutil
from PIL import Image
from threading import Thread

class WeatherGenerator(ctk.CTkFrame):  # Weather generator class
    def __init__(self, master):  # Initializer
        super().__init__(master)

        load_dotenv()  # Load environment variables from .env file
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

        self.weather_description = ""
        self.weather_image_url = ""

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Button to generate weather
        self.generate_button = ctk.CTkButton(
            self, text="Generate Weather", command=self.start_generation
        )
        self.generate_button.grid(row=0, column=0, columnspan=2, pady=10)

        self.description_label = ctk.CTkLabel(self, text="Weather Description:")
        self.description_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.description_textbox = ctk.CTkTextbox(self, width=400, height=100, wrap="word")
        self.description_textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.description_textbox.configure(state="disabled")

        self.image_canvas = ctk.CTkLabel(self, text="")  # Placeholder for the image
        self.image_canvas.grid(row=4, column=0, columnspan=2, pady=10)

    def start_generation(self):
        # Disable the button while generating
        self.generate_button.configure(state="disabled")
        self.description_textbox.configure(state="normal")
        self.description_textbox.delete("1.0", "end")
        self.description_textbox.insert("1.0", "Generating weather...")
        self.description_textbox.configure(state="disabled")
        generate_thread = Thread(target=self.generate)
        generate_thread.start()    

    def generate(self):
        description = self.generate_weather_description()
        image_url = self.generate_weather_image(description)
        self.update_image(image_url)
        self.update_description(description)
        self.generate_button.configure(state="normal")

    def generate_weather_description(self):
        try:
            prompt = "Generate a short simple description for dnd weather. only the description. make it not based on location."
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a weather forecaster."},
                    {"role": "user", "content": prompt},
                ],
            )
            self.weather_description = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating weather description: {e}")
            self.weather_description = "Unable to generate weather description."
        return self.weather_description

    def generate_weather_image(self, description: str):
        try:
            prompt = f"Create a basic image of the following weather: {description}"
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size='1024x1024',
                quality="standard",
                n=1,
            )
            self.weather_image_url = response.data[0].url
        except Exception as e:
            print(f"Error generating weather image: {e}")
            self.weather_image_url = ""
        return self.weather_image_url

    def update_description(self, description: str):
        self.description_textbox.configure(state="normal")
        self.description_textbox.delete("1.0", "end")
        self.description_textbox.insert("1.0", description)
        self.description_textbox.configure(state="disabled")

    def update_image(self, image_url: str):
        if image_url:
            try:
                url = image_url
                file_name = 'weather_image.png'

                res = requests.get(url, stream = True)

                if res.status_code == 200:
                    with open(file_name,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                else:
                    print("Image Couldn't be retrieved")

                image = ctk.CTkImage(dark_image=Image.open("weather_image.png"), size=(380, 380))
                self.image_canvas.configure(image=image, text="")
                
            except Exception as e:
                print(f"Error loading image: {e}")
                self.image_canvas.configure(text="Unable to load image.")
        else:
            self.image_canvas.configure(text="No image available.")