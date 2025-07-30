import glob
import pandas as pd

carpeta = r'C:\Users\Usuario\OneDrive\Desktop\proyecto-final\archive'
filenames = glob.glob(carpeta + "/*.csv")

archivos_csv = []
for filename in filenames:
    archivos_csv.append(pd.read_csv(filename))

big_frame = pd.concat(archivos_csv, ignore_index=True)

forma = big_frame.shape
print("forma del dataframe: " , forma)
    
tipos_datos = big_frame.dtypes
print("tipos de datos: ", tipos_datos)
    
valores_nulos = big_frame.isnull().sum()
print("valores nulos del dataframe: ", valores_nulos)
