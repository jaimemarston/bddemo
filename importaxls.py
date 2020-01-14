import xlrd
from datetime import *
from conn import * 


import xlrd

book = xlrd.open_workbook("E:\proyectosdjango\Insumos_app_inventarios\prueba.xlsx")
#book = xlrd.open_workbook(sys.argv[3])

print "proceso"
#print "The number of worksheets is", book.nsheets
#print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(0)
print "Libro:",sh.name,"Registros:", sh.nrows,"Columnas:", sh.ncols
insertadatos = [] #empty list
empdatos = {} #empty dictionary

nreg=0
for rx in range(1,sh.nrows):
    vxls1=sh.cell_value(rowx=rx, colx=0)
    vxls2=sh.cell_value(rowx=rx, colx=1)
    vxls3=sh.cell_value(rowx=rx, colx=2)
    vxls4=sh.cell_value(rowx=rx, colx=3)
    vxls5=sh.cell_value(rowx=rx, colx=4)
    vxls6=sh.cell_value(rowx=rx, colx=5)
    vxls7=sh.cell_value(rowx=rx, colx=6)
    nreg +=1
    empdatos={'codigo':vxls1,'registro':str(nreg).zfill(4),'td':vxls2,'destd':vxls3,'codemp':vxls4,'nombre':vxls5,'hrae1':vxls6,'hras1':vxls7,
              'estadoregistro':1,'idemp':1}

    insertadatos.append(empdatos)

print insertadatos

#i = tble286.insert()
#i.execute(insertadatos)


