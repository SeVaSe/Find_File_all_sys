import asyncio
import os
import keyboard


class SearchFile:
    """ПАНЕЛЬ УПРАВЛЕНИЯ"""
    def __init__(self, files_list=None, keyword=None, function='да'):
        self.files_list = files_list  # список файлов
        self.keyword = keyword  # список слов
        self.function = function  # выбор функции

    global dictFileKey  # инициализация словоря, для хранения найденных значений

    async def search_word(self, filename, keyword):
        """ПОИСК СЛОВ В ВВДЕННЫХ ФАЙЛАХ"""
        try:
            with open(filename, 'r', encoding='utf-8') as fl:  # чтение файла
                content = fl.read()

                found_word = [wr for wr in keyword if wr in content]  # генератор списка найденных слов
                print(f'В файле \033[92m{filename}\033[0m нашел такие слова из вашего списка: \033[92m{found_word}\033[0m\n')
                dictFileKey[filename] = []
                dictFileKey[filename].append(found_word)  # добавление значений в словарь

                # for key, value in self.dictFileKey.items():
                #     print(f"Файл: {key}\n Значения: {value}")
        except PermissionError:
            print(f'\033[91m{"Чет с правами"}\033[0m \n')
        except Exception as e:
            print(f'\033[91m{f"Ошибка: {e}"}\033[0m \n')
        except:
            print(f'\033[91m{f"@Ошибка@"}\033[0m \n')

    async def search_all_word(self, filename, keyword):
        """ПОИСК СЛОВ ПО ВСЕМ ФАЙЛАМ СИСТЕМЫ"""
        try:
            with open(filename, 'r', encoding='utf-8') as fl:
                print(filename)
                try:
                    content = fl.read()
                    #print(f'{keyword} ++++')
                    found_word = [wr for wr in keyword if wr in content]  # генератор

                    if len(found_word) != 0:  # если в файле есть слова, то выполняем код
                        text = f'В файле {filename} нашел такие слова из вашего списка: {found_word}'
                        print(f'\033[92m{text}\033[0m \n')
                        dictFileKey[filename] = []
                        dictFileKey[filename].append(found_word)
                    else:
                        print(f'\033[93m{"Нету слов, которые нужны вам"}\033[0m \n')
                except Exception as e:
                    print(f'\033[91m{f"Ошибка1: {e}"}\033[0m \n')
        except PermissionError:
            print(f'\033[91m{"Чет с правами"}\033[0m \n')
        except Exception as e:
            print(f'\033[91m{f"Ошибка2: {e}"}\033[0m \n')
        except:
            print(f'\033[91m{f"@Ошибка@"}\033[0m \n')

    async def find_file(self):
        """НАЙТИ ФАЙЛ"""
        for root, dirs, files in os.walk('C:\\'):  # прохождение по всей системе, разделяя на блоки
            for file in files:  # если имя файла совпадает со списком, то далее...
                #print(file)
                match self.function:  # у нас есть функция с обозначениями, которые ведут себя как флаги
                    case 'да':  # выполнит функцию search_word
                        if file.lower() in self.files_list:
                            print(f'\033[92m{"Нашел файл:"}\033[0m {file}')
                            path = os.path.join(root, file)
                            await self.search_word(path, self.keyword)
                    case 'нет':  # выполнит функцию search_all_word
                        print(f'\033[95m{"Ищу слова в файлах системы:"}\033[0m')
                        path = os.path.join(root, file)
                        await self.search_all_word(path, self.keyword)
                    case 'fi':  # выполнит поиск полного пути для указанного файла
                            if file.lower() in self.files_list:
                                path = os.path.join(root, file)
                                print(f'\033[92m{"Нашел полный путь файла"}\033[0m \033[93m{file}\033[0m\033[92m:\033[0m {path}')
                                dictFileKey[file] = []
                                dictFileKey[file].append(path)
                            # else:
                            #     print(f'\033[91m{f"Ошибка, такого файла не существует!"}\033[0m \n')


