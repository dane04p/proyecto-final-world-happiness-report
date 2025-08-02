import glob
import pandas as pd

carpeta = r'C:\Users\Prestamo\Desktop\Yerlin\Curso_Python\Proyecto_final\archive'
filenames = glob.glob(carpeta + "/*.csv")

archivos_csv = []
for filename in filenames:
    try:
        data = pd.read_csv(filename)
        archivos_csv.append(pd.read_csv(filename))
        print(f"Archivo cargado correctamente: {filename}")
    except Exception as e:
        print(f"Error al cargar: {filename} por: {e}")
        
big_frame = pd.concat(archivos_csv, ignore_index=True)

print(f"\nTotal de archivos procesados: {len(archivos_csv)}")

forma = big_frame.shape
print(f"\nForma del dataframe: {forma}")
    
print("\nTipos de datos: ")
tipos_datos = big_frame.dtypes
print(tipos_datos)

print("\nValores nulos del dataframe: ")
valores_nulos = big_frame.isnull().sum()
print(valores_nulos)
