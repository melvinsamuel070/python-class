print ("please enter yuor details: ")
name = input("Enter your name: ")

print("Welcome " + name) 

if name ==():
    exit()
elif name == "samuel" or name == "big stan":
 print("correct name entry ""Saving.....")

else:
    print("yuor entry is incorrect ." "Not,Saved")  
    exit()

with open("store.txt", "a+") as f:
    f .write(name + "\n")

age = int(input("Enter your age: ")) 

if age <= 20:
    print("You are not qualified")
    exit()
elif age >= 20 and age <= 46:
    print("You are qualified")
    print("Save .......")  # Fixed typo in "save" to "Save"
    
else:
    print("You are not qualified")
    exit()

sex = input("Enter your sex: ")
print ("Saved .........")
with open("store.txt", "a+") as f:
    f .write(sex + "\n")

status = input("Enter yuor status: ")
print ("saved ........")
with open("store.txt", "a+") as f:
    f .write(status + "\n")

state =input("Enter yuor state: ")
print("saved .......")
with open("store.txt", "a+") as f:
    f .write(state + "\n")

occupation =input("Enter yuor occupation: ")
print ("saved ......")
with open("store.txt" "a+") as f:
    f .write(occupation + "\n")