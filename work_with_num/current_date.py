from datetime import datetime

def show_date_of_this_moment():
    return f'Сегодня {(str(datetime.today())).split(' ')[0]}'