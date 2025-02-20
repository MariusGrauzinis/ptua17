
import logging
import math

logging.basicConfig(
    filename="functions_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
def sum_of_numbers(*args):
    try:
        total = sum(args)
        logging.info(f"The sum of numbers {args} is: {total}")
        return total
    except Exception as e:
        logging.exception(f"Error while calculating sum: {e}")
    
def square_root(number):
    try:
        result = math.sqrt(number)
        logging.info(f"The square root of {number} is: {result}")
        return result
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")

def count_charakters(sentence):
    char_count = len(sentence)
    logging.info(f"The number of characters in sentence: {char_count}")
    return char_count
def devide_numbers(x, y):
    try:
        result = x/ y
        logging.info(f"The division of {x} and {y} gives {result}")
        return result
    except ZeroDivisionError:
        logging.exception(
            f"Error: Division by zero is not allowed. Cannot divide {x} by {y}."
        )
        return "Error: Division by zero is not allowed."


print(sum_of_numbers(10, 20, 30))
print(square_root(16))
print(count_charakters("Hello my name is Marius"))
print(devide_numbers(8, 5))