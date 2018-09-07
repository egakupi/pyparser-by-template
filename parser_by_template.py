import re
from os import listdir
from os.path import isfile, isdir, join

"""
Дан каталог на диске. В нём находятся различные файлы.
Часть файлов имеет имя, заданное шаблоном:

image-[name]-[timestamp].tar.gz

например:
image-x64_600_sspace_windows-20180726T161105.tar.gz
image-unix_1100_engine-e2k-linux_vdb-20180726T041855.tar.gz

Необходимо написать функцию, которая найдет в каталоге все файлы, попадающие под шаблон, и вернет список, содержащий только [name] из названий файлов. Для приведенных выше примеров, список должен содержать элементы:
x64_600_sspace_windows
unix_1100_engine-e2k-linux_vdb

Обратите внимание, что [name] может также содержать символы дефиса.
Список должен содержать уникальные элементы.
"""


def parse(path):
    if not isdir(path):
        print("Path isn\'t corrected")
    else:
        only_files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in only_files:
            file = re.search('(?<=-)[\w-]+(?=-)', file)
            # TODO return unique list of [name]
            print(file.group(0))
