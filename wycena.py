import requests as r
from bs4 import BeautifulSoup, Comment


def offert(program_file):
    with open(program_file, "r") as file:
        HTMLFile = file.read()
        soup = BeautifulSoup(HTMLFile, 'html.parser')
        comments = soup.findAll(string = lambda text: isinstance(text, Comment))
        for comment in comments:
            if comment == 'Programm-Nummer und Bemerkung':      #wyszykiwanie danych po komentarzach, bo tylko tak można wyznaczyć dane w tym plik HTML
                table_rows = comment.find_next_sibling('tr')
                b_prog = table_rows.find('b')
                print("Nazwa programu:",b_prog.text)
            
            if comment == 'Material (Technologietabelle)':
                table_rows = comment.find_next_sibling('tr')
                b_mat = table_rows.find('b')
                print("Materiał:",b_mat.text.strip()[:9])

   

program_file = "E:\\Programowanie\\Project\\Wycena\\programy\\ativm2310a10B.HTML"
offert(program_file)