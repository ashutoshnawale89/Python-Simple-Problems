#Write a Python program to search for a particular string in a file and replace it with another string.

search_value = input("Enter search value: ")
replace_value = input("Enter replace value: ")
result = ""
with open("test.txt","r") as file1:
    for i in file1:
        arr_value = i.split(" ")
        for j in arr_value:
            if search_value == j:
                result = result+" "+replace_value
            else:
                result = result +" "+ j

with open("test.txt","w") as file2:
    file2.write(result)
