from get_program_data import get_program_data
from get_element_data import get_element_data
from counts import material_costs, cut_price, suma_per_detail
import os

class Detail:
    def __init__ (self, name, material, thicknes, dimensionX, dimensionY, cut_time, quantity, price, isbending =0):
        self.name = name
        self.material = material
        self.thicknes = thicknes
        self.dimensionX = dimensionX
        self.dimensionY = dimensionY 
        self.cut_time = cut_time
        self.quantity = quantity
        self.price = price
        self.isbending = 0

    def show_data(self):
        print(self.name,self.material,self.thicknes,self.dimensionX,self.dimensionY,self.cut_time,self.quantity,self.price,self.isbending)



path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
# get_program_data(program_file)   

## Pobieranie danych o całym programie
print('='*40)                                   # wywołanie funkcji offert
print ('Nazwa programu:',get_program_data(program_file) [0])      # nazwaprogramu
#print (get_program_data(program_file) [1])      # materiał
material = get_program_data(program_file) [1]
thicknes = get_program_data(program_file) [2]
print('Materiał:',material)
print('Grubość:',thicknes,'mm')

print ('Czas cięcia programu:',get_program_data(program_file) [3])      # czas całego programu
print ('Ilość powtórzeń programu:',get_program_data(program_file) [4])      # ilość powtórzeń programu
# print (get_program_data(program_file) [5])      # ilość wierszy w tabeli

material_weight = 2.8
material_price = 15
cut_hour_price = 420


## Pobiernie danych o detalu
print('='*40)
detail_table_lenght = len(get_element_data(program_file))
#print(get_element_data(program_file)[0])
#detail_object_list=[]
i=0
while i < detail_table_lenght:
    ## --- wyswietlane danych do zast. Objektem 
    ##print(get_element_data(program_file))
    detail_name = get_element_data(program_file)[i]['NAZWA PLIKU GEO:']
    print ('Nazwa detalu:',detail_name)
    dimension_x = get_element_data(program_file)[i]['dim_x']
    dimension_y = get_element_data(program_file)[i]['dim_y']
    print('Wymiar X detalu:',dimension_x,'mm')
    print('Wymiar Y detalu:',dimension_y,'mm')
    cut_time = get_element_data(program_file)[i]['CZAS OBRÓBKI:']
    print ('Czas cięcia detalu:',cut_time,'min')
    quantity = get_element_data(program_file)[i]['ILOŚĆ:']
    print ('Ilość:',quantity,'szt.')
    material =get_element_data(program_file)[i]['mat']
    print('Materiał:',material)
    thicknes = get_element_data(program_file)[i]['thick']
    print('Grubośc:',thicknes,'mm')
    
    mat_cost = material_costs(i,dimension_x,dimension_y,material_price,material_weight, thicknes, cut_time) 
    print('Cena materiału:',mat_cost, 'zł netto/szt.')
    mat_cut_cost = cut_price(i,cut_hour_price,cut_time)
    print('Cena cięcia:',mat_cut_cost, 'zł netto/szt.')
    costs_per_detail = round(suma_per_detail(i,mat_cost,mat_cut_cost),2)
    print('Koszt jednego detalu:', costs_per_detail, 'zł netto/szt.')
    quant_details_cost = round((int(quantity)*costs_per_detail),2)
    print ('Za',quantity,'det.:',quant_details_cost, 'zł netto/szt.') 
    # print (get_element_data(program_file))
    print('-'*40)
    ## detail = Detail(detail_name,material,thicknes,dimension_x,dimension_y,cut_time,quantity,costs_per_detail,0  )
    ## detail_object_list.append(detail)
    i += 1
print('='*40)
## print(detail_object_list)
##detail.show_data()

## class Detail:
##     def __init__ (self, name, material, thicknes, dimensionX, dimensionY, cut_time, quantity, price, isbending =0):
##         self.name = name
##         self.material = material
##         self.thicknes = thicknes
##         self.dimensionX = dimensionX
##         self.dimensionY = dimensionY 
##         self.cut_time = cut_time
##         self.quantity = quantity
##         self.price = price
##         self.isbending = 0