#1)A manual list to work with
to_do_list = ["Learn Python","Go to the gym","Drink water","Read a book"]
completed_tasks = []
print("Original_list:", to_do_list)
#2)Adding items to the list
to_do_list.append("Go for a walk")
print("Updated_list:",to_do_list)
#insert
to_do_list.insert(1,"Buy groceries")
print("Updated_list:",to_do_list)
#extend:adding multiple items from another list to the original list
additional_tasks = ["Visit the orphanage","Cook dinner"]
to_do_list.extend(additional_tasks)
print("Updated_list:",to_do_list)
#3)Finding and rearranging tasks
#Index: Finding the position of a task in a list
position = to_do_list.index("Drink water")
print("Position of drink water:",position)
#Reverse: Flips the list backwards
to_do_list.reverse()
print("Reversed_list:",to_do_list)
#Sort: Permanently sorts the list in alphabetical order
to_do_list.sort()
print("Sorted_list(alphabetical):", to_do_list)
#4)Methods to remove items from the list
#Pop: Removes item at a specific index and returns its value
Removed_item = to_do_list.pop(2)
print(f"{Removed_item}:",to_do_list)
#Remove: Removes the first occurence of avalue from the list(Removes an item by its exact name)
to_do_list.remove("Go for a walk")
print("Updated_list:",to_do_list)
def complete_tasks(task):
    if task in to_do_list:
       to_do_list.remove(task)
       completed_tasks.append(task)
       print(f" '{task}' is completed.")
    else:
        print(f" '{task}' is not in to_do list")
user_input = input("Enter a new task to add to the to_do list:")
complete_tasks(user_input)
print("Final completed tasks:",completed_tasks)
