# Lab 1: Grade Evaluator & Archiver
A Python + Bash project that evaluates a student's grades from a CSV file and archives that grade history automatically.
## What This Project Does
**`grade-evaluator.py`** reads a CSV of assignment grades and:
- Validates that scores are within range and weight add up correctly
- Calculates the Final Grade and GPA
- Determines PASSED/FAILED status (requires >= 50% in both Formatives and Summatives)
- Flags any failed Formative assignment eligible for resubmission

**`organizer.sh`** archives the current `grades.csv`:
- Creates an `archive/` folder if needed, and moves the timestamped file into it 
- Resets the workspace with a fresh, empty `grades.csv`
- Logs every archive action to `organizer.log` 
## Project Structure
```
lab1_fmohamed-a11y/
├── grade-evaluator.py   Python script - reads grades.csv and evaluates the student's standing
├── organizer.sh         Bash script - archives grades.csv and resets the workspace
├── grades.csv           Input data - the student's assignment scores
├── organizer.log        Auto-generated log of every archive run (created on first use)
├── archive/             Auto-created folder holding timestamped past versions of grades.csv
└── Readme.md            This file
```
## 🐍 How to Run the Grade Evaluator
1. Make sure `grades.csv` is in the same folder as `grade-evaluator.py`.
2. Run:
```bash
   python3 grade-evaluator.py
```
3. When it asks for a filename, type:
```
grades.csv
```
4. That's it, the script prints  everything at once: validation results, Final Grade, GPA, category averages, PASSED/FAILED status, and resubmission info if applicable.
### Testing the empty-CSV case
To confirm the script handles an empty CSV gracefully instead of crashing, you can create a test file with just the header row and no assignment:
```bash
echo "assignment,group,score,weight" > empty_test.csv
python3 grade-evaluator.py
```
When you type `empty_test.csv` it should print a message saying there's no data to process, instead of giving an error.

## 🗃️ How to Run the Archiver

1. Give it permission to run (only the first time):
```bash
   chmod +x organizer.sh
```
2. Run it:
```bash
   ./organizer.sh
```
3. Everything else happens automatically. No input is needed. Check the results anytime with:
```bash
   ls archive/
   cat organizer.log
   cat grades.csv
```
   Note: After running this command, `grades.csv` will be empty and ready for the next batch of grades. The previous data has been moved into `archive/`.

## 📝 A Couple of Notes
- If `grades.csv` doesn't exist when you run the evaluator, it exits with a clear error instead of crashing.
- If `grades.csv` is empty (right after running the archiver), the evaluator reports that there's nothing to process, instead of erroring out.
- You can run `organizer.sh` as many times as you like. `organizer.log` keeps growing with every run. It never gets overwritten.

## 💻 Author
Fatima Samir - ALU, BSE Year1, Trimester 2
