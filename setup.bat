@echo off

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python.
    exit /b
)

:: Create a virtual environment
python -m venv .venv

:: Activate the virtual environment
call .\.venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Apply migrations
python manage.py migrate

:: Optionally, collect static files if your project uses this
:: python manage.py collectstatic --noinput

:: Optionally, you might want to create a superuser for Django admin
:: python manage.py createsuperuser

echo Setup is complete. The virtual environment is activated. You can now run the Django server with 'python manage.py runserver'.
