from get_program_data import get_program_data as gpd

class Detail:
    def __init__ (self, name, material, thicknes, dimmensions, cut_time, quantity, price = 0):
        self.name = name
        self.material = material
        self.thicknes = thicknes
        self.dimmensions = dimmensions
        self.cut_time = cut_time
        self.quantity = quantity
        self.price = 0


def get_element_data():
    i=1                                                                 # zmienna pomocnicza dla iteracji w pęti while
    detail_list=[] 
    detail_table_lenght = gpd.details_table_lenght 
                                                     # pusta lista, do której wpisywane będą słowniki z parametrami detali
    while i < detail_table_lenght:                                     # iteracja do momentu, gdy zmienna i nie osiągnie dlugości tabeli, po to aby wczytać wszystkie wiersze tabeli
        start_cell = gpd.rows[i].findChildren('td')[1].getText().strip()    # ustanowienie, od której komórki zaczynaja się dane konkretnego detalu
                    
                    # dane detali przechowywane będą w słownikach, gdzie para klucz wartość, to nazwa komórki tabeli i przypisana dla niej wartość
                    # np. |CZAS OBRÓBKI: | 11.83 min |
                    # każdy detal będzie miał swój słownik, a słowniki zawarte będą w liście słowników (detali) dla danego programu TruTops

        if start_cell == 'NUMER CZĘŚCI:':                       #jeżeli komórka startowa równa jest "NUMER CZĘŚCI:" (od tej komórki zaczynają się dane detalu)    
            index_of_start_cell = gpd.rows.index(gpd.rows[i])           # to ustaw index tej komórki (w liście komórek tabeli)
                                                                # print('komórka startowa:',start_cell)   # dla kontroli wyświetlenie zawartości komórki startowej, czy na[ewno jest "NUMER CZĘŚCI:"
                                                                # print('INDEX:',index_of_start_cell)     # dla kontrli podanie indeksu tej komórki, dla każdej części z osobna
            dict_name = 'detal_dict_'+str(index_of_start_cell)  # ustalenie jak mają sie nazywać poszczególne słowniki zawierające dane detalli
                                                                # print(dict_name)  # dla kontroli wyświetlenie nazwy słownika dla danego detalu
            dict_name={}                                        # pusty słownik, do którego wpisywane będą dane z komórek tabeli po przejściu kolejny iteracji poniższej pętli
            for j in range(index_of_start_cell,index_of_start_cell+15): # pętla zaczyna sie od indeksu komórki startowej dla danej części i kończy 15 komórek niżej
                row = gpd.rows[j]
                cell_0 = row.findChildren('td')[0].getText().strip()    # komórka w pierwszej kolumnie tabeli, np."" "CZAS OBRÓBKI:'" -> to będzie klucz słownika
                cell_1 = row.findChildren('td')[1].getText().strip()    # komórka w drugiej kolumnie tabeli, np.: "11.83 min" -> to będzie wartość przypisana do klucza
                dict_name[cell_0]=cell_1                                # dodanie do słownika pary cell_0:cell_1 (klucz:wartość)
            detail_list.append(dict_name)                               # po odczytanu wszytstkich wierszy(komórek) dla danego deatlu słownik wpisany zostaje do listy detali programu TruTops  
        i += 1                                                          # zwiększenie o 1 zmiennej iteracyjnej i dla pętli while
       # print(program_data)    
    return (detail_list)             
                