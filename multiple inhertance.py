# Enter your code here
# multiple inhertance
class father:
    def father_method():
        return "this is father method "
class mother:
    def mother_method():
        return "this is mother method "
class child(father,mother):
    def child_method():
        return "this is child method"
parent_object1=father
parent_object2=mother
child_object=child
print(parent_object1.father_method())
print(parent_object2.mother_method())
print(child_object.child_method())
print(child_object.father_method())
print(child_object.mother_method())

