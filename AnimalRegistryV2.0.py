class Animal:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        if self.commands:
            print(f"{self.name} knows the following commands:")
            for command in self.commands:
                print("-", command)
        else:
            print(f"{self.name} doesn't know any commands yet.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class Hamster(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

class Horse(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class Donkey(Animal):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

class PetRegistry:
    def __init__(self):
        self.animals = []

    def get_new_animal(self):
        animal_type = input("Enter the type of animal (Dog, Cat, Hamster, Horse, Donkey): ")
        name = input("Enter the name of the animal: ")
        if animal_type == "Dog":
            breed = input("Enter the breed of the dog: ")
            animal = Dog(name, breed)
        elif animal_type == "Cat":
            color = input("Enter the color of the cat: ")
            animal = Cat(name, color)
        elif animal_type == "Hamster":
            fur_color = input("Enter the fur color of the hamster: ")
            animal = Hamster(name, fur_color)
        elif animal_type == "Horse":
            color = input("Enter the color of the horse: ")
            animal = Horse(name, color)
        elif animal_type == "Donkey":
            size = input("Enter the size of the donkey: ")
            animal = Donkey(name, size)
        else:
            print("Invalid animal type.")
            return
        self.animals.append(animal)
        print(f"{animal_type} named {name} added to the registry.")

    def assign_animal_to_class(self):
        name = input("Enter the name of the animal you want to assign: ")
        for animal in self.animals:
            if animal.name == name:
                animal.list_commands()
                return
        print("Animal not found in the registry.")

    def teach_new_command(self):
        name = input("Enter the name of the animal you want to teach a new command: ")
        for animal in self.animals:
            if animal.name == name:
                command = input("Enter the new command: ")
                animal.add_command(command)
                print(f"New command '{command}' added to {name}.")
                return
        print("Animal not found in the registry.")

    def menu(self):
        while True:
            print("\n--- Pet Registry Menu ---")
            print("1. Get a new animal")
            print("2. Assign an animal to the correct class")
            print("3. See the list of commands an animal performs")
            print("4. Teach the animal a new command")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.get_new_animal()
            elif choice == "2":
                self.assign_animal_to_class()
            elif choice == "3":
                self.list_commands()
            elif choice == "4":
                self.teach_new_command()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    registry = PetRegistry()
    registry.menu()