tasks=[]
def show_menu():
  print("1.Add task: ")
  print("2.view task: ")
  print("3.delete task: ")
  print("4.Exit")
while(True):
  show_menu()
  choice=input("Enter your choice (1-4): ")

if(choice==1):
  task=input("Enter a new task: ")
  tasks.append(task)
  print(f"✅ Task '{task}' added!")

elif(choice==2):
  if len(tasks)==9:
    print("No task is available! ")
  else:
    print("\n Your tasks:")
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")
elif(choice==3):
  if len(tasks)==0:
    print("No task to delete!")
  else:
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")
    try:
      task_num=int(input("Enter task number to delete ")
      removed=tasks.pop(task_num-1)
      print(f"🗑️ Task '{removed}' deleted!")
    except (ValueError, IndexError):
                print("⚠️ Invalid input, please try again.")

elif(choice==4):
  print("👋 Exiting... Goodbye!")
  break
else:
  print("⚠️ Invalid choice, please enter 1-4.")
