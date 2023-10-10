import pandas as pd

def leer_csv_y_crear_dataframe(archivo_csv):
    try:
        # Lee el archivo CSV y carga su contenido en un DataFrame
        df = pd.read_csv(archivo_csv)
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {str(e)}")
        return None

# Ejemplo de uso de la función
if __name__ == "__main__":
    archivo_csv = "C:\\Users\\MARIA GARCES\\Downloads\\Ratios.csv"  # Reemplaza con la ruta completa al archivo CSV
    dataframe = leer_csv_y_crear_dataframe(archivo_csv)
    
    if dataframe is not None:
        print("DataFrame creado con éxito:")
        print(dataframe)
