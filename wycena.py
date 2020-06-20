import os
import requests as r
from bs4 import BeautifulSoup, Comment


def offert(program_file):
    with open(program_file, "r") as file:
        HTMLFile = file.read()
        soup = BeautifulSoup(HTMLFile, 'html.parser')
        # wyszykiwanie danych po komentarzach, bo tylko tak można wyznaczyć dane w tym plik HTML
        # plik nie zawira 'id' ani 'class'
        # cały plik podzielony jest na sekcje za pomocą komentarzy
        comments = soup.findAll(string = lambda text: isinstance(text, Comment))
        for comment in comments:
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
                print("Czas maszynowy:",b_time.text.strip())

            if comment == 'Anzahl Programmdurchlauefe':
                table_rows = comment.find_next('tr')
                tr = table_rows.findAll('td')
                for td in tr:
                   if td.text.strip().isdigit():
                        print("Ilość powtórzeń programu:",td.text.strip())
                             
            if comment == 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode ':
                table = comment.find_next('table')  # znajduje tabele zaraz po komentarzu: 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode '
                rows = table.findAll('tr')          # przypisuje do zmiennej rows wszystkie znalezione <tr> w tabeli
                print("="*180)
                details_table_lenght = len(rows)
                print(details_table_lenght)
                i=1
                while i < 3:
                    dict1={}
                    for i in range(1,16):
                        row = rows[i]
                        cell_0 = row.findChildren('td')[0].getText().strip()
                        cell_1 = row.findChildren('td')[1].getText().strip()
                        dict1[cell_0]=cell_1
                        #print(cell_0,cell_1)
                        i += 1
                    #print (dict1['NUMER RYSUNKU:'])
                    print (dict1)

                    #print(rows[i].text.strip()) 
                    # row = rows[i]                        # przypisanie do zmiennej row wiersz nr 7
                    # cell = row.findChildren('td')
                    # detail_number = cell[1].getText()    # druga komórka z dwóch w wierszu o numerze 7
                    # print(detail_number) 
                   

                # dict1={}
                # print (rows[6].getText().strip())
                # dict1[]


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
                # odczyt z jednej komórki
                



                # for i in range(1,len(rows)): 
                    
                #     print(rows[i].getText())

                # for row in rows:
                #     cells = row.findChildren('td')
                #     for cell in cells:
                #         print (cell.getText().strip())

                # details_table_lenght = len(rows)

                # while rows < details_table_lenght:
                #     print(rows)
                    # print(row.getText())
                    
                    #print(len(cell))
                #     
                #---------------------------------------
                # for row in rows: 
                #     cells = row.findChildren('td')
                    
                #     for cell in cells:
                #          print(cell.getText())
                        
                print("="*180) 
                   
                
            
path_name = os.getcwd()+'\\programy\\'
path = os.path.abspath(path_name)
program_file = path+"\\ativm2310a10B.HTML"
offert(program_file)