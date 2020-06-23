from get_program_data import get_program_data
from get_element_data import get_element_data
import os

path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   



print('='*40)                                   # wywołanie funkcji offert
print (get_program_data(program_file) [0])      # nazwaprogramu
print (get_program_data(program_file) [1])      # materiał
print (get_program_data(program_file) [2])      # czas całego programu
print (get_program_data(program_file) [3])      # ilość powtórzeń programu
# print (get_program_data(program_file) [4])    # wiersze tabeli  
print (get_program_data(program_file) [5])      # ilość wierszy w tabeli


print('='*40)
#print(get_element_data(program_file))
print (get_element_data(program_file)[0]['NAZWA PLIKU GEO:'])
wymiary =  (get_element_data(program_file)[0]['WYMIARY:'])
print(wymiary+'|')
print(len(wymiary))
print (get_element_data(program_file)[0]['CZAS OBRÓBKI:'])
#print (get_element_data(program_file))
print (get_element_data(program_file)[1]['NAZWA PLIKU GEO:'])
print (get_element_data(program_file)[2]['NAZWA PLIKU GEO:'])