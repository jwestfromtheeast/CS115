'''
Created on Apr 12, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
# A class is a blueprint for an object that you wish to model.
# Classes have attributes, or properties, that describe the state
# of your object. The constructor __init__ is a special method whose
# purpose is to initialize the fields of the class. When you call the
# constructor of a class, it creates an object value. This process
# is called instantiation.
import sys

# Some common errors:
# ValueError, TypeError, ZeroDivisionError, IndexError, KeyError, IOError

class Student(object):
    def __init__(self, first_name, last_name, sid, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid
        self.__gpa = float(gpa)
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    
    @property
    def sid(self):
        return self.__sid
    
    @sid.setter
    def sid(self, sid):
        self.__sid = sid
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, gpa):
        try:
            local_gpa = float(gpa)
        except:
            raise TypeError("GPA must be a float.")
        if local_gpa < 0.0 or local_gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0.")
        self.__gpa = local_gpa
        
    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ' (SID: ' + \
            self.__sid + ', GPA: ' + str(self.__gpa) + ')'
        
if __name__ == '__main__':
    s = Student('Tim', 'Yost', '12345', 5.6)
    print(s.first_name)
    print(s.last_name)
    print(s.sid)
    print(s.gpa)
    s.gpa = 3.9
    print(s)
    try:
        t = Student("Bart", "Simpson", "12346", "3.0")
    except (TypeError, ValueError) as error:
        print("Error: ", error)
        sys.exit(1)
    try:
        t.gpa = input("Enter new GPA for " + t.first_name + ": ")
    except (TypeError, ValueError) as error:
        print("Error: ", error)
        sys.exit(1)
    sys.exit(0)