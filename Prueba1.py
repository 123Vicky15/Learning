
import pandas as pd

def readExcel(df):
    try:
        # Lee el archivo CSV y carga su contenido en un DataFrame
        df = pd.read_csv(r"C:\\Users\\MARIA GARCES\\Downloads\\Ratios.csv")
        # Devuelve el DataFrame
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {str(e)}")
        return None

# Ejemplo de uso de la función
if __name__ == "__main__":
    #archivo_csv = "C:\\Users\\MARIA GARCES\\Downloads\\nombre_del_archivo.csv"  # Reemplaza con la ruta completa al archivo CSV
    dataframe = readExcel("C:\\Users\\MARIA GARCES\\Downloads\\Ratios.csv")
    
    if dataframe is not None:
        print("DataFrame creado con éxito:")
        print(dataframe)
