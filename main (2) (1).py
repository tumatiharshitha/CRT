class student_data:
    def _init_(self,name,rool,age,branch,cgpa):
        self.name=name
        self.roll=roll
        self.age=age
        self.branch=branch
        self.cgpa=cgpa
        self.marks_btech=marks_btech
        self.marks_10th=marks_10th
        self.marks_inter=marks_inter
    def display(name,roll,age,branch,cgpa):
        return f"name :{name} roll_number : {roll} age={age} branch={branch} cgpa={cgpa}"
    def grade(cgpa):
        if(cgpa>9.5):
            return "excellent"
        elif(cgpa>7 and cgpa<9):
            return"good"
        elif(cgpa>6 and cgpa<7):
            return"average"
    def check_placements(marks_10th,marks_inter,mar_btech):
        if(marks_10th>60 and marks_btech>60 and marks_inter>60):
            return "you are eligible for placement"
        else:
            return "you are not eligible for placement"
creating object
student_1=student_data
student_2=student_data
student_3=student_data
print(student_1.display("umesh",20,21,"civil",7.0))
print(student_1.check_placements(70,77,80))
