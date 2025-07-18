Expense Management System
==========================

This project is an Expense Management System that includes:

- A **Streamlit frontend application**
- A **FastAPI backend server**

Both components are designed to work together to help manage and track expenses efficiently.

Project Structure
-----------------
- **frontend/** : Contains the Streamlit frontend application code.
- **backend/**  : Contains the FastAPI backend server code.
- **tests/**    : Contains test cases for both frontend and backend.
- **requirements.txt** : Lists the required Python packages.
- **README.md** : Provides an overview and setup instructions for the project.

Dependencies
------------
Ensure you have Python installed, then install the required packages:


Usage Instructions
------------------
1. **Start the backend server**:
   Navigate to the `backend/` directory and run:uvicorn main:app --reload

2. **Run the frontend application**:
Navigate to the `frontend/` directory and run: streamlit run app.py

3. **Testing**:
Run tests from the project root using: pytest


Note
----
Make sure both the frontend and backend are running simultaneously for full functionality.



# Full-Stack-Py-ExpenseTracker
