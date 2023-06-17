import os
import win32com.client as win32

excel = win32.Dispatch("excel.Application")
excel.Visible = True

workbook = excel.Workbooks.Add()
workbook.SaveAs(os.path.join(os.getcwd(), "hoja1.xlsx"))

sheet1 = workbook.Worksheets("Sheet1")
sheet1.name = "Deposito"
sheet1.Range("A:D").ColumnWidth = 30

cells = sheet1.Cells

# Contenido de las celdas principales
cells(1, "A").Value = "Client ID"
cells(1, "A").Font.Bold = True
cells(1, "B").Value = "Nombre"
cells(1, "B").Font.Bold = True
cells(1, "C").Value = "Apellido"
cells(1, "C").Font.Bold = True
cells(1, "D").Value = "Direccion"
cells(1, "D").Font.Bold = True
cells(1, "E").Value = "Box"
cells(1, "E").Font.Bold = True
cells(1, "F").Value = "Box $"
cells(1, "F").Font.Bold = True
cells(1, "G").Value = "Mini"
cells(1, "G").Font.Bold = True
cells(1, "H").Value = "Extras"
cells(1, "H").Font.Bold = True
cells(1, "I").Value = "Extras $"
cells(1, "I").Font.Bold = True

cells(1, "L").Value = "Precio Box"
cell_box = cells(2, "L").Value = 2900
cells(1, "M").Value = "Precio Mini"
precio_mini = cells(2, "M").Value = 2000

# Contenido de las celdas secundarias
cells(2, "A").Value = 1
cells(2, "B").Value = "Bruno"
cells(2, "C").Value = "Ruiz Talamo"
cells(2, "D").Value = "Hipolito Yrigoyen 2442"
cells(2, "E").Value = 2
cells(2, "F").Formula = "=L2*E2"
cells(2, "G").Value = 7
cells(2, "H").Value = "Ruiz Talamo"
cells(2, "I").Formula = "=M2*G2"

cells(3, "A").Value = 3
cells(3, "B").Value = "Alicia"
cells(3, "C").Value = "Gonzalez"
cells(3, "D").Value = "Rio Negro 3713"
cells(3, "E").Value = 15
cells(3, "F").Formula = "=L3*E3"
cells(3, "G").Value = 3
cells(3, "H").Value = "Alicia"
cells(3, "I").Formula = "=M3*G3"

cells(4, "A").Value = 4
cells(4, "B").Value = "Jose"
cells(4, "C").Value = "Martinez"
cells(4, "D").Value = "Buenos Aires 2736"
cells(4, "E").Value = 9
cells(4, "F").Formula = "=L4*E4"
cells(4, "G").Value = 3
cells(4, "H").Value = "Alicia"
cells(4, "I").Formula = "=M4*G4"


cells(5, "A").Value = 2
cells(5, "B").Value = "Juan Cruz"
cells(5, "C").Value = "Rodriguez"
cells(5, "D").Value = "Colon 1733"
cells(5, "E").Value = 11
cells(5, "F").Formula = "=L5*E5"
cells(5, "G").Value = 3
cells(5, "H").Value = "Alicia"
cells(5, "I").Formula = "=M5*G5"

#Si quiero sumar celdas, "cells(6, "A").Value = =SUM(E2:F4)" --> suma celdas en E y F
#Tambien puedo hacer "cells(6, "A").sValue = =SUM(E2:E4)"


# Crear el primer gráfico
chart1 = sheet1.Shapes.AddChart()
chart1.Chart.SetSourceData(Source=sheet1.Range("E:E"), PlotBy=2)
chart1.Chart.ChartType = 63
chart1.Name = "Boxes"

# Crear el segundo gráfico
chart2 = sheet1.Shapes.AddChart()
chart2.Chart.SetSourceData(Source=sheet1.Range("F:F"), PlotBy=2)
chart2.Chart.ChartType = 63
chart2.Name = "Minis"

# Crear el tercer gráfico
chart3 = sheet1.Shapes.AddChart()
chart3.Chart.SetSourceData(Source=sheet1.Range("G:G"), PlotBy=2)
chart3.Chart.ChartType = 63
chart3.Name = "Boxes $"

# Crear el cuarto gráfico
chart4 = sheet1.Shapes.AddChart()
chart4.Chart.SetSourceData(Source=sheet1.Range("H:H"), PlotBy=2)
chart4.Chart.ChartType = 63
chart4.Name = "Minis $"
workbook.SaveAs(os.path.join(os.getcwd(), "hoja1.xlsx"))

# Crear una función para manejar el evento SheetChange
def on_sheet_change(target):
    # Verificar si la celda modificada se encuentra en el rango de interés (por ejemplo, L2 y F2)
    if target.Address == "$L$2" or target.Address == "$F$2":
        # Obtener los nuevos valores de las celdas L2 y F2
        precio_box = cells(2, "L").Value
        extras = cells(2, "F").Value

        # Realizar el cálculo de multiplicación
        resultado = precio_box * extras

        # Actualizar el valor de la celda X2 con el resultado de la multiplicación
        cells(2, "X").Value = resultado

# Asignar la función on_sheet_change al evento SheetChange
sheet1.OnSheetChange = on_sheet_change

# ... código posterior ...

# Guardar el archivo Excel con los cambios realizados
workbook.Save()

# Cerrar la aplicación de Excel
excel.Quit()