# Import-safe to-do module
# Keeps data and functions at module level; interactive/demo code is inside `demo()`.

to_do_list = ["Learn Python", "Go to the gym", "Drink water", "Read a book"]
completed_tasks = []


def display_tasks():
    """Return a list of tuples (index, task) for current tasks."""
    return list(enumerate(to_do_list, start=1))


def add_task(task: str) -> bool:
    """Add a non-empty task. Returns True if added."""
    task = task.strip()
    if not task:
        return False
    to_do_list.append(task)
    return True


def delete_task(index: int) -> str:
    """Delete task by 1-based index and return the removed task.

    Raises IndexError if index out of range.
    """
    if index < 1 or index > len(to_do_list):
        raise IndexError("Task index out of range")
    return to_do_list.pop(index - 1)


def complete_tasks(task: str) -> bool:
    """Mark a task completed by name. Returns True if moved."""
    if task in to_do_list:
        to_do_list.remove(task)
        completed_tasks.append(task)
        return True
    return False


def demo():
    """Interactive demo — kept inside function so importing is safe."""
    print("Original_list:", to_do_list)
    add_task("Go for a walk")
    print("Updated_list:", to_do_list)
    to_do_list.insert(1, "Buy groceries")
    print("Updated_list:", to_do_list)
    additional_tasks = ["Visit the orphanage", "Cook dinner"]
    to_do_list.extend(additional_tasks)
    print("Updated_list:", to_do_list)
    print("Position of 'Drink water':", to_do_list.index("Drink water"))
    to_do_list.reverse()
    print("Reversed_list:", to_do_list)
    to_do_list.sort()
    print("Sorted_list (alphabetical):", to_do_list)
    removed = to_do_list.pop(2)
    print(f"{removed}:", to_do_list)
    if "Go for a walk" in to_do_list:
        to_do_list.remove("Go for a walk")
        print("Updated_list:", to_do_list)
    user_input = input("Enter a new task to add to the to_do list: ")
    if add_task(user_input):
        print("Task added")
    else:
        print("Empty task not added")
    print("Final completed tasks:", completed_tasks)


if __name__ == "__main__":
    demo()
