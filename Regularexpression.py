# Python function to validate the resular expression of the following :
#Email Address
#Mobile number - Bangladesh
#Telephone number of USA
#16 character Alpha - numeric password composed of alphabets - upper case , lower case , special character and numbers
import re
 
# compiling the pattern for alphanumeric string
patemail = re.compile(r"^[A-Za-z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}")
patebangladeshnumber=re.compile(r"^(?:\+88|88)?(01[3-9]\d{8})$")
patUSAnumber=re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
patpassword=re.compile(r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*[A-Z])(?=.*[-\#\$\.\%\&\*])(?=.*[a-zA-Z]).{8,16}$")

 
# Prompts the user for input string
testemail = input("Enter the email: ")

 
# Checks whether the whole string matches the re.pattern or not
if re.fullmatch(patemail, testemail):
    print(f"'{testemail}' is a valid Email")

else:
    print(f"'{testemail}' is NOT a valid Email")

#Promts the user for input number
testbangladeshnumber = input("Enter Bangladesh Number: ")
 
# Checks whether the whole string matches the re.pattern or not
if re.fullmatch(patebangladeshnumber, testbangladeshnumber):
    print(f"'{testbangladeshnumber}' is a valid Number")
else:
    print(f"'{testbangladeshnumber}' is NOT a valid Number")

#Promts the user for input number
testUSAnumber = input("Enter USA Number: ")
 
# Checks whether the whole string matches the re.pattern or not
if re.fullmatch(patUSAnumber, testUSAnumber):
    print(f"'{testUSAnumber}' is a valid Number")
else:
    print(f"'{testUSAnumber}' is NOT a valid Number")

#Promts the user for input number
testpassword = input("Enter USA Number: ")
 
# Checks whether the whole string matches the re.pattern or not
if re.fullmatch(patpassword, testpassword):
    print(f"'{testpassword}' is a valid Number")
else:
    print(f"'{testpassword}' is NOT a valid Number")