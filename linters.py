# analyze and evaluate code from pep8
# pass case?
# snake case ?

# Bad Code

# class myperson:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#     def GetName(self):
#         self.AskedForName = True
#         return self.name
# print(myperson("Mike",20,"m").GetName())

# Bad Code 0/10


##
# Implement Correct Naming Conventions
# class MyPerson:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.asked_for_name = False
#     def getname(self):
#         self.asked_for_name = True
#         return self.name
# print(MyPerson("Mike",20,"m").getname())

# 6/10


##
# Addng doc string and public methods
""" My perfect code example 

This should eventually get to 10/10 points.
"""
class MyPerson:
    """
    Person Class
    """
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.AskedForName = False # pylint: disable=invalid-name
    def get_name(self):
        """
        Returns the name of the person
        :return: the name
        """
        self.AskedForName = True
        return self.name
    def get_age(self):
        """
        Returns the age of the person
        :return: the age
            """
        return self.age
print(MyPerson("Mike", 20, "m").get_name())#10/10
