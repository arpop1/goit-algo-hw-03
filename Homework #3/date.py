from datetime import datetime

def get_days_from_today(date):
        try:
            date_str = datetime.strptime( date, "%Y-%m-%d").date()
            today = datetime.today().date()
            difference = date_str - today 
            return difference.days
        except ValueError:
            print(f"{date} має бути у форматі YYYY-MM-DD. Спробуйте знову, використовуючи цифри")
            return None 

days_difference = get_days_from_today("2025-02-24")
print(f"Різниця у днях: {days_difference}")
