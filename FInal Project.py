"""
ICS3U Final Project Todolist by Alice Kim
"""

class Task:

    def __init__(self, name: str):
        self.name = name
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            situation = "Finally Done"
        else:
            situation = "Not even close"
        return self.name + " - " + situation

class Todolist:
    
    def __init__(self):
        self.tasks = [] 
    
    def add_task(self):
        name = input("Please enter a new task: ").strip()
        if name:
            new_task = Task(name)
            self.tasks.append(new_task)
            print(f"{name} has been added to the list.")
        else:
            print("Task name cannot by empty")
    
    def show_tasks(self):
        if self.tasks == []:
            print("No tasks! Do something before you become a failure")
        else:
            print("Your tasks:")
            for i in self.tasks:
                print(i)
    
    def mark_task_done(self):
        if self.tasks == []:
            print("No tasks!")
            return
    
        self.show_tasks()
        num = int(input("Which task number? "))
        self.tasks[num - 1].mark_done()
        print("Done!")
    
    def remove_task(self):
        if self.tasks == []:
            print("No tasks!")
            return
    
        self.show_tasks()
        num = int(input("Which task number? "))
        removed = self.tasks.pop(num - 1)
        print("Removed:", removed.name)    

def main():
    todo = Todolist()
    running = True 
  
    print("Alice's Cute TODOLIST dedicated to motivate her!!")
  
    while running:
        print("Menu:")
        print("1) Add task")
        print("2) View tasks")
        print("3) Mark task as done")
        print("4) Remove task")
        print("5) Quit")
        choice = input("Type something: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.mark_task_done()
        elif choice == "4":
            todo.remove_task()
        elif choice == "5":
            print("Bye^^ COME BACK WHEN YOU ARE READY")
            running = False 
        else:
            print("Invalid choice. Please enter a number from 1–5.") 
if __name__ == "__main__":
    main()
    
#Example Runs

# Example Run 1:
# Alice's Cute TODOLIST dedicated to motivate her!!
# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 1
# Please enter a new task: finish homework
# finish homework has been added to the list.

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 1
# Please enter a new task: clean room
# clean room has been added to the list.

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 2
# Your tasks:
# finish homework - Not even close
# clean room - Not even close

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 3
# Your tasks:
# finish homework - Not even close
# clean room - Not even close
# Which task number? 1
# Done!

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 2
# Your tasks:
# finish homework - Finally Done
# clean room - Not even 

# Example Run 2:
# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 4
# Your tasks:
# finish homework - Finally Done
# clean room - Not even close
# Which task number? 2
# Removed: clean room

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 2
# Your tasks:
# finish homework - Finally Done

# Menu:
# 1) Add task
# 2) View tasks
# 3) Mark task as done
# 4) Remove task
# 5) Quit
# Type something: 5
# Bye^^ COME BACK WHEN YOU ARE READY

