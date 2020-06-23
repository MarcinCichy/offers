from get_program_data import get_program_data
from get_element_data import get_element_data
import os

path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   

class Detail:
   def __init__ (self, name, material, thicknes, dimension_x,dimension_y, cut_time, quantity, price):
      self.name = name
      self.material = material
      self.thicknes = thicknes
      self.dimension_x = dimension_x
      self.dimension_y = dimension_y
      self.cut_time = cut_time
      self.quantity = quantity
      self.price = price

   # def print_description(self):
   #    print(self.city,self.full_price(),"tyś złotych")

   # def __repr__(self):
   #    return self.city+' '+str(self.full_price())

print('='*40)                                   
print ('Nazwa programu:', get_program_data(program_file) [0])      # nazwa programu
material_string = get_program_data(program_file) [1]
minus_index = (material_string.index('-'))
material = material_string[0:minus_index]
thicknes = abs(int(material_string[minus_index:])/10)
print('Materiał:',material)
print('Grubość:',thicknes,'mm')

print ('Czas cięcia programu:', get_program_data(program_file) [2],'godz.:min')      # czas całego programu
print ('Ilość powtórzeń programu:', get_program_data(program_file) [3])      # ilość powtórzeń programu
# print (get_program_data(program_file) [4])    # wiersze tabeli  
# print (get_program_data(program_file) [5])    # ilość wierszy w tabeli
#rows = get_program_data(program_file) [4]
table_lenght = get_program_data(program_file) [5]


print('='*40)
details=[]
i=1
while i < table_lenght:
   name = get_element_data(program_file,i)[0]['NAZWA PLIKU GEO:']
   print (name) 
   wymiary = get_element_data(program_file,i)[0]['WYMIARY:']
   x_index = wymiary.index('x')
   dimension_x = float(wymiary[0:x_index-1])
   dimension_y = float(wymiary[x_index+2:-3])
   print('Wymiar X detalu:',dimension_x,'mm')
   print('Wymiar Y detalu:',dimension_y,'mm')
   cut_time = get_element_data(program_file,i)[0]['CZAS OBRÓBKI:'][0:-4]
   print ('Czas cięcia detalu:',cut_time ,'min') 
   quantity = get_element_data(program_file,i)[0]['ILOŚĆ:']
   print ('Ilość:',quantity) 
   price = 0
   detail = Detail(name, material, thicknes, dimension_x, dimension_y, cut_time, quantity, price = 0)
   details.append(detail)
   print('='*40)
   
   i+=20
print(details[0])