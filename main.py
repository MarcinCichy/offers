from get_program_data import get_program_data
from get_element_data import get_element_data
import os

path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   



print('='*40)                                   # wywołanie funkcji offert
print ('Nazwa programu:',get_program_data(program_file) [0])      # nazwaprogramu
#print (get_program_data(program_file) [1])      # materiał
material_string = get_program_data(program_file) [1]
minus_index = (material_string.index('-'))
material = material_string[0:minus_index]
thicknes = abs(int(material_string[minus_index:])/10)
print('Materiał:',material)
print('Grubość:',thicknes,'mm')

print ('Czas cięcia programu:',get_program_data(program_file) [2])      # czas całego programu
print ('Ilość powtórzeń programu:',get_program_data(program_file) [3])      # ilość powtórzeń programu
# print (get_program_data(program_file) [4])    # wiersze tabeli  
# print (get_program_data(program_file) [5])      # ilość wierszy w tabeli


print('='*40)
#print(get_element_data(program_file))
print ('Nazwa detalu:',get_element_data(program_file)[0]['NAZWA PLIKU GEO:'])
dimensions =  (get_element_data(program_file)[0]['WYMIARY:'])
x_index = dimensions.index('x')
dimension_x = float(dimensions[0:x_index-1])
dimension_y = float(dimensions[x_index+2:-3])
print('Wymiar X detalu:',dimension_x,'mm')
print('Wymiar Y detalu:',dimension_y,'mm')
cut_time = get_element_data(program_file)[0]['CZAS OBRÓBKI:'][0:-4]
print ('Czas cięcia detalu:',cut_time,'min')
#print (get_element_data(program_file))
