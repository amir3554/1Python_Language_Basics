# Simple CLI Task Manager

A lightweight, file-based command-line tool for managing your TODOs.  
Tasks are persisted in a plain-text file (`Mytasks.txt`) and can be added, listed, marked done, removed, or reset.

---

## Project Overview

This small Python project provides a single script (`task_manager.py` or `main.py`) which:

1. **Parses** command-line arguments with `argparse`.  
2. **Dispatches** commands to a `TaskController` that reads/writes tasks in `Mytasks.txt`.  
3. Supports the following subcommands:
   - `add` — create a new task  
   - `list` — show unfinished (or all) tasks  
   - `check` — mark a task done (and remove if already done)  
   - `remove` — delete a specific task  
   - `reset` — wipe **all** tasks  

All logic for storing, formatting, and manipulating tasks lives in the `TaskController` class (in `controller.py` or similar).

---

## Dependencies

This project uses **only** the Python Standard Library:

- **`argparse`**  
  For parsing subcommands & their options.
- **`datetime`**  
  (Optional) If you extend tasks with date fields in future.
- **`os` / `sys`**  
  For file‐path handling and script entry point.

_No third-party modules required!_

---

## Installation

1. **Clone** the repo:
   ```bash
   git clone https://github.com/yourusername/simple-cli-task-manager.git
   cd simple-cli-task-manager


## Usage
bash
Copy
Edit
python task_manager.py <command> [options]



# add new task 
	<title>
-d, --description <text>
-s, --start_date YYYY-MM-DD
-e, --end_date YYYY-MM-DD
--done

#  list	List tasks	-a, --all (include completed tasks)


check	Mark a task done (or remove if done)	-t, --task <number>

remove	Remove a task permanently	-t, --task <number>


reset	Remove all tasks	(no options)



# 1. Add a task with title only
python task_manager.py add "Buy groceries"

# 2. Add a task with description & dates
python task_manager.py add "Write report" \
  -d "Outline and data analysis" \
  -s 2025-07-06 -e 2025-07-08

# 3. Show only unfinished tasks
python task_manager.py list

# 4. Show all tasks (including done)
python task_manager.py list --all

# 5. Mark task #2 as done
python task_manager.py check --task 2

# 6. Delete task #3
python task_manager.py remove --task 3

# 7. Clear every task
python task_manager.py reset


add_task(args)	Append a new task line (with title, description, dates, done-flag) to Mytasks.txt.

Display(args)	Read & print tasks. If args.all, include completed; otherwise, only unfinished.

check_task(args)	Toggle “done” status of task args.task; remove it if already done.

remove_task(args)	Permanently delete the task at index args.task.

reset()	Erase all contents of Mytasks.txt.








#  Data Storage
File: Mytasks.txt

Location: Same folder as the script

Format: One task per line; fields for title, description, start/end dates, and a done-flag.


...
Feel free to adjust repository URLs, file names, or expand on the field-format in `Mytasks.txt` as needed.

