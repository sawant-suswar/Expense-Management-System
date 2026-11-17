
# Expense Mangement System

Expense Mangement System is a web-based application developed for mangement and monitoring of personal expenses. It let's user  record transactions, categorize spending and retrieve expense records based on specific dates.

The application is developed in python, FastAPI as backend API developement, Streamlit for all user interface and MySQL for data storage.
## Features

- Add, Update and Delete Transactions.
- Categorize expense based on spending types.
- Retrieve expenses using specific dates.
- Store expense records in a MySQL database.
- Interactive dashboard using Streamlit.


## Tech Stack

**Programming Language:** Python

**Frontend:** Streamlit

**Backend:** FastAPI, Uvicorn

**Database:** MySQL

**Libraries:** pandas, request, pydantic, pytest, mysql-connector-python


## Architecture
![Architecture Diagram]<img width="327" height="562" alt="Architecture" src="https://github.com/user-attachments/assets/01473227-1a2a-4096-8652-b4bba46f03dd" />

## Project Structure

```text
expense-management/
│
├── backend/
│   ├── app.log
│   ├── logger_setup.py
│   ├── db_helper.py
│   └── server.py
│
├── frontend/
│   ├── app.py
|   ├── add_upload_ui.py
|   ├── analytics_monthly_ui.py
│   └── analytics_ui.py
│
├── tests/
│   ├── conftest.py
|   └── backend
│       └── test_db_helper.py
|
├── .env
├── requirements.txt
└── README.md
```

- backend/: Contains FastAPI server endpoints and database operations.
- frontend/: Contains Streamlit application code.
- test/: Contains unit tests for database operations.
- requirements.txt: List the required python packages.
- README.md: Provides an overview and instructions for the project.


## Pre-requisites

Make sure the following software is installed:

- Python 3.12 or above
- MySQL 8.0 or above
## Installation

### 1. Clone the repository

```bash
git clone https://github.com/username/expense-Management-system.git
```

### 2. Navigate to the project directory
``` bash
cd expense-Management-system
```

### 3. Create a virtual environment
```bash
python -m venv .venv
```

### 4. Activate the virtual environment
```bash
Windows:

.venv\Scripts\activate

Linux/macOS:

source .venv/bin/activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Database Configuration

- Install and configure MySQL Server.
- Create a database named `expense_manager`.
- Configure your database credentials in the `db_helper.py` file.

### 7. Run FastAPI server (server.py)
```bash
uvicorn server:app --reload

Access API Documentation:

http://127.0.0.1:8000/docs
```

### 8. Run Streamlit application
```bash
streamlit run app.py
```


## API Documentation

| Method | Endpoint | Description |
| --- | --- | --- |
| Get | **/expenses/{expense_date}** | Retrieve Expenses By Date |
| Post| **/expenses/{expense_date}** | Add Expense |
| Post| **/analytics** | Get Summary Analytics by Category
| Get | **/monthly_analytics** |Get Monthly Analytics|
		


