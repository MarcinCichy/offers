from get_program_data import get_program_data
from get_element_data import get_element_data
import os

path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   



print('='*40)                            # wywołanie funkcji offert
print (get_program_data(program_file) [0])
print (get_program_data(program_file) [1])
print (get_program_data(program_file) [2])
print (get_program_data(program_file) [3])
print (get_program_data(program_file) [4])
print (get_program_data(program_file) [5])


print('='*40)
#print (get_element_data(program_file)[1][0]['NAZWA PLIKU GEO:'])
# wymiary =  (get_element_data(program_file)[1][1]['WYMIARY:'])
# print(wymiary+'|')
# print(len(wymiary))
# print (get_element_data(program_file)[1][2]['CZAS OBRÓBKI:'])