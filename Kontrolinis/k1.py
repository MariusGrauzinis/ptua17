from typing import Dict, List, Union


def display_tasks(tasks: Dict[str, Union[str, bool]]) -> None:  #raktų ir reikšmių rinkinys {key: value}, Bool ( True false reiksmes)
    if not tasks:
        print("No tasks to display.")
    else:
         for index, task in enumerate(tasks):   # enumirate pereina per sarasa, ir grazina kiekvienosu uzduoties indeksa
            status = "[✔]" if task["done"] else "[ ]" #tikriname, ar užduoties done reikšmė yra True (atlikta) ar False (neatlikta).
            print(f"{index + 1}. {task['task']} {status}") #kad numeracija prasidėtų nuo 1 (vietoje 0).

def add_task(tasks: Dict[str, Union[str, bool]]) -> None:
    task_desc = input("Enter the task description: ")
    tasks.append({"task": task_desc, "done": False}) #sukuriam zodyna kad priskirti prie raktu task, ir pridedada zodyna prie saraso
    print(f"Task '{task_desc}' added.")

def mark_task_completed(tasks: Dict[str, Union[str, bool]]) -> None: # tikrina, ar vartotojo įvestas indeksas yra galiojantis, t. y. ar jis yra nuo 0 iki užduočių sąrašo ilgio minus vienas (indeksavimas prasideda nuo 0).
    display_tasks(tasks)
    while True:
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1 #Kadangi sąrašai yra indeksuojami nuo 0, o vartotojas įveda numerį, prasidedantį nuo 1 (pvz., 1, 2, 3…), mes mažiname įvestą numerį 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True #Kai vartotojas įveda galiojantį užduoties numerį, funkcija atnaujina šią užduotį, nustatydama jos done reikšmę kaip True, taip pažymėdama užduotį kaip atliktą.
                print(f"Task '{tasks[task_index]['task']}' marked as completed.")
                break   #Baigiame ciklą, kai užduotis pažymėta
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:    #Jei vartotojas įveda kažką, kas nėra skaičius (pvz., raidę arba specialų simbolį), atsiranda klaida
            print("Please enter a valid number.")

def remove_task(tasks: Dict[str, Union[str, bool]]) -> None:
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index) #jei indeksas teisingas, užduotis pašalinama iš sąrašo naudojant pop metodą, ir ją išsaugome kintamajame pašalinta_uzduotis.
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks:  List[Dict[str, Union[str, bool]]]  = [] # Inicijuojamas tuščias sąrašas, kuriame bus saugomos užduotys.
    while True:   #2.Nuolatinė kilpa, kuri leis vartotojui nuolat pasirinkti veiksmus, kol jis nuspręs išeiti.
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
