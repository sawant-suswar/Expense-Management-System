from datetime import date
from fastapi import FastAPI,HTTPException
import db_helper
from pydantic import BaseModel
from logger_setup import setup_logger

app = FastAPI()

logger = setup_logger("server")

class Expense(BaseModel):
    amount: int
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

class Monthly_Analytics(BaseModel):
    month_year: str
    total_amount: int


@app.get("/expenses/{expense_date}",response_model =list[Expense])
def get_expenses_by_date(expense_date:date):
    logger.info(f"fetching expenses data for {expense_date}")
    expenses = db_helper.get_expense_by_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=404, detail="No expense data found")
    return expenses

@app.post("/expenses/{expense_date}")
def add_expense(expense_date: date,expenses:list[Expense]):
    db_helper.delete_expense(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
    return {"Message": "Successfully added expense"}

@app.post("/analytics")
def get_summary_analytics(daterange:DateRange):
    data = db_helper.get_expense_summary_by_date(daterange.start_date,daterange.end_date)
    if data is None:
        raise HTTPException(status_code=404, detail="No expense data found")
    total = sum([row['total_amount'] for row in data])

    breakdown = {}
    for row in data:
        row["percentage"] = round((row['total_amount']/total)*100,2) if row['total_amount']>0 else 0
        breakdown[row["category"]] = {
            "total" : row["total_amount"],
            "percentage" : row["percentage"]
        }

    return breakdown

@app.get("/monthly_analytics")
def get_monthly_analytics(response_model = list[Monthly_Analytics]):
    data = db_helper.get_expense_total_by_month_year()
    if data is None:
        raise HTTPException(status_code=404, detail="No expense data found")
    return  data


