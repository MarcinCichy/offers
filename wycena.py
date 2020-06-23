import os
import ntpath
import requests as r
from bs4 import BeautifulSoup, Comment


def get_detail_name(detail_name):
    print(ntpath.basename(detail_name))

def offert(program_file):
    with open(program_file, "r") as file:
        HTMLFile = file.read()
        soup = BeautifulSoup(HTMLFile, 'html.parser')
        # wyszykiwanie danych po komentarzach, bo tylko tak można wyznaczyć dane w tym plik HTML
        # plik nie zawira 'id' ani 'class'
        # cały plik podzielony jest na sekcje za pomocą komentarzy
        comments = soup.findAll(string = lambda text: isinstance(text, Comment))  # funkcja znajdująca komentarze w pliku html (<!-- --->) 
        for comment in comments:                                        # pętla aby wyszukać z pośród wszytskicj komentarzy, tylko te które nas interesują
            if comment == 'Programm-Nummer und Bemerkung':      
                table_rows = comment.find_next_sibling('tr')
                b_prog = table_rows.find('b')
                print("Nazwa programu:",b_prog.text)
            
            if comment == 'Material (Technologietabelle)':
                table_rows = comment.find_next_sibling('tr')
                b_mat = table_rows.find('b')
                print("Materiał:",b_mat.text.strip()[:9])

            if comment == 'Maschinenzeit/Tafel':
                table_rows = comment.find_next_sibling('tr')
                b_time = table_rows.find('nobr')
                print("Czas maszynowy programu:",b_time.text.strip())

            if comment == 'Anzahl Programmdurchlauefe':
                table_rows = comment.find_next('tr')
                tr = table_rows.findAll('td')
                for td in tr:
                   if td.text.strip().isdigit():
                        print("Ilość powtórzeń programu:",td.text.strip())
                             
            if comment == 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode ':
                table = comment.find_next('table')  # znajduje tabele zaraz po komentarzu: 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode '
                rows = table.findAll('tr')          # przypisuje do zmiennej rows wszystkie znalezione <tr> w tabeli
                print("="*130)
                details_table_lenght = len(rows)    # ustala długość całej tabeli z danymi poszczególnych detali
                # print(details_table_lenght)
                # start_cell = rows[1].findChildren('td')[1].getText().strip()
                # index = rows.index(rows[1])
                # print('komórka startowa:',start_cell)
                # print(index)


                i=1                                                                 # zmienna pomocicza dla iteracji w pęti while
                detail_list=[]                                                      # pusta lista, do której wpisyane będą słowniki z parametrami detali
                while i < details_table_lenght:                                     # iteracja do momentu, gdy zmienna i nie osiągnie dlugości tabeli, po to aby wczytać wszystkie wiersze tabeli
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
                            dict_name[cell_0]=cell_1                                # dodanie do słownika pary cell_0:cell_1 (klucz:wartość)
                        detail_list.append(dict_name)                               # po odczytanu wszytstkich wierszy(komórek) dla danego deatlu słownik wpisany zostaje do listy detali programu TruTops  
                    i += 1                                                          # zwiększenie o 1 zmiennej iteracyjnej i dla pętli while
                
                # poniżej kontrolne wyświetlenie listy wszytskich detali z programu i ch parametrów
                # oraz jednego konkretnego(dla przykładu) parametru którgoś z detali
                for k in range (0,len(detail_list)):
                    print(detail_list[k])
                    print("-"*130)
                print(detail_list[2]['WYMIARY:'])
# poniżej próby wyświetlania różnych wartości z tabeli
                #print(rows)                         # wypisuje wszystkie wiersze <tr> bez formatowania
                #nr_czesci = rows[1].text.strip()
                #wymiary = rows[6].text.strip()`
                #print(nr_czesci)
                #print(wymiary)
                #print(rows[3].text.strip())        # wypisuje cały wiersz z formatowaniem -> sam tekst z wiersza (obie komórki), pozycja o indexie 3 z tabeli 'rows'
                #---------------------------------------
                # for i in range(1,21):             # odczyt całej jednej tabeli -> jeden detal 
                #     row = rows[i]                 # dla wierszy od 1 do 20
                #     print(row.getText())
                #---------------------------------------
                # odczyt z jednej komórki
                # row = rows[7]                        # przypisanie do zmiennej row wiersz nr 7
                # cell = row.findChildren('td')
                # detail_number = cell[1].getText()    # druga komórka z dwóch w wierszu o numerze 7
                # print(detail_number) 
                #---------------------------------------`
                print("="*130) 
                   
                            
path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTops
offert(program_file)                                # wywołanie funkcji offert



