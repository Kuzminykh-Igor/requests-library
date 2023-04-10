import requests


def get_best_superhero(heroes_list):
    response = requests.get(url=URL)
    all_heroes = response.json()
    heroes = {}
    for hero in all_heroes:
        if hero['name'] in heroes_list:
            heroes[f'{hero["name"]}'] = hero['powerstats']['intelligence']
    best_hero = max(heroes, key=lambda el: heroes[el])

    print(f"Среди \"{', '.join(heroes_list)}\". Самый умный супергерой - {best_hero}.")


if __name__ == '__main__':
    URL = "https://akabab.github.io/superhero-api/api/all.json"
    superhero_list = ['Hulk', 'Captain America', 'Thanos']
    get_best_superhero(superhero_list)