from ya_disk import YandexDisk


if __name__ == '__main__':
    TOKEN = input('Введите токен для Я.Диска: ')
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path='test.txt', filename='test.txt')