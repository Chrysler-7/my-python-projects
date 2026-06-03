planner = [{
    "task": "Biology essay", "due_date": "2026-07-15", "status": "incomplete"
}, {
    "task": "Physics project", "due_date": "2026-06-20", "status": "complete"
}, {
    "task": "Chemistry lab report", "due_date": "2026-07-01", "status": "incomplete"
}]
planner.append({
    "task": "Geography group work", "due_date": "2026-06-15", "status": "complete"
}, {
    "task": "Teacher consultation", "due_date":"2026-06-23", "status": "complete"
})
print("Updated planner:", planner)
student_planner = planner.index({"task": "Teacher consultation"})
print("Index of 'Teacher consultation':", student_planner)
planner.remove({"task": "Physics project", "due_date": "2026-06-20", "status": "complete"})
print("Updated planner after removing 'Physics project':", planner)