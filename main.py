#-----IMPORTS-----#
from datetime import datetime

#-----FUNCTIONS-----#
def get_and_handle_user_input(task_list):
    raw_input = input("task-cli ")
    user_action = raw_input.split()

    if user_action[0] == "add":
      try:
        add_item(user_action[1], task_list)
      except IndexError:
        print("The command expects 1 argument")

    if user_action[0] == "update":
      pass

    if user_action[0] == "delete":
      pass

    if user_action[0] == "mark-in-progress":
      pass

    if user_action[0] == "mark-done":
      pass
    
    if user_action[0] == "list":
      pass

    if user_action[0] == "list done":
      pass

    if user_action[0] == "list todo":
      pass
    
    if user_action[0] == "list in-progress":
      pass

def add_item(description, list):
  #I want the new task to have the lowest available positive integer as its ID.
  # for i in len(list):
  #   print (f"there are {i} items in the list")
  print(description)

#-----MAIN-----#
def main():
  print(f"Welcome to the Task Tracker")

  task_list = []

  get_and_handle_user_input(task_list)

if __name__ == "__main__":
  main()