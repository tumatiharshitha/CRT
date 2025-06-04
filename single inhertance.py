# Enter your code here
# single inhertance
class father:
    def father_method():
        return "this is father method "
class child(father):
    def child_method():
        return "this is child method"
parent_object=father
child_object=child
print(parent_object.father_method())
print(child_object.child_method())
print(child_object.father_method())
