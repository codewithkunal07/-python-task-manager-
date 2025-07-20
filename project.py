# To-Do List Application: Day-07 Project 🚀

# Step 1: Initialize lists
checklist = []
completed_tasks = []
incomplete_tasks = []

# Step 2: Add tasks to checklist
print("Enter your tasks for today (type 'done' when finished):")
while True:
    task = input("Add task: ")
    if task.lower() == 'done':
        break
    checklist.append(task)

# Step 3: Review and categorize each task
print("\nReview your tasks:")
for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ")
    if status.lower() == 'yes':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Step 4: Display summary
print("\n--- Task Summary ---")
print("✅ Completed Tasks:", completed_tasks)
print("❌ Incomplete Tasks:", incomplete_tasks)