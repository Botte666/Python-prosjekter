# Python program to implement the FizzBuzz problem
for i in range(1, 101):
 # Numbers that are divisible by 3 and 5
 # are always divisible by 15
 # Therefore, "FizzBuzz" is printed in place of that number
 if (i%15 == 0):
    print("FizzBuzz")
 # "Fizz" is printed in place of numbers
 # that are divisible by 3
 elif (i%3 == 0):
    print("Fizz")
 # "Buzz" is printed in place of numbers
 # that are divisible by 5
 elif(i%5 == 0):
    print("Buzz")
 # If none of the above conditions are satisfied,
 # the number is printed
 else:
    print(i)