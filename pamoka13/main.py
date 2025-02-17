# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="data.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


import logging

first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))


try:
    c = first_number / second_number
    print(f"First number divided by second is: {c}")
except ZeroDivisionError as e:
    logging.exception("Exception occured!")

print("I am still runnig, no problem at all")