#this is to print the name 
print("This is to print the name")
user_name=input("Enter your name :" )
user_sex=input("Enter your sex :" )
if user_sex == ('m' or 'M' or "male" or "MALE"):
    print("Hello Mr: ",user_name)
else:
    print("Hello Miss: ",user_name)