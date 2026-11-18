import random

# Tool 1: Interactive To-Do List
# Allows users to view, add, and remove tasks from a dynamic list.
def todo_list_tool():
    tasks = ["Buy groceries", "Finish Python project"]
    while True:
        print("\n--- Interactive To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print(f"'{new_task}' has been added successfully!")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    rem_index = int(input("Enter the number of the task to remove: ")) - 1
                    if 0 <= rem_index < len(tasks):
                        removed = tasks.pop(rem_index)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid integer.")
        elif choice == "4":
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please pick between 1 and 4.")

# Tool 2: Number Guessing Game
# Challenges the user to guess a secret number between 1 and 10 with feedback loops.
def guessing_game_tool():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the secret number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Tool 3: Simple Tip Calculator
# Calculates bill totals, tips, and split amounts based on input parameters.
def tip_calculator_tool():
    print("\n--- Simple Tip Calculator ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter number of people splitting the bill: "))
        
        if bill < 0 or tip_percent < 0 or people <= 0:
            print("Values must be greater than zero.")
            return
            
        tip_amount = bill * (tip_percent / 100)
        total_bill = bill + tip_amount
        per_person = total_bill / people
        
        print(f"\n--- Bill Summary ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill: ${total_bill:.2f}")
        print(f"Amount Per Person: ${per_person:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Main Program Loop
def main():
    print("🌟 Welcome to Your Personal Mini-Toolkit! 🌟")
    
    while True:
        print("\n==============================")
        print("          MAIN MENU           ")
        print("==============================")
        print("1. Interactive To-Do List")
        print("2. Number Guessing Game")
        print("3. Simple Tip Calculator")
        print("4. Quit")
        print("==============================")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            todo_list_tool()
        elif choice == "2":
            guessing_game_tool()
        elif choice == "3":
            tip_calculator_tool()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please select a valid option between 1 and 4.")

if __name__ == "__main__":
    main()