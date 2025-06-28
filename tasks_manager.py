from googleapiclient.discovery import build
from auth import get_credentials

# List all task lists
def list_task_lists(service):
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get('items', [])
    return items

# List tasks in a given task list
def list_tasks(service, tasklist_id):
    results = service.tasks().list(tasklist=tasklist_id, showCompleted=True).execute()
    items = results.get('items', [])
    return items

# Add a new task to a given task list
def add_task(service, tasklist_id, title):
    task = {'title': title}
    result = service.tasks().insert(tasklist=tasklist_id, body=task).execute()
    return result

if __name__ == "__main__":
    creds = get_credentials()  # Should include tasks scope
    service = build('tasks', 'v1', credentials=creds)

    # List task lists
    tasklists = list_task_lists(service)
    if not tasklists:
        print("No task lists found.")
        exit(0)
    print("Your Task Lists:")
    for i, tl in enumerate(tasklists, 1):
        print(f"{i}. {tl['title']} (ID: {tl['id']})")
    print()

    # Show tasks in the first list
    first_list_id = tasklists[0]['id']
    tasks = list_tasks(service, first_list_id)
    print(f"Tasks in '{tasklists[0]['title']}':")
    if not tasks:
        print("  No tasks found.")
    else:
        for t in tasks:
            status = '✔️' if t.get('status') == 'completed' else '❌'
            print(f"  {status} {t['title']}")
    print()

    # Example: Add a new task
    new_task_title = input("Enter a new task to add (or leave blank to skip): ").strip()
    if new_task_title:
        added = add_task(service, first_list_id, new_task_title)
        print(f"Added task: {added['title']}") 