from typing import Any

# الفئة الرئيسية: Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

# الفئة الفرعية الأولى: Mammal (ثدييات)
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def feed_milk(self):
        return f"{self.name} is feeding its young with milk."

# الفئة الفرعية الثانية: Bird (طيور)
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wing_span} meters."

# فئة متخصصة: Lion (أسد)
class Lion(Mammal):
    def __init__(self, name, age, fur_color, pride_size):
        super().__init__(name, age, fur_color)
        self.pride_size = pride_size

    def roar(self):
        return f"{self.name} is roaring loudly to protect its pride of {self.pride_size} members."

# فئة متخصصة: Parrot (ببغاء)
class Parrot(Bird):
    def __init__(self, name, age, wing_span, can_talk):
        super().__init__(name, age, wing_span)
        self.can_talk = can_talk

    def talk(self):
        if self.can_talk:
            return f"{self.name} is talking! It says 'Hello!'"
        else:
            return f"{self.name} cannot talk."

# استخدام الفئات
def main():
    # كائن من الفئة Mammal
    mammal = Mammal("Elephant", 10, "Gray")
    print(mammal.eat())  # Elephant is eating.
    print(mammal.feed_milk())  # Elephant is feeding its young with milk.

    # كائن من الفئة Bird
    bird = Bird("Eagle", 5, 2.5)
    print(bird.fly())  # Eagle is flying with a wingspan of 2.5 meters.

    # كائن من الفئة Lion
    lion = Lion("Simba", 7, "Golden", 15)
    print(lion.roar())  # Simba is roaring loudly to protect its pride of 15 members.

    # كائن من الفئة Parrot
    parrot = Parrot("Polly", 3, 0.5, True)
    print(parrot.talk())  # Polly is talking! It says 'Hello!'
    print(parrot.fly())  # Polly is flying with a wingspan of 0.5 meters.

if __name__ == "__main__":
    main()
