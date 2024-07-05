# daily_reminder.py

def main():
    # Prompt for task description
    task = input("Enter your task: ")

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Provide a customized reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Modify reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.")
        return

    # Print the reminder
    print("Reminder:", reminder)

# Run the main function
if __name__ == "__main__":
    main()
