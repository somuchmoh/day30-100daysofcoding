# Catching exceptions on FileNotFoundError
try:
    file = open("a_file.txt")
    new_dict = {"key": "value"}
    print(new_dict["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", mode='w')
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file is closed")


# Raising own exceptions
try:
    file = open("a_file.txt")
    new_dict = {"key": "value"}
    print(new_dict["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", mode='w')
    file.write("Something")
else:
    content = file.read()
    print(content)
# finally:
        # raise KeyError


# When would you want to raise your own exception?
height = int(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height cannot be more than 3 meters")

bmi = weight / height ** 2
print(bmi)