class PanelControl:
    """ПАНЕЛЬ УПРАВЛЕНИЯ"""
    def __init__(self, fileListName=None, fileListText=None):
        self.fileListName = fileListName  # список фалов
        self.fileListText = fileListText  # список текстов

    # запуск функционала - 1
    async def findFileText(self, fileLName, fileTList):
        files_list = fileLName         #tes_ai_1.txt, tes_ai_2.txt, план работы.txt
        keyword = fileTList          #Привет васапа таск1 таск2
        tasks = []

        searchFile = SearchFile(files_list, keyword)
        tasks.append(searchFile.find_file())

        await asyncio.gather(*tasks)

    # запуск функционала - 2
    async def findOsText(self, fileTList, function):
        keyword = fileTList
        tasks = []

        searchFile = SearchFile(keyword=keyword, function=function)
        tasks.append(searchFile.find_file())

        await asyncio.gather(*tasks)

    # запуск функционала - 3
    async def find_file_name(self, fileLName, function):
        files_list = fileLName  # tes_ai_1.txt, tes_ai_2.txt, план работы.txt
        tasks = []

        searchFile = SearchFile(files_list=files_list, function=function)
        tasks.append(searchFile.find_file())

        await asyncio.gather(*tasks)

    # ЭТО НАДО ДЛЯ РАСПРЕДЕЛЕНИЯ ФЛАГОВ ПО ФУНКЦИИ
    async def input_name_file(self, function='да'):
        match function:
            case 'да':
                await self.findFileText(self.fileListName, self.fileListText)
            case 'нет':
                await self.findOsText(self.fileListText, function)
            case 'fi':
                await self.find_file_name(self.fileListName, 'fi')


async def main():
    while True:
        a = input('Выберите действие:\n'
                    '1. Поиск слов в указанных файлах\n'
                    '2. Поиск слов во всех файлах на компьютере\n'
                    '3. Поиск полного пути файлов во всей системе\n'
                    'Ваш выбор: ')
        print()
        match a.lower():
            case '1':
                inNameFile = input('Введите имя/ена файла/ов через запятую: ').lower()
                inTextFile = input('Введите слова, чтобы увидеть какой из данных файлов содержит данные слова: ').lower()
                print('\n\n')

                lNameFile = inNameFile.split(', ')
                lTextFile = inTextFile.split(' ')
                print(lNameFile, lTextFile)

                pContrl = PanelControl(lNameFile, lTextFile)
                await pContrl.input_name_file()
                i = 0
                for key, value in dictFileKey.items():
                    i += 1
                    print(f"\033[94mФайл{i}:\033[0m \033[95m{key}\033[0m\n \033[94mЗначения:\033[0m \033[95m{value}\033[0m")
                print('\n\n')
            case '2':
                inTextFile = input('Введите слова, чтобы увидеть список всех файлов, которые содержат данные слова: ')
                print('\n\n')

                lTextFile = inTextFile.split(' ')
                print(lTextFile)

                pContrl = PanelControl(fileListText=lTextFile)
                await pContrl.input_name_file('нет')
                i = 0
                for key, value in dictFileKey.items():
                    i += 1
                    print(f'\033[94mФайл{i+1}:\033[0m \033[95m{key}\033[0m\n \033[94mЗначения:\033[0m \033[95m{value}\033[0m')
                print('\n\n')
            case '3':
                inTextFile = input('Введите через запятую имена файлов, для получения полных путей: ')
                print('\n\n')

                lNameFile = inTextFile.split(', ')
                print(lNameFile)

                pContrl = PanelControl(fileListName=lNameFile)
                await pContrl.input_name_file('fi')
                i = 0
                for key, value in dictFileKey.items():
                    i += 1
                    print(f'\033[94mФайл{i + 1}:\033[0m \033[95m{key}\033[0m\n \033[94mЗначения:\033[0m \033[95m{value}\033[0m')
                print('\n\n')


if __name__ == '__main__':
    dictFileKey = {}
    asyncio.run(main())



