from datetime import datetime

def get_days_from_today(date):
        try:
            date_str = datetime.strptime( date, "%Y-%m-%d")
            today = datetime.today()
            difference = date_str - today 
            return difference.days
        except ValueError:
            print(f"{date} має бути у форматі YYYY-MM-DD. Спробуйте знову, використовуючи цифри")
            return None 

days_difference = get_days_from_today("2021-10-09")
print(f"Різниця у днях: {days_difference}")