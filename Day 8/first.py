#class & object
# class Student:

    #default constructors
    # def __init__(self):
    #     pass

    #paeameterized constructoers
#     def __init__(self, fullname):
#         self.name = fullname
#         print("creating new student in database..")

# s1 = Student("karan")
# print(s1.name)

# s2 = Student("arjun")
# print(s2.name)


# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


#methods

class Student:
    college_name = "ABC Collage"
    # paeameterized constructoers
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name) 

    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
s1.welcome()
print(s1.get_marks())