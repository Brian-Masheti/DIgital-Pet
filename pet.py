# Python OOP Challenge: Digital Pet
# Defines the Pet class with attributes and methods for a virtual pet

class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name          # Pet's name (string)
        self.hunger = 5           # Hunger level (0 = full, 10 = very hungry)
        self.energy = 5           # Energy level (0 = tired, 10 = fully rested)
        self.happiness = 5        # Happiness level (0 = sad, 10 = very happy)
        self.tricks = []          # List to store learned tricks (bonus)

    # Method to feed the pet
    def eat(self):
        self.hunger -= 3          # Reduce hunger by 3
        if self.hunger < 0:       # Ensure hunger doesn't go below 0
            self.hunger = 0
        self.happiness += 1       # Increase happiness by 1
        if self.happiness > 10:   # Ensure happiness doesn't exceed 10
            self.happiness = 10
        return f"{self.name} eats some food! Yum! 😋"

    # Method to let the pet sleep
    def sleep(self):
        self.energy += 5          # Increase energy by 5
        if self.energy > 10:      # Ensure energy doesn't exceed 10
            self.energy = 10
        return f"{self.name} takes a nap. Zzz... 😴"

    # Method to play with the pet
    def play(self):
        self.energy -= 2          # Decrease energy by 2
        if self.energy < 0:       # Ensure energy doesn't go below 0
            self.energy = 0
        self.happiness += 2       # Increase happiness by 2
        if self.happiness > 10:   # Ensure happiness doesn't exceed 10
            self.happiness = 10
        self.hunger += 1          # Increase hunger by 1
        if self.hunger > 10:      # Ensure hunger doesn't exceed 10
            self.hunger = 10
        return f"{self.name} plays happily! Woof! 🎉"

    # Method to display the pet's current status
    def get_status(self):
        return (f"{self.name}'s Status:\n"
                f"Hunger: {self.hunger}/10\n"
                f"Energy: {self.energy}/10\n"
                f"Happiness: {self.happiness}/10")

    # Bonus: Method to train the pet a new trick
    def train(self, trick):
        self.tricks.append(trick)  # Add trick to the list
        self.happiness += 1       # Increase happiness for learning
        if self.happiness > 10:   # Ensure happiness doesn't exceed 10
            self.happiness = 10
        return f"{self.name} learned to {trick}! Good pet! 🐶"

    # Bonus: Method to show all learned tricks
    def show_tricks(self):
        if not self.tricks:       # Check if the tricks list is empty
            return f"{self.name} hasn't learned any tricks yet."
        tricks_list = ", ".join(self.tricks)  # Join tricks into a string
        return f"{self.name}'s tricks: {tricks_list}"
    
