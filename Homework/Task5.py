num: int = int (input ("Please enter a number "));
if num %5 == 0 and num %3 == 0:
    print ("Fizz Buzz");
elif num %5 == 0:
    print ("Fizz")
elif num %3 == 0:
    print ("Buzz")
else:
    print ("This number is not divided by 5 or 3");