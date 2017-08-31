#array
student_list = ["mohit", "pawan", "saurabh"]
student_list.append("Himanshu")
"mohit" in student_list == True
del student_list[3]
print(len(student_list));

#for loop
for name in student_list:
    print("name is {0}".format(name));
#range function will have Range(10)

#Dictionary in Python
student={
    "name":"mohit",
    "age":32,
    "nullvalues":None
}

#to print values
print(student.get("name"));

#to print keys
print(student.keys())

#to print values
print(student.values());

# Exception handling
try:
    last_name=student["lastname"];
except Exception:
    print("There is no such key");

print("Hello world")
number=5;
decimalnumber=5.5;
print(number+decimalnumber);
nondecimal=int(decimalnumber)
print(nondecimal)
name="mohit";
greet="hello";
messge="hey , say {1} to {0}".format(name,greet);
print(messge);





#if condition
num=10;
if num==10:
    print("number is 10")
else:
    print("number is not 10");