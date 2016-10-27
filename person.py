import datetime

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setBirthday(self, birthDate):
        #assumes birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        #return True if self's name is lexicographically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name

me = Person('John Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print him
print him.getLastName()
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
#Big no no. Evil.
#him.birthday = '8/4/61'
print her.getAge()
print him.getAge()
print him < her
print me < her
pList = [me, him, her]
print 'The people in pList are:'
for p in pList:
   print '  ' + str(p)
pList.sort()
print 'The people in pList are:'
for p in pList:
   print '  ' + str(p)

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self)==UG or type(self)==G

p1 = MITPerson('Barbara Beaver')
print p1, p1.getIdNum()
p2 = MITPerson('Sue Yuan')
print p2, p2.getIdNum()
p3 = MITPerson('Sue Yuan')
print p3, p3.getIdNum()
p4 = Person('Sue Yuan')
print 'p1 < p2 =', p1 < p2
print 'p3 < p2 =', p3 < p2
print '_lt__(p1, p2) =', Person.__lt__(p1, p2)
print 'p1 == p4 =', p1 == p4
print 'p4 < p3 =', p4 < p3
#Won't work because p4 is a Person not an MITPerson and cannot compare to a non-existing id.
##print 'p3 < p4 =', p3 < p4
