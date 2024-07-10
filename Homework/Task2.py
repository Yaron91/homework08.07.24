grade: int = int (input ("Please enter your score in the test "));
if grade > 100 or grade < 0:
    print("Illegal grade");
elif grade >= 96 and grade <= 100:
    print("Excellent!!! You're a Star!");
elif grade >= 81:
    print("Awesome!");
elif grade >= 61:
    print("Pretty good");
elif grade >= 41:
    print("You're getting there, need some more work");
else:
    print("Try harder next time");