print ("First user details:")
user_id1: str = input ("Please enter your User ID: ");
first_name1: str = input ("Please enter your First name: ");
last_name1: str = input ("Please enter your Last name: ");
height1: float = float (input ("Please enter your Height: "));
year_of_birth1: int = int (input ("Please enter your year of birth: "));


print ("Second user details:")
user_id2: str = input ("Please enter your User ID: ");
first_name2: str = input ("Please enter your First name: ");
last_name2: str = input ("Please enter your Last name: ");
height2: float = float (input ("Please enter your Height: "));
year_of_birth2: int = int (input ("Please enter your year of birth: "));

print ("Third user details:")
user_id3: str = input ("Please enter your User ID: ");
first_name3: str = input ("Please enter your First name: ");
last_name3: str = input ("Please enter your Last name: ");
height3: float = float (input ("Please enter your Height: "));
year_of_birth3: int = int (input ("Please enter your year of birth: "));






print(f"{user_id1:<10} {last_name1:<10.10} {first_name1:<10.10} {height1:<10.2f} {year_of_birth1:<10}")
print(f"{user_id2:<10} {last_name2:<10.10} {first_name2:<10.10} {height2:<10.2f} {year_of_birth2:<10}")
print(f"{user_id3:<10} {last_name3:<10.10} {first_name3:<10.10} {height3:<10.2f} {year_of_birth3:<10}")