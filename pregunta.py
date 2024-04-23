"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #para unificar el formato de fecha se hizo necesario tomar dos, con el año primero y con el año a lo último
    date1 = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce', format='%Y/%m/%d')
    date2 = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce', format='%d/%m/%Y')
    #luego se unen los dos df de fechas
    df['fecha_de_beneficio'] = date1.fillna(date2)

    #para el monto se quitó el signo pesos, quitar la coma y tomar la parte entera
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x : int(x.replace("$","").replace(",","").split(".")[0]))

    #Cambios en las columnas de texto: poner en minúscula y reemplazar - y _ por espacio
    df["sexo"]=df["sexo"].str.lower()
    df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"]=df["idea_negocio"].str.replace('-', ' ').str.replace('_', ' ').str.lower()
    df["barrio"]=df["barrio"].str.replace('-', ' ').str.replace('_', ' ').str.lower()
    df["línea_credito"]=df["línea_credito"].str.replace('-', ' ').str.replace('_', ' ').str.lower()

    #eliminación de duplicados
    df=df.drop_duplicates(subset=["sexo","tipo_de_emprendimiento", "idea_negocio", "barrio", "estrato", "comuna_ciudadano", "fecha_de_beneficio", "monto_del_credito", "línea_credito"])

    #eliminación de registros con valores nulos
    df = df.dropna()
    return df
