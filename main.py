from get_program_data import get_program_data
from get_element_data import get_element_data
import os

path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   



print('='*40)                                   # wywołanie funkcji offert
print ('Nazwa programu:', get_program_data(program_file) [0])      # nazwa programu
#print ('Materiał:', get_program_data(program_file) [1])      # materiał
material_string = get_program_data(program_file) [1]
minus_index = (material_string.index('-'))
material = material_string[0:minus_index]
thicknes = abs(int(material_string[minus_index:])/10)
print('Materiał:',material)
print('Grubość:',thicknes,'mm')

print ('Czas cięcia programu:', get_program_data(program_file) [2])      # czas całego programu
print ('Ilość powtórzeń programu:', get_program_data(program_file) [3])      # ilość powtórzeń programu
# print (get_program_data(program_file) [4])    # wiersze tabeli  
# print (get_program_data(program_file) [5])    # ilość wierszy w tabeli
#rows = get_program_data(program_file) [4]
table_lenght = get_program_data(program_file) [5]
# print(table_lenght)

print('='*40)
i=1
while i < table_lenght:
   print ('Nazwa detalu:', get_element_data(program_file,i)[0]['NAZWA PLIKU GEO:']) 
   print ('Wymiary detalu:', get_element_data(program_file,i)[0]['WYMIARY:']) 
   print ('Czas cięcia detalu:', get_element_data(program_file,i)[0]['CZAS OBRÓBKI:']) 
   print ('Ilość:', get_element_data(program_file,i)[0]['ILOŚĆ:']) 
   print('='*40)
   i+=20
#print(get_element_data(program_file))
#print (get_element_data(program_file)[0]['NAZWA PLIKU GEO:'])
#wymiary =  (get_element_data(program_file)[0]['WYMIARY:'])
# print(wymiary+'|')
# print(len(wymiary))
# print (get_element_data(program_file)[0]['CZAS OBRÓBKI:'])
#print (get_element_data(program_file))
#print (get_element_data(program_file)[1]['NAZWA PLIKU GEO:'])
#print (get_element_data(program_file)[2]['NAZWA PLIKU GEO:'])
#print ('Lista elemenów:',len(get_element_data(program_file)))