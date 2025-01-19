"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import os
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    output_dir = "files/plots"
    try:
        os.makedirs(output_dir, exist_ok=False)
    except Exception as e:
        print(f"Error al crear el directorio {output_dir}: {e}")
        return
    
    plt.figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2, 
    }

    #Cargar los datos desde el archivo csv
    try:
        df = pd.read_csv("files/input/news.csv", index_col=0)
    except FileNotFoundError:
        print("Error al cargar el archivo csv: {e}")
        return
    
    #Crear el gráfico
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col, 
            zorder=zorder[col], 
            linewidths=linewidths[col]
        )

    plt.title("How people get their news", fontsize = 16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            first_year -0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )

        plt.text(
            last_year +0.2,
            df[col][last_year],
            str(df[col][first_year]) + "%",
            ha='left',
            va='center',
            color=colors[col],
        )

    plt.tight_layout()

    #Guardar el gráfico en el archivo
    output_file = os.path.join(output_dir, "news.png")
    try:
        plt.savefig(output_file)
        print(f"Gráfico guardado exitosamente en {output_file}")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")
    finally:
        plt.close()

    if __name__ =="__main__":
        #Rutas de entrada y de salida

        #Llamar a la función
        print(pregunta_01())
