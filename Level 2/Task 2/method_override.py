while True:  # Obtain user's input
    name = input("Input your name: ")
    age = int(input("Input your age: "))
    hair_colour = input("Input your hair colour: ")
    eye_colour = input("Input your eye colour: ")

    class Adult():  # Create Adult class
        def __init__(self, name, age, eye_colour, hair_colour):
            self.name = name
            self.age = age
            self.eye_colour = eye_colour
            self.hair_colour = hair_colour

        # Create a method to determine if the user is old enough to drive
        def can_drive(self):
                print(f"{self.name} is old enough to drive.")

    class Child(Adult):
        def can_drive(self):  # Override parent class "can drive" method
            print(f"{self.name} is too young to drive.")
    
    if age > 18:  # Determine if the user is an adult or a child
        person = Adult(name, age, eye_colour, hair_colour)
    else:
        person = Child(name, age, eye_colour, hair_colour)

    person.can_drive()  # Call the can drive method
