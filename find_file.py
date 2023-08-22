import asyncio
import os


async def search_word(filename, keyword):
    with open(filename, 'r', encoding='utf-8') as fl:
        content = fl.read()
        print('я тут')

        found_word = [wr for wr in keyword if wr in content]
        print(f'В файле {os.path.basename(filename)} нашел такие слова из вашего списка: {found_word}')

async def main():
    files_list = ['tes_ai_1.txt', 'tes_ai_2.txt', 'план работы.txt']
    keyword = ['Привет', 'васапа', 'таск1', 'таск2']

    tasks = []

    while True:
        for root, dirs, files in os.walk('C:\\'):
            for file in files:

                if file in files_list:
                    print(f'Нашел файл: {file}')
                    path = os.path.join(root, file)

                    task1 = asyncio.create_task(search_word(path, keyword))
                    tasks.append(task1)


        await asyncio.gather(*tasks)


asyncio.run(main())
