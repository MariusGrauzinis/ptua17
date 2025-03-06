from typing import Dict, List, Union


def display_tasks(tasks: Dict[str, Union[str, bool]]) -> None:  
    if not tasks:
        print("No tasks to display.")
    else:
         for index, task in enumerate(tasks):   
            status = "[✔]" if task["done"] else "[ ]" 
            print(f"{index + 1}. {task['task']} {status}") 

def add_task(tasks: Dict[str, Union[str, bool]]) -> None:
    task_desc = input("Enter the task description: ")
    tasks.append({"task": task_desc, "done": False}) 
    print(f"Task '{task_desc}' added.")

def mark_task_completed(tasks: Dict[str, Union[str, bool]]) -> None: 
    display_tasks(tasks)
    while True:
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1 
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True 
                print(f"Task '{tasks[task_index]['task']}' marked as completed.")
                break   
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:    
            print("Please enter a valid number.")

def remove_task(tasks: Dict[str, Union[str, bool]]) -> None:
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index) 
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks:  List[Dict[str, Union[str, bool]]]  = [] 
    while True:  
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option (1-5): "))
            
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                print("Exiting the To-Do List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
