import datetime
import pandas as pd

print("---Task Manager---")

tasks = []

# 1. Data Input Section
choice = input("1. Input your own tasks \n2. Load Demo Tasks \nSelection: ")

if choice == '1':
    while True:
        task_name = input("\nEnter task name (type '0' to finish): ").strip()
        if task_name == '0': 
            break
        
        d_input = input("Deadline (YYYY-MM-DD) [Leave empty for today]: ").strip()
        
        # Error handling for date input
        try:
            if d_input:
                deadline = datetime.datetime.strptime(d_input, "%Y-%m-%d").date()
            else:
                deadline = datetime.date.today()
        except ValueError:
            print("Invalid format! Defaulting to today's date.")
            deadline = datetime.date.today()
            
        status = input("Status (Pending/Completed): ").lower().strip()
        
        tasks.append({'Task': task_name, 'Deadline': deadline, 'Status': status})
else:
    # Demo data for quick testing
    today = datetime.date.today()
    print("\nLoading demo tasks...")
    tasks = [
        {'Task': 'Python Project Submission', 'Deadline': today + datetime.timedelta(days=1), 'Status': 'pending'},
        {'Task': 'Fix CSS Layout Issues', 'Deadline': today + datetime.timedelta(days=2), 'Status': 'pending'},
        {'Task': 'Update Personal Portfolio', 'Deadline': today + datetime.timedelta(days=4), 'Status': 'pending'},
        {'Task': 'Read Pandas Documentation', 'Deadline': today + datetime.timedelta(days=5), 'Status': 'pending'},
        {'Task': 'Clean up GitHub Repository', 'Deadline': today + datetime.timedelta(days=10), 'Status': 'pending'},
        {'Task': 'Backup Local Files', 'Deadline': today + datetime.timedelta(days=15), 'Status': 'pending'},
        {'Task': 'Setup Python Environment', 'Deadline': today - datetime.timedelta(days=3), 'Status': 'completed'}
    ]

# 2. Process Data using Pandas
df = pd.DataFrame(tasks)

if not df.empty:
    today = datetime.date.today()
    
    # Calculate days remaining using vectorized operations
    df['Days_Left'] = (df['Deadline'] - today).apply(lambda x: x.days)

    # 3. Dynamic Priority Logic
    def assign_priority(row):
        if row['Status'] == 'completed': 
            return 'Completed'
        if row['Days_Left'] <= 3: 
            return 'High'
        if row['Days_Left'] <= 5: 
            return 'Medium'
        return 'Low'

    df['Priority'] = df.apply(assign_priority, axis=1)

    # 4. Display Results
    # Formatting the output for better readability
    print("HIGH PRIORITY TASKS")
    high_prio = df[df['Priority'] == 'High'].copy()
    
    if not high_prio.empty:
        # Reset index to start from 1 for the display
        high_prio.index = range(1, len(high_prio) + 1)
        print(high_prio[['Task', 'Deadline', 'Days_Left']].to_string())
    else:
        print("No high priority tasks at the moment! ")

    print("Full task list processed successfully.")

else:
    print("No tasks found to process.")

