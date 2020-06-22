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