from application.salary import calculate_salary
from application.db.people import get_employees
from work_with_num.current_date import show_date_of_this_moment
from work_with_num.test_numpy import del_error_rate

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(show_date_of_this_moment())
    print(del_error_rate([54, 84, 363, 83]))