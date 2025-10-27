File = open("TestFIle.txt")

line = File.readline()

for line in File.readlines():
    print(line)

#while line != "":
 #   print(line)
  #  line = File.readline()



File.close()