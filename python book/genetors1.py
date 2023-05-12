#!python3

def simple_yield():
    print("First statement")
    yield
    print("Second statement")
    yield
    print("Third statement")

first_yield_test = simple_yield()
next(first_yield_test) # Runs to first yield statement
next(first_yield_test) # Runs to second yield statement
next(first_yield_test) # Tries to run to third yield statement

# Since there are no more yield statements, the Python script will
# generate a run-time error.  This means the following statement
# will not execute.
print("This statement will not print")


def increment():
    i = 0
    while True:   # Creates an infinite loop
        yield i       # returns the value of i and sets next start point
        i += 1

incrementor = increment()
print(next(incrementor))  # Runs to first yield statement
print(next(incrementor))  # Runs to second yield statement
print(next(incrementor))  # Runs to third yield statement

# next() may be called an infinite number of times


def increment():
    i = 0
    while True:   # Creates an infinite loop
        yield i       # returns the value of i and sets next start point
        i += 1

inc_one = increment()
inc_two = increment()
print("First incrementor generator")
print(next(inc_one))  # Runs to first yield statement
print(next(inc_one))  # Runs to second yield statement
print("Second incrementor generator")
print(next(inc_two))  # Runs to third yield statement


def fibonacci(first_value, second_value):
    while True:
        yield first_value
        temp = first_value # Temporarily stores first_value
        first_value = second_value # Since it will be overwritten here
        second_value = temp + second_value # Uses the stored temp value (first_value)

fib = fibonacci(0,1)

# Print the first 15 Fibonacci numbers

for i in range(0,15):
    print(next(fib),end=", ")


def fibonacci(first_value, second_value):
    while True:
        yield first_value
        first_value, second_value = second_value, first_value + second_value

fib = fibonacci(0,1)

# Print first 15 Fibonacci numbers

for i in range(0,15):
    print(next(fib),end=", ")


def my_range(initial_value, increment):
    i = initial_value
    while True:
        yield i
        i += increment

inc_one = my_range(0,1)
inc_two = my_range(0,5)

print("First generator:  ", end="")
for i in inc_one:
    if i > 10:
        break;
    else:
        print(i, end=", ")

print()
print("Second generator:  ", end="")
for i in inc_two:
    if i > 10:
        break;
    else:
        print(i, end=", ")



def my_range(initial_value, increment):
    i = initial_value
    while True:
        yield i
        i += increment

inc_one = my_range(0,1)
print(type(inc_one))





