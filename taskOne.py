from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()

        current_date = datetime.today().date()

        days_difference = (current_date - date_obj).days

        return days_difference
    
    except ValueError as e:
        return f"Invalid date format. Please use YYYY-MM-DD format. Error: {str(e)}"
    
print(get_days_from_today("2021-10-09")) 