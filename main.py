new_file = open('New_File.txt','x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt","w")
my_file.write("Hi! I am Akshat and I am 13yrs old.")
my_file.close()

os.remove('Cdgl.txt')
os.rmdir('Example')