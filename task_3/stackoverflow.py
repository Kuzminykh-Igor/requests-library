import requests
import datetime
from pprint import pprint


class StackOverFlowAPI:

    def __init__(self):
        self.URL = 'https://api.stackexchange.com'

    def get_issues(self, fromdate, todate, tags):
        '''
        Метод выводит вопросы с сайта stackoverflow в виде словаря {'название_вопроса': 'ссылка_на_вопрос'}
        Параметры:
        fromdate - дата начала поиска (например ПОЗАВЧЕРА)
        todate - дата конца поиска (например СЕГОДНЯ)
        tags - по этому тэгу ищутся вопросы
        '''
        url = f'{self.URL}/2.3/questions'
        params = {'fromdate': fromdate, 'todate': todate, 'order': 'desc', 'sort': 'activity', 'tagged': tags, 'site': 'stackoverflow'}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=url, params=params, headers=headers).json()

        f_day = datetime.datetime.fromtimestamp(fromdate).strftime('%d.%m.%Y')
        t_day = datetime.datetime.fromtimestamp(todate).strftime('%d.%m.%Y')

        issues = {}
        for res in response['items']:
            issues[f"{res['title']}"] = res['link']
        print(f'\nС {f_day} по {t_day} по тэгу \"{tags}\" найдены следующие вопросы:\n')
        pprint(issues)