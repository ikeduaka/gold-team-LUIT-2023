my_working_directory1 = {
  "file1" : {
    "name" : "Ec2",
    "size" : "1.5gb"
  },
  "file2" : {
    "name" : "error logs",
    "size" : "1.2mb"
  },
  "file3" : {
    "name" : "system check",
    "size" : "5.9mb"
  }
}

my_working_directory2 = {
  "file4" : {
    "name" : "Storage",
    "size" : "5.5gb"
  },
  "file5" : {
    "name" : "system logs",
    "size" : "2.5gb"
  },
  "file6" : {
    "name" : "system check",
    "size" : "10.9mb"
  }
}
print(my_working_directory1)
print(my_working_directory2)

for x in my_working_directory1:
  print(my_working_directory1[x])
for x in my_working_directory2:
  print(my_working_directory2[x])

