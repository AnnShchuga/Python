from os.path import exists
from ДЗ7_CSV_creating import creating
from ДЗ7_File_writing import writing_scv
from ДЗ7_File_writing import writing_txt


path = 'ДЗ7_Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()