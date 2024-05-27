class Animal:
    name = None
    age = None

    def __init__(self):  # konstruktor
        self.name = "John"
        self.age = 2

    def print_details(self):
        print(f"Name: {self.name}, age: {self.age}")
        #print(f"NAME: {self.NAME}, AGE: {self.AGE}")


my_dog = Animal()
my_dog.print_details()
print(my_dog.name)
print(my_dog.age)

my_dog.name = "Alík"
my_dog.age = 5
my_dog.print_details()

my_cat = Animal()
my_cat.name = "Kitty"
my_cat.age = 3
my_cat.print_details()


class Animal:
    name = None
    age = None

    def __init__(self, name="Rex", age=2):  # konstruktor
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}, age: {self.age}")


my_parrot = Animal("Ara", 3)
my_parrot.print_details()

my_turtle = Animal("Leonardo", 15)
my_turtle.print_details()
my_turtle.age = -15
my_turtle.print_details()
my_turtle.age = "patnáct"
my_turtle.print_details()


# protected fields
class Animal():
    def __init__(self, name="Rex", age=2):
        self._name = name
        self._age = age


my_dog = Animal()
print(my_dog._name)
my_dog._name = "Alík"
print(my_dog._name)


# private fields
class Animal():
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age


my_dog = Animal()
#print(my_dog.__name)  # Error: AttributeError: 'Animal' object has no attribute '__name'
# my_dog.__age = 3
# print(my_dog.__age)


# Private fields - object status update
class Animal():
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return f"age: {self.__age}"

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater then 0.")


my_dog = Animal()
print(my_dog.get_name())
my_dog.set_name("Alík")
print(my_dog.get_name())
my_dog.set_age(-15)
print(my_dog.get_age())


# Properties - getter, setter
class Animal:
    # pokud chci private atributy, tak je nesmím definovat zde, ale jen v konsgtruktoru
    #__name = ""
    #__age = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return f"age: {self.__age}"

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter
    def age(self):
        print("Deleting age property")
        del self.__age


my_dog = Animal('Alík', 11)
my_dog.age = 3
print(my_dog.age)
del my_dog.age
#print(my_dog.age)  # AttributeError: 'Animal' object has no attribute '_Animal__age'.

#my_dog.__name = "Zoro"
#print(my_dog.__name)


# TODO: vytvořte třídu Person, která bude obsahovat atributy:
# - name
# - surname
# - tel_number
# - email
# všechny atributy budou private a bude k nim přístup pomocí properties

class Person:
    def __init__(self, name=None, surname=None, tel_number=None, email=None):
        self.__name = name
        self.__surname = surname
        self.__tel_number = tel_number
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def tel_number(self):
        return self.__tel_number

    @tel_number.setter
    def tel_number(self, tel_number):
        my_tel_number = str(tel_number).replace(" ", "")
        if len(my_tel_number) == 9:
            # TODO: ošetřit, zda jsou jen číslice
            self.__tel_number = "+420"+my_tel_number
        elif len(my_tel_number) == 13:
            # TODO: ošetřit, zda je '+' a pak jen číslice
            self.__tel_number = my_tel_number
        else:
            print(f"Incorrect telephone number: '{my_tel_number}'")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        correct_at = False
        correct_dot = False
        for ch in email:
            if ch == '@' and correct_at:  # pokud najdu druhý zavináč
                correct_at = False
            elif ch == '@' and not correct_at:  # našel jsem první zavináč
                correct_at = True
            if correct_at and ch == '.':
                correct_dot = True
        if correct_at and correct_dot:
            self.__email = email
        else:
            print(f"Incorrect email: '{email}'")

    def __str__(self):
        return (f"Name: {self.__name}, surname={self.__surname}, "
                f"tel_number: {self.__tel_number}, email: {self.__email}")


john = Person(name='John',
              surname='Smith',
              tel_number=777123456,
              email="john.smith@gmail.com")

john.tel_number = "777 55 456"
john.email = "john@smith@gmail.com"
john.email = "@."  # FIXME: toto zatím projde, je potřeba lépe ošetřit
print(john)


# Value and reference
class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


dog_a = Animal()
dog_b = dog_a  # toto nevytvoří kopii objektu, ale jen referenci na stávající objekt
print(f"dog_a.name: {dog_a.name}, dog_b.name: {dog_b.name}")
dog_a.name = "Pongo"
print(f"dog_a.name: {dog_a.name}, dog_b.name: {dog_b.name}")
dog_b.name = "Alík"
print(f"dog_a.name: {dog_a.name}, dog_b.name: {dog_b.name}")


# Inheritance
class Programmer(Person):
    def __init__(self, name=None, surname=None, tel_number=None, email=None, languages=[]):
        super().__init__(name, surname, tel_number, email)  # vytvoříme objekt třídy Person
        self.__languages = languages

    def __str__(self):
        return (f"{self.name} {self.surname}, "
                f"tel: {self.tel_number}, "
                f"email: {self.email}, "
                f"languages: {self.__languages}")

    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, languages):
        self.__languages = languages

    def add_language(self, language):
        self.__languages.append(language)


bob = Programmer("Bob", "Smith", 777123456, "bob@smith.com", ['Python'])
print(bob)
bob.add_language('Java')
print(bob)


class Student(Person):
    def __init__(self, name=None, surname=None, tel_number=None, email=None, school=None):
        super().__init__(name, surname, tel_number, email)
        self.__school = school

    def __str__(self):
        return (f"{self.name} {self.surname}, "
                f"tel: {self.tel_number}, "
                f"email: {self.email}, "
                f"school: {self.__school}")

    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school):
        if len(school) > 2:
            self.__school = school
        else:
            print(f"Incorrect school name: '{school}'")


student1 = Student("Martin",
                   "Novák",
                   777159753,
                   "martin@novak.cz",
                   "MUNI")

print(student1)
student1.email = "martin.novak@mail.muni.cz"
student1.tel_number = "+420 777 555 888"
student1.school = "MUNI FI"
print(student1)


class StudentProgrammer(Student, Programmer):
    def __init__(self, name, surname, tel_number, email, school, languages):
        super().__init__(name, surname, tel_number, email, school)
        self.languages = languages

    def __str__(self):
        return (f"{self.name} {self.surname}, "
                f"tel: {self.tel_number}, "
                f"email: {self.email}, "
                f"school: {self.school}, "
                f"languages: {self.languages}")


student_programmer = StudentProgrammer("Franta",
                                       "Novák",
                                       777888999,
                                       "franta@novak.cz",
                                       "VUT",
                                       ["Python", "Java"])

print(student_programmer)
student_programmer.add_language("C#")
print(student_programmer)
