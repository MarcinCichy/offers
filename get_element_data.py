from get_program_data import get_program_data
import ntpath

class Detail:
    def __init__ (self, name, material, thicknes, dimmensions, cut_time, quantity, price = 0):
        self.name = name
        self.material = material
        self.thicknes = thicknes
        self.dimmensions = dimmensions
        self.cut_time = cut_time
        self.quantity = quantity
        self.price = 0


def get_element_data(program_file,i):
    
    detail_list=[]                                                      # pusta lista, do której wpisywane będą słowniki z parametrami detali
    rows = get_program_data(program_file) [4]                           # pobierz wszystkie wiersze tabeli do dalszej analizy
    start_cell = rows[i].findChildren('td')[1].getText().strip()    # ustanowienie, od której komórki zaczynaja się dane konkretnego detalu
                
                                                            # dane detali przechowywane będą w słownikach, gdzie para klucz wartość, to nazwa komórki tabeli i przypisana dla niej wartość
                                                            # np. |CZAS OBRÓBKI: | 11.83 min |
                                                            # każdy detal będzie miał swój słownik, a słowniki zawarte będą w liście słowników (detali) dla danego programu TruTops

    if start_cell == 'NUMER CZĘŚCI:':                       #jeżeli komórka startowa równa jest "NUMER CZĘŚCI:" (od tej komórki zaczynają się dane detalu)    
        index_of_start_cell = rows.index(rows[i])           # to ustaw index tej komórki (w liście komórek tabeli)
                                                            # print('komórka startowa:',start_cell)   # dla kontroli wyświetlenie zawartości komórki startowej, czy na[ewno jest "NUMER CZĘŚCI:"
                                                            # print('INDEX:',index_of_start_cell)     # dla kontrli podanie indeksu tej komórki, dla każdej części z osobna
        dict_name = 'detal_dict_'+str(index_of_start_cell)  # ustalenie jak mają sie nazywać poszczególne słowniki zawierające dane detalli
                                                            # print(dict_name)  # dla kontroli wyświetlenie nazwy słownika dla danego detalu
        dict_name={}                                        # pusty słownik, do którego wpisywane będą dane z komórek tabeli po przejściu kolejny iteracji poniższej pętli
        for j in range(index_of_start_cell,index_of_start_cell+15): # pętla zaczyna sie od indeksu komórki startowej dla danej części i kończy 15 komórek niżej
            row = rows[j]
            cell_0 = row.findChildren('td')[0].getText().strip()    # komórka w pierwszej kolumnie tabeli, np."" "CZAS OBRÓBKI:'" -> to będzie klucz słownika
            cell_1 = row.findChildren('td')[1].getText().strip()    # komórka w drugiej kolumnie tabeli, np.: "11.83 min" -> to będzie wartość przypisana do klucza
            if cell_0 == 'NAZWA PLIKU GEO:':                        # jeżeli komórk (klucz łownika) ma wartość 'NAZWA PLIKU GEO:' ,to zastosuj
                cell_1 = ntpath.basename(cell_1)                    # funkcję ntpath.basename() w celu wyofdrębnienia nazwy pliku ze ścieżki    
            dict_name[cell_0]=cell_1                                # dodanie do słownika pary cell_0:cell_1 (klucz:wartość)
        detail_list.append(dict_name)                               # po odczytanu wszytstkich wierszy(komórek) dla danego deatlu słownik wpisany zostaje do listy detali programu TruTops  
  
    return (detail_list)     