# PASSWORD STRENGTH CHECKER

print("I Suggest You, Please Don't Make simple password...")
print("Let's Guess How Strong Your Password Have..")
print("Please Use a Chapital, Small and Special Character, and number also")

password = input("Enter Your Password : ")
score = 0

if len(password) >= 8:
    score += 1

if len(password) == 0:
    print("Please Type Password")

if any(ch.isupper() for ch in password):
    score += 1

if any(ch.islower() for ch in password):
    score += 1

if any(ch.isdigit() for ch in password):
    score += 1

if any(not ch.isalnum() for ch in password):
    score += 1

# Now Count It...

if score <=0:
    print("Too Weak Passwod")
elif score <= 2:
    print("Weak Password")
elif score <= 3:
    print("Medium Password")
elif score <= 4:
    print("Strong Password")
else:
    print("Very Strong Password")
