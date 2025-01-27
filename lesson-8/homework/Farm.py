#so cool project, fr
#made some changes tho, for a better purposes
# Parent Class
class Animal:
    def __init__(self, name, species, age, country, cage_number):
        self.name = name
        self.species = species
        self.age = age
        self.country = country
        self.cage_number = cage_number

    def eat(self):
        print(f"{self.species} named {self.name} eats 6 times a day according to its own diet.")

    def sleep(self):
        print(f"{self.species} named {self.name} sleeps 10 hours a day.")

    def cage(self):
        return f"Cage #{self.cage_number}"


# Child Classes
class Zebra(Animal):
    def __init__(self, name, age, country, cage_number, stripe_count):
        super().__init__(name, "Zebra", age, country, cage_number)
        self.stripe_count = stripe_count

    def run(self):
        print(f"Zebra named {self.name} has {self.stripe_count} stripes!")


class Giraffe(Animal):
    def __init__(self, name, age, country, cage_number, neck_length):
        super().__init__(name, "Giraffe", age, country, cage_number,)
        self.neck_length = neck_length

    def reach_leaves(self):
        print(f"Giraffe named {self.name}'s neck is {self.neck_length}-meter-long.")


class Lion(Animal):
    def __init__(self, name, age, country, cage_number, mane_size):
        super().__init__(name, "Lion", age, country, cage_number)
        self.mane_size = mane_size

    def roar(self):
        print(f"Lion named {self.name} roars loudly, showing its {self.mane_size}-inch mane!")


class Panda(Animal):
    def __init__(self, name, age, country, cage_number, bamboo_eaten):
        super().__init__(name, "Panda", age, country, cage_number)
        self.bamboo_eaten = bamboo_eaten

    def roll_around(self):
        print(f"Panda named {self.name} rolls around after eating {self.bamboo_eaten} sticks of bamboo everyday.")


# Zoo Management Class
class ZooManagement:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []  # List of all animals in the zoo

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to {self.zoo_name}.")

    def list_animals(self):
        if not self.animals:
            print(f"{self.zoo_name} has no animals yet.")
        else:
            print(f"Animals in {self.zoo_name}:")
            for animal in self.animals:
                print(f"  - {animal.name} the {animal.species} (Cage: {animal.cage()}, From: {animal.country})")

    def locate_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                print(f"{animal.species} named {animal.name} is located in {animal.cage()}.")
                return
        print(f"No animal named {name} found in {self.zoo_name}.")

# Example Usage
def main():
    # Create a zoo
    zoo = ZooManagement("Toshkent Hayvonot Bogi")

    # Create animals
    zebra = Zebra(name="Martin", age=5, country="Africa", cage_number=34, stripe_count=80)
    giraffe = Giraffe(name="Melman", age=8, country="Africa", cage_number=39, neck_length=2)
    lion = Lion(name="Simba", age=7, country="Tailand", cage_number=67, mane_size=10)
    panda = Panda(name="Po", age=6, country="China", cage_number=24, bamboo_eaten=40)

    # Add animals to the zoo
    zoo.add_animal(zebra)
    zoo.add_animal(giraffe)
    zoo.add_animal(lion)
    zoo.add_animal(panda)

    print("\nListing all animals:")
    zoo.list_animals()

    print("\nLocating specific animals:")
    zoo.locate_animal("Martin")
    zoo.locate_animal("Simba")
    zoo.locate_animal("Dumbo")  # Non-existent animal


# Run the program
main()
