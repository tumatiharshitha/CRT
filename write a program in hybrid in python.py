# Enter your code here
# multi-level inhertance
class grandfather:
    def grandfather_method():
        return "this is  grandfather method "
class father(grandfather):
    def father_method():
        return "this is father method "
class mother(grandfather):
    def mother_method():
        return "this is mother method "
class child(father,mother,grandfather):
    def child_method():
        return "this is child method"
parent_object1=grandfather
parent_object2=father
parent_object3=mother
child_object=child
print(parent_object1.grandfather_method())
print(parent_object2.father_method())
print(parent_object2.grandfather_method())
print(parent_object3.mother_method())
print(child_object.child_method())
print(child_object.father_method())
print(child_object.mother_method())

