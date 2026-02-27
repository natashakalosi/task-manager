# task-manager
A Python-based productivity tool that automatically categorizes tasks by priority based on their deadlines.

### Key Features
- **Dynamic Priority Scoring:** Tasks are automatically labeled as High, Medium, or Low priority depending on how many days are left.
- **Date Math:** Calculates remaining days in real-time using Python's `datetime` and `pandas`.
- **Demo Mode:** Includes a built-in dataset to showcase the priority logic immediately.

### Built With
- **Python**
- **Pandas:** For data manipulation and vectorized calculations.
- **Datetime:** For handling deadlines and time differences.

### How it Works
1. Run the script.
2. Choose to enter your own tasks or load the demo data.
3. The app will display a filtered list of **High Priority** tasks (due in 3 days or less).
