import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_lgger
import datetime

logger = setup_lgger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1163",
        database="expense_manager"
    )


    cursor = connection.cursor(dictionary=True)

    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    logger.info(f"fetch_all_records called")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)


def fetch_expense_for_date(expense_date):
    logger.info(f"fetch_expense_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()

        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date:{expense_date} amount:{amount} category:{category} notes:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", (expense_date, amount, category, notes))

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called for date:{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summery(start_date, end_date):
    logger.info(f"fetch_expense_summery called with start:{start_date} end:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
        '''SELECT category, SUM(amount) as total
           FROM expenses WHERE expense_date
           BETWEEN %s and %s
           GROUP BY category;''',
           (start_date, end_date)
        )
        data = cursor.fetchall()

        return data

def fetch_monthly_expense_summary():
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month, SUM(amount) AS total_expense
            FROM expenses GROUP BY DATE_FORMAT(expense_date, '%Y-%m') ORDER BY month;
            '''
        )


        data = cursor.fetchall()

        return data


if __name__ == "__main__":
    # fetch_all_records()
    print(fetch_monthly_expense_summary())

