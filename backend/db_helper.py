import mysql.connector
from contextlib import contextmanager
from logger_setup import setup_logger
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("host")
db_user = os.getenv("user")
db_password = os.getenv("password")
db_name = os.getenv("database")

#logging Config

logger = setup_logger("db_helper")


#DB config

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password ,
            database = db_name
        )

    if connection.is_connected():
        print("DB connection established")
    else:
        print("DB connection failed")

    cursor = connection.cursor(dictionary = True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def get_expenses():
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses")
        expenses = cursor.fetchall()
        return expenses

def get_expense_by_date(date):
    logger.info(f"Fetched expense details of {date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(date,amount,category,notes):
    logger.info(f"Inserted expense details in {date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("Insert Into expenses(expense_date,amount,category,notes) Values(%s,%s,%s,%s)",
                       (date,amount,category,notes))

def delete_expense(date):
    logger.info(f"Deleted expense for {date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("Delete from expenses where expense_date =%s",(date,))

def get_expense_summary_by_date(start_date,end_date):
    logger.info(f"get_expense_summary_by_date called with start_date:{start_date} and end_date:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("""select category,SUM(amount) as total_amount from expenses
                        where expense_date between %s and %s
                        group by category""",(start_date,end_date))
        summary = cursor.fetchall()
        return summary

def get_expense_total_by_month_year():
    logger.info(f"executing get_expense_total_by_month_year sql query")
    with get_db_cursor() as cursor:
        cursor.execute("""with expense_month As
                    (
                    select *, 
                        concat(monthname(expense_date), " " , Year(expense_date)) as month_year 
                    from expenses
                    )
                    select  month_year, 
                        sum(amount) as total_amount
                    from expense_month
                    Group By  month_year;""")
        total = cursor.fetchall()
        return total

if __name__ == "__main__":
    #get_expenses()
    #delete_expense("68")
    #get_expense_by_date("2026-11-04")
    #summary = get_expense_summary_by_date("2024-08-02","2024-08-05")
    #for expense in summary:
        #print(expense)
    total = get_expense_total_by_month_year()
    for month in total:
        print(month)

