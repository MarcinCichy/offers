import ntpath

# wmiary detalu
text = '1200.000 x 730.000 mm'
print(len(text))

if 'x' in text:
    x_index = (text.index('x'))
    x_dim = float(text[0:x_index-1])
    y_dim = float(text[x_index+2:-3])
print(x_dim)
print(y_dim)

# nazwa deatalu
name = 'Z:\2019\aluteam\11-10-20119zap\Lustro\Actemium_Abdeckung_Blechbelag\Einlauf_HL8\Blech_2.9.GEO'
print(ntpath.basename(name))


#grubość detalu
mat = 'AlMg3-150'
thicknes = abs(int(mat[-3:])/10)
print(thicknes,'mm')