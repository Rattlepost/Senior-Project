from openai import OpenAI
import os
from dotenv import load_dotenv


class NPCGenerator:
    def __init__(self):  # Initializer
        self.healthPoints = 0
        self.name = ""
        self.race = ""
        self.class_ = ""
        self.alignment = ""
        self.description = ""

        load_dotenv()  # Load environment variables from .env file
        api_key = os.getenv("OPENAI_API_KEY")

        self.client = OpenAI(api_key=api_key)

    def generate_health(self):  # Generate a random health point value between 15 and 70
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": "a random number between 15 and 70. only the number",
                    },
                ],
            )
            self.healthPoints = response.choices[0].message.content.strip()
        except Exception as e:
            print("Error:" + {e})

    def generate_name(
        self,
    ):  # Generate a random name using OpenAI based on the class and alignment
        try:
            prompt = f"""
                Generate a name for a DnD NPC based on this info: 
                {self.name}, {self.class_}, {self.alignment}. 
                Dont make the name too over-fantasized. 
                Only the name and no other text.
                """
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            self.name = response.choices[0].message.content.strip()
        except Exception as e:
            print("Error:" + {e})

    def generate_race(self):  # Generates a random race using OpenAI based on the health points
        try:
            prompt = f"""
                Generate a race for the DnD NPC based off this info: 
                {self.healthPoints}. Only give the race and no other text.
                """
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            self.race = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {e}")

    def generate_class(self):  # Generates a random class using OpenAI from a list of classes and then chooses a subclass
        try:
            prompt = f"""
                Generate a class for the DnD NPC from the list: 
                Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk,
                Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard. 
                Then pick a subclass for that class. 
                Give only the class and subclass and no other text. 
                Use the format class - subclass"]
                """
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            self.class_ = response.choices[0].message.content.strip()
        except Exception as e:
            print("Error:" + {e})

    def generate_alignment(self):  # Generates a random alignment using OpenAI based on the class and race
        try:
            prompt = f"""
            Generate an alignment for the DnD NPC based off this info: 
            {self.class_}, {self.race}. 
            Only give the alignment and no other text
            """
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            self.alignment = response.choices[0].message.content.strip()
        except Exception as e:
            print("Error:" + {e})

    def generate_description(self): # Generates a description of the npc incorporating the name, class, alignment, and race
        try:
            prompt = f"Generate a short description for this NPC such as backstory. Do not add any additional text other than the backstory. Incorporate this information: {self.name}, {self.class_}, {self.alignment}, {self.race}"
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            self.description = response.choices[0].message.content.strip()
        except Exception as e:
            print("Error:" + {e})
