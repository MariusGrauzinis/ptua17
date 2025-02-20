
import logging

logging.basicConfig(
    filename="input_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
while True:
        user_input = input("Enter something (or 'end' to quit): ")
        
        if user_input.lower() == "end":
            print("Goodbye!")
            break

        logging.info(f"User input: {user_input}")
