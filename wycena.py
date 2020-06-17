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
                             



            
path_name = os.getcwd()+'\\programy\\'
path = os.path.abspath(path_name)
program_file = path+"\\ativm2310a10B.HTML"
offert(program_file)