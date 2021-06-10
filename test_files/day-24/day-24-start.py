# with open("my_file.txt") as file:
# 	contents = file.read()
# print(contents)

# r = read (only reads the file)
# content = file.read()

# a = append (adds a entry in the file)
# file.write("\nhello")

# w = writes (overwrites everything in the file)
# file.write("\nhello")

# if you use the `with open("file.txt", mode=a) as file:
# and the file.txt doesnt actually exist, it will create it for you.


with open("D:\SCHOOL\python_learning_projects\Python_Playground\test_files\day-24") as file:
	contents = file.read()
	print(contents)
