# walk () генерирует имена файлов в дереве каталогов, перемещаясь по дереву сверху вниз или снизу вверх
from os import path, walk, listdir
import shutil

project_name = 'my_project'

try:
    for root, dirs, files in walk(project_name):
# поиск templates в папке
        if 'templates' in dirs and root != project_name:
#listdir для получения списка всех файлов и каталогов в указанном каталоге
            for entry in listdir(path.join(root, 'templates')):
#path.join объединяет компоненты в имени пути для создания полного имени пути
#shutil.copytree рекурсивно копирует все дерево каталогов 
                shutil.copytree(path.join(root, 'templates', entry), path.join(project_name, 'templates', entry))

except FileExistsError:
    print('already worked with these templates')