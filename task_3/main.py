import datetime
import time
from stackoverflow import StackOverFlowAPI


def get_unix_date(days=0):
    '''
    Функция переводит дату в unix-формат
    Параметр days указывает сколько дней прошло от текущей даты т.е.:
    days=0 - это сегодня
    days=1 - это вчера
    days=2 - это два дня назад
    и т.д.
    '''
    day = f'{datetime.datetime.now().date() - datetime.timedelta(days)}'
    date_obj = datetime.datetime.strptime(day, '%Y-%m-%d')
    return int(time.mktime(date_obj.timetuple()))


if __name__ == '__main__':
    two_days_ago = get_unix_date(days=2)
    today = get_unix_date(days=0)

    stackoverflow = StackOverFlowAPI()
    stackoverflow.get_issues(fromdate=two_days_ago, todate=today, tags='Python')