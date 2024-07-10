# First exercise
num_slices:int= int(input("Please enter the number of slices: "))
x:int=int(num_slices/4)
y:int=int(num_slices%4)

if num_slices<1 :
    print("Please enter the correct number of slices!")
elif y==0:
    print(f"Danny's friends got {x} slices, and there are no slices left!")
else:
    print(f"Danny's friends got {x} slices, and {y} slices left!")


# Second exercise

slices_num:int= int(input("Please enter the number of slices: "))
num_friends:int= int(input("Please enter the number of friends: "))

x:int=int(slices_num/num_friends)
y:int=int(slices_num%num_friends)

if (slices_num<1) :
    print("Please enter the correct number of slices!")
elif (num_friends<1):
    print("Please enter the correct number of friends!")
elif (y==0):
    print(f"Danny's friends got {x} slices, and there are no slices left!")
else:
    print(f"Danny's friends got {x} slices, and {y} slices left!")