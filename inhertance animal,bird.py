# Enter your code here
# multi-level inhertance
class Animal:
    def speak():
        return "animal is speaking "
class Bird(Animal):
    def speak():
        return "bird is speaking "
Animal_object1=Animal
bird_object2=Bird
print(Animal_object1.speak())
print(bird_object2.speak())
