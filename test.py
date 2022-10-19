import unittest
import io
import sys
from unittest.mock import patch

from people import Person
from people import Faculty
from people import Student


class Test01_Person(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** FUNCTION CALL: x = Person('Stephen','May') *** EXPECT: x.firstname+':'+x.lastname == 'Stephen:May' ***
        """
        x = Person('Stephen','May')
        self.assertEqual('Stephen:May', x.firstname+':'+x.lastname)
        print()

class Test02_Faculty(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') *** EXPECT: x.firstname+':'+x.lastname+':'+x.department == 'Stephen:May:Computer Science' ***
        """
        x = Faculty('Stephen','May','Computer Science')
        self.assertEqual('Stephen:May:Computer Science', x.firstname+':'+x.lastname+':'+x.department)
        print()

class Test03_FacultyInheritsPerson(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') *** EXPECT: isinstance(x, Person) == True ***
        """
        x = Faculty('Stephen','May','Computer Science')
        self.assertEqual(True, isinstance(x, Person))
        print()

class Test04_FacultyInheritsStudent(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') *** EXPECT: isinstance(x, Student) == False ***
        """
        x = Faculty('Stephen','May','Computer Science')
        self.assertEqual(False, isinstance(x, Student))
        print()

class Test05_Student(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') THEN y = Student('Mickey','Mouse') THEN y.set_class('Freshman') THEN y.set_major('Electrical Engineering') THEN y.set_advisor(x) *** EXPECT: y.firstname+':'+y.lastname+':'+y.classyear+':'+y.major+':'+y.advisor.firstname+':'+y.advisor.lastname == 'Mickey:Mouse:Freshman:Electrical Engineering:Stephen:May' ***
        """
        x = Faculty('Stephen','May','Computer Science')
        y = Student('Mickey','Mouse')
        y.set_class('Freshman')
        y.set_major('Electrical Engineering')
        y.set_advisor(x)
        self.assertEqual('Mickey:Mouse:Freshman:Electrical Engineering:Stephen:May', y.firstname+':'+y.lastname+':'+y.classyear+':'+y.major+':'+y.advisor.firstname+':'+y.advisor.lastname)
        print()

class Test06_StudentInheritsPerson(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') THEN y = Student('Mickey','Mouse') THEN y.set_class('Freshman') THEN y.set_major('Electrical Engineering') THEN y.set_advisor(x) *** EXPECT: isinstance(y, Person) == True ***
        """
        x = Faculty('Stephen','May','Computer Science')
        y = Student('Mickey','Mouse')
        y.set_class('Freshman')
        y.set_major('Electrical Engineering')
        y.set_advisor(x)
        self.assertEqual(True, isinstance(y, Person))
        print()

class Test07_StudentInheritsFaculty(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 *** FUNCTION CALL: x = Faculty('Stephen','May','Computer Science') THEN y = Student('Mickey','Mouse') THEN y.set_class('Freshman') THEN y.set_major('Electrical Engineering') THEN y.set_advisor(x) *** EXPECT: isinstance(y, Faculty) == False ***
        """
        x = Faculty('Stephen','May','Computer Science')
        y = Student('Mickey','Mouse')
        y.set_class('Freshman')
        y.set_major('Electrical Engineering')
        y.set_advisor(x)
        self.assertEqual(False, isinstance(y, Faculty))
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
