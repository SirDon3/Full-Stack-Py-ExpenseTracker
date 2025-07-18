from datetime import datetime
from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

class MonthlySummary(BaseModel):
    month: str
    total_expense: float
    month_name: str

@app.get("/expense/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses = db_helper.fetch_expense_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")
    return expenses

@app.post("/expense/{expense_date}")
def add_or_update_expense(expense_date:date, expenses:List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summery(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summery from database")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total) * 100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown

@app.get("/analytics/monthly", response_model=List[MonthlySummary])
def get_monthly_expenses():
    expenses = db_helper.fetch_monthly_expense_summary()
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")

    for expense in expenses:
        try:
            month_date = datetime.strptime(expense["month"], "%Y-%m")
            expense["month_name"] = month_date.strftime("%B")
        except ValueError:
            expense["month_name"] = "Unknown"

    return expenses