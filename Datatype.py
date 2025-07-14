
#List is  data type that allows multiple values and can be different data type

values=[1,2,"Aditya", 4, 5.5]
print(values[0])
print(values[2])
print(values[4])
#to print last index
print(values[-1])

#print value for indexing
print(values[1:3])

values.insert(3,"Joshi")
print(values)

#insert values in end
values.append("End")
print(values)
#updating values
values[2]="ADITYA"
print(values)

#del values from list

del values[0]
print(values)

#tuple

val = (1,2,"Aditya", 4,5)
print(val[2])

#dictonary

dict= {"a":2, 4:"Aditya", "abc": "Joshi"}
print(dict["abc"])


dic = {}
dic ["firstname"]= "Aditya"
dic ["lastname"]= "Joshi"
dic ["gender"] ="Male"

print(dic)
print(dic["lastname"])
