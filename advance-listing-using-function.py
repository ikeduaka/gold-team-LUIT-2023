# list of files and files content in the Dictionary

my_working_directory = {
  "file1" : {
    "name" : "Ec2",
    "size" : "1.5gb"
  },
  "file2" : {
    "name" : "error logs",
    "size" : "3.4gb"
  },
  "file3" : {
    "name" : "system check",
    "size" : "1.2gb"
  }
}

x = input("file content: " )    # input file name to get file content as output

file1 = { "name" : "Ec2",  "size" : "1.5gb"}
file2 = { "name" : "error logs",  "size" : "3.4gb"}
file3 = { "name" : "system check",  "size" : "1.2gb"}

if x == "file1":
    print(file1)
elif x == "file2":
    print(file2)
elif x == "file3":
    print(file3)
# if content not in file it defaults to the entire dictionary list
else:                    
    print(my_working_directory)
