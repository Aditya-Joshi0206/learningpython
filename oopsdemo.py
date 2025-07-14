#classes are user defined blueprint or prototype

#sum,multiplication, addition

#methods , class variable , instance variable

class Calculator:
    num=100

    def getdata(self):
        print("I am now using as method in class")

obj = Calculator()
obj.getdata()
print(obj.num)


