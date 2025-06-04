# Enter your code here
# multiple inhertance
class grandfather:
    def grandfather_method():
        return "this is  grandfather method "
class father(grandfather):
    def father_method():
        return "this is father method "
class child(father):
    def child_method():
        return "this is child method"
parent_object1=grandfather
parent_object2=father
child_object=child
print(parent_object1.grandfather_method())
print(parent_object2.father_method())
print(child_object.child_method())
print(parent_object2.grandfather_method())
print(child_object.father_method())

