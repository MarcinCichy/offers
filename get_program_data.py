import os
from bs4 import BeautifulSoup, Comment


def get_program_data(program_file):
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
                program_data.append(b_program_time.text.strip()[0:-9]) # usunięcie z napisu '[h:min:s]

            if comment == 'Anzahl Programmdurchlauefe':
                table_rows = comment.find_next('tr')
                tr = table_rows.findAll('td')
                for td in tr:
                   if td.text.strip().isdigit():
                        # print("Ilość powtórzeń programu:",td.text.strip())
                        program_data.append(td.text.strip())

            if comment == 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode ':
                table = comment.find_next('table')  # znajduje tabele zaraz po komentarzu: 'HTML-Block: Einzelteil-Informationen mit Grafiken, ohne Barcode '
                rows = table.findAll('tr')          # przypisuje do zmiennej rows wszystkie znalezione <tr> w tabeli
                program_data.append(rows)
                details_table_lenght = len(rows)    # ustala długość całej tabeli z danymi poszczególnych detali
                program_data.append(details_table_lenght)
        return (program_data)