def print_hello():
    print("Hello Madhu Chandra")
print_hello()

def print_input_name(name):
    print("Hi, " + name)
print_input_name("Madhu Chandra")

def print_fn_ln(fn, ln):
    print(fn, ln)
print_fn_ln(fn="Madhu", ln="Chandra")

def details(name, age, dob):
    print(name, age, dob)
details(name="Madhu Chandra", age="33", dob="11th May 1986")

def sum(a, b, c):
    print(a+b+c)
sum(1, 2, 3)

def returnsum(a, b, c, d, e):
    return (a+b+c+d+e)
x = returnsum(1, 2, 3, 4, 5)
print(x)