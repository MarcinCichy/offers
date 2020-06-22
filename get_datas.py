import os
#import requests as r
from bs4 import BeautifulSoup, Comment



def offert(program_file):
    with open(program_file, "r") as file:
        HTMLFile = file.read()
        soup = BeautifulSoup(HTMLFile, 'html.parser')
        # wyszykiwanie danych po komentarzach, bo tylko tak można wyznaczyć dane w tym plik HTML
        # plik nie zawira 'id' ani 'class'
        # cały plik podzielony jest na sekcje za pomocą komentarzy
        program_data=[]
        comments = soup.findAll(string = lambda text: isinstance(text, Comment))  # funkcja znajdująca komentarze w pliku html (<!-- --->) 
        for comment in comments:                                        # pętla aby wyszukać z pośród wszytskicj komentarzy, tylko te które nas interesują
            if comment == 'Programm-Nummer und Bemerkung':      
                table_rows = comment.find_next_sibling('tr')
                b_prog_name = table_rows.find('b')
               #  print("Nazwa programu:",b_prog.text)
                program_data.append(b_prog_name.text)

            if comment == 'Material (Technologietabelle)':
                table_rows = comment.find_next_sibling('tr')
                b_mat = table_rows.find('b')
               #  print("Materiał:",b_mat.text.strip()[:9])
                program_data.append(b_mat.text.strip()[:9])

            if comment == 'Maschinenzeit/Tafel':
                table_rows = comment.find_next_sibling('tr')
                b_program_time = table_rows.find('nobr')
                # print("Czas maszynowy programu:",b_time.text.strip())
                program_data.append(b_program_time.text.strip())

            if comment == 'Anzahl Programmdurchlauefe':
                table_rows = comment.find_next('tr')
                tr = table_rows.findAll('td')
                for td in tr:
                   if td.text.strip().isdigit():
                        # print("Ilość powtórzeń programu:",td.text.strip())
                        program_data.append(td.text.strip())
             
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if comment == 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode ':
                table = comment.find_next('table')  # znajduje tabele zaraz po komentarzu: 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode '
                rows = table.findAll('tr')          # przypisuje do zmiennej rows wszystkie znalezione <tr> w tabeli
                details_table_lenght = len(rows)    # ustala długość całej tabeli z danymi poszczególnych detali
             
                i=1                                                                 # zmienna pomocnicza dla iteracji w pęti while
                detail_list=[]                                                      # pusta lista, do której wpisywane będą słowniki z parametrami detali
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
       # print(program_data)    
    return (program_data),(detail_list)            
                            
path_name = os.getcwd()+'\\programy\\'              # ustalenie ścieżki, do katalogu zawierającego przykładowe pliki z programem TruTops
path = os.path.abspath(path_name)                   # ustalenie ścieżki absolutnej
program_file = path+"\\ativm2310a10B.HTML"          # nazwa pliku z programem TruTopspritn
offert(program_file)   



print('='*40)                            # wywołanie funkcji offert
print (offert(program_file)[0][1])
print('='*40)
print (offert(program_file)[1][0]['NAZWA PLIKU GEO:'])
wymiary =  (offert(program_file)[1][1]['WYMIARY:'])
print(wymiary+'|')
print(len(wymiary))
print (offert(program_file)[1][2]['CZAS OBRÓBKI:'])