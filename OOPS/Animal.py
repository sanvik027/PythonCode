class Animal:
    def eat(self):
        print("Animal can eat")
    def move(self):
        print("Animal can run")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


class Cat(Animal):
    def meow(self):
        print("cat can meow")

dog = Dog()
dog.bark()
dog.eat()
dog.move()

cat = Cat()
cat.meow()
cat.eat()
cat.move()