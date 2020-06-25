from get_program_data import get_program_data
import ntpath

class Detail:
    def __init__ (self, name, material, thicknes, dimension_x, dimension_y, cut_time, quantity, price = 0, num_of_bends = 0):
        self.name = name
        self.material = material
        self.thicknes = thicknes
        self.dimensions_x = dimension_x
        self.dimension_y = dimension_y
        self.cut_time = cut_time
        self.quantity = quantity
        self.price = 0
        self.num_of_bends = 0

    def show_data(self):
        print(self.name,self.material,self.thicknes,self.dimension_x,self.dimension_y,self.cut_time,self.quantity,self.price,self.num_of_bends)

def get_element_data(program_file):
    
    i=1                                                                 # zmienna pomocnicza dla iteracji w pęti while
    details_list=[] 
    one_detail_list =[]                                                     # pusta lista, do której wpisywane będą słowniki z parametrami detali
    detail_table_lenght = len(get_program_data(program_file) [5])       # przy pomocy zew. funkcji get_program_data pobierz ilość komórek w tabeli
    rows = get_program_data(program_file) [5]                           # pobierz wszystkie wiersze tabeli do dalszej analizy
    while i < detail_table_lenght:                                      # iteracja do momentu, gdy zmienna i nie osiągnie dlugości tabeli, po to aby wczytać wszystkie wiersze tabeli
        start_cell = rows[i].findChildren('td')[1].getText().strip()    # ustanowienie, od której komórki zaczynaja się dane konkretnego detalu
                    
                                                                        # dane detali przechowywane będą w słownikach, gdzie para klucz wartość, to nazwa komórki tabeli i przypisana dla niej wartość
                                                                        # np. |CZAS OBRÓBKI: | 11.83 min |
                                                                        # każdy detal będzie miał swój słownik, a słowniki zawarte będą w liście słowników (detali) dla danego programu TruTops

        if start_cell == 'NUMER CZĘŚCI:':                               #jeżeli komórka startowa równa jest "NUMER CZĘŚCI:" (od tej komórki zaczynają się dane detalu)    
            index_of_start_cell = rows.index(rows[i])                   # to ustaw index tej komórki (w liście komórek tabeli)
                                                                        # print('komórka startowa:',start_cell)   # dla kontroli wyświetlenie zawartości komórki startowej, czy na[ewno jest "NUMER CZĘŚCI:"
                                                                        # print('INDEX:',index_of_start_cell)     # dla kontrli podanie indeksu tej komórki, dla każdej części z osobna
            #dict_name = 'detal_dict_'+str(index_of_start_cell)          # ustalenie jak mają sie nazywać poszczególne słowniki zawierające dane detalli
            # -- ponizej część kodu odp. za odczyt komórek i dodwanie ich do słownika                                                            # print(dict_name)  # dla kontroli wyświetlenie nazwy słownika dla danego detalu
            dict_name={}   
            thick = None    
            mat = None                                         # pusty słownik, do którego wpisywane będą dane z komórek tabeli po przejściu kolejny iteracji poniższej pętli
            for j in range(index_of_start_cell,index_of_start_cell+15): # pętla zaczyna sie od indeksu komórki startowej dla danej części i kończy 15 komórek niżej
                row = rows[j]
                cell_0 = row.findChildren('td')[0].getText().strip()    # komórka w pierwszej kolumnie tabeli, np."" "CZAS OBRÓBKI:'" -> to będzie klucz słownika
                cell_1 = row.findChildren('td')[1].getText().strip()    # komórka w drugiej kolumnie tabeli, np.: "11.83 min" -> to będzie wartość przypisana do klucza
                if cell_0 == 'NAZWA PLIKU GEO:':                        # jeżeli komórk (klucz łownika) ma wartość 'NAZWA PLIKU GEO:' ,to zastosuj# jeżeli komórk (klucz łownika) ma wartość 'NAZWA PLIKU GEO:' ,to zastosuj
                    name = ntpath.basename(cell_1)                      # funkcję ntpath.basename() w celu wyofdrębnienia nazwy pliku ze ścieżki 
                    dict_name[cell_0] = name                            # dodanie do słownika pary cell_0:cell_1 (klucz:wartość)
                if cell_0 == 'ILOŚĆ:':
                    quantity = int(cell_1)
                    dict_name[cell_0] = quantity
                if cell_0 == 'WYMIARY:':
                    dimensions = cell_1
                    x_index = dimensions.index('x')
                    dimension_x = round(float(dimensions[0:x_index-1]),2)
                    dimension_y = round(float(dimensions[x_index+2:-3]),2)
                    dict_name['dim_x'] = dimension_x
                    dict_name['dim_y'] = dimension_y
                if cell_0 == 'CZAS OBRÓBKI:':
                    cut_time = float(cell_1[0:5])     
                    dict_name[cell_0] = cut_time
            thicknes = get_program_data(program_file) [2] 
            dict_name['thick'] = thicknes
            material = get_program_data(program_file) [1]       
            dict_name['mat'] = material
            details_list.append(dict_name)  
            #detail[i] = Detail(name,material,thicknes,dimension_x,dimension_y,cut_time,quantity,price=0,num_of_bends=0)                             # po odczytanu wszytstkich wierszy(komórek) dla danego deatlu słownik wpisany zostaje do listy detali programu TruTops  

        i += 1   
                                                      # zwiększenie o 1 zmiennej iteracyjnej i dla pętli while
    return (details_list)             
              