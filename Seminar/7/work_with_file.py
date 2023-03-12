path = "file.txt"

"""file = open(path, "r", encoding = "UTF-8")
#data = file.read()
#data = file.readline()
data = file.readlines()
print(data)
file.close()


#или так

with open(path, "r", encoding = "UTF-8") as file:
    data = file.readlines()
print(data)"""



with open(path, "w", encoding = "UTF-8") as file:
    file.write("Это боле новая строка")