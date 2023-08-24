import asyncio
import os


class SearchFile:
    """ПАНЕЛЬ УПРАВЛЕНИЯ"""
    def __init__(self, files_list=None, keyword=None, function='да'):
        self.files_list = files_list
        self.keyword = keyword
        self.function = function

    async def search_word(self, filename, keyword):
        with open(filename, 'r', encoding='utf-8') as fl:
            content = fl.read()

            found_word = [wr for wr in keyword if wr in content]
            print(f'В файле {os.path.basename(filename)} нашел такие слова из вашего списка: {found_word}\n')

    async def search_all_word(self, filename, keyword):
        try:
            with open(filename, 'r', encoding='utf-8') as fl:
                try:
                    content = fl.read()
                    print(f'{keyword} ++++')
                    found_word = [wr for wr in keyword if wr in content]

                    if len(found_word) != 0:
                        text = f'В файле {filename} нашел такие слова из вашего списка: {found_word}\n'
                        print(f'\033[91m{text}\033[0m')
                    else:
                        print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRORRRREEEEEEEEEE')
                except Exception as e:
                    print(f'Ошибка: {e}')
        except PermissionError:
            print('Чет с правами')
    async def find_file(self):
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                #print(file)
                match self.function:
                    case 'да':
                        if file.lower() in self.files_list:
                            print(f'Нашел файл: {file}')
                            path = os.path.join(root, file)
                            await self.search_word(path, self.keyword)
                    case 'нет':
                        print('Ищу слова в файлах по система: ')
                        path = os.path.join(root, file)
                        await self.search_all_word(path, self.keyword)



class PanelControl:
    """ПАНЕЛЬ УПРАВЛЕНИЯ"""
    def __init__(self, fileListName=None, fileListText=None):
        self.fileListName = fileListName
        self.fileListText = fileListText

    async def findFileText(self, fileLName, fileTList):
        files_list = fileLName         #tes_ai_1.txt, tes_ai_2.txt, план работы.txt
        keyword = fileTList          #Привет васапа таск1 таск2
        tasks = []


        searchFile = SearchFile(files_list, keyword)
        tasks.append(searchFile.find_file())

        await asyncio.gather(*tasks)

    async def findOsText(self, fileTList, function):
        keyword = fileTList
        tasks = []

        searchFile = SearchFile(keyword=keyword, function=function)
        tasks.append(searchFile.find_file())

        await asyncio.gather(*tasks)

    async def input_name_file(self, function='да'):
        match function:
            case 'да':
                await self.findFileText(self.fileListName, self.fileListText)
            case 'нет':
                await self.findOsText(self.fileListText, function)






if __name__ == '__main__':
    while True:
        a = input('да или нет: ')
        match a.lower():
            case 'да':
                inNameFile = input('Введите имя/ена файла/ов через запятую: ').lower()
                inTextFile = input('Введите слова, чтобы увидеть какой из данных файлов содержит данные слова: ').lower()
                print('\n\n')

                lNameFile = inNameFile.split(', ')
                lTextFile = inTextFile.split(' ')
                print(lNameFile, lTextFile)

                pContrl = PanelControl(lNameFile, lTextFile)
                asyncio.run(pContrl.input_name_file())

            case 'нет':
                inTextFile = input('Введите слова, чтобы увидеть список всех файлов, которые содержат данные слова: ')
                print('\n\n')

                lTextFile = inTextFile.split(' ')
                print(lTextFile)

                pContrl = PanelControl(fileListText=lTextFile)
                asyncio.run(pContrl.input_name_file('нет'))


