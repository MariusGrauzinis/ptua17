from my_functions import get_cat_image, save_image_to_disk
from requests.exceptions import ConnectionError

cats_directory = "my_cats/"
print("Welcome to Cat image generator")

c = 0
while True:
    print("If you wish to generate a new file of cat press 1")
    user_input = input("Enter your choice:   ")
    if user_input == "1":
        cat_image = get_cat_image()
        if cat_image:
            c += 1
            save_image_to_disk(cat_image, f"{cats_directory}{c}")
        else:
            print("Woopsie our awesome cat image generator is broken...")
    else:
        break

print("Program is terminating...")