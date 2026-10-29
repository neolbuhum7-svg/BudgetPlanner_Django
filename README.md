# Budget Planner (Django)

A beginner-friendly Django budget planner website. It tracks income and expenses using SQLite.

## Run in VS Code

1. Extract `BudgetPlanner_Django.zip`.
2. Open the extracted `BudgetPlanner_Django` folder in VS Code.
3. Open Terminal > New Terminal.
4. Create and activate a virtual environment.

### Windows (PowerShell)
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If PowerShell blocks activation, use Command Prompt and run:
```bat
venv\Scripts\activate.bat
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

5. Open http://127.0.0.1:8000/ in your browser.

## Features
- Add income and expenses
- Dashboard totals and remaining balance
- Transaction history
- SQLite database
- Delete transactions
- Responsive page layout

This is a learning project. It does not include user accounts, so do not deploy it publicly with private financial information.
