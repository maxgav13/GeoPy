Instrucciones para instalar pyGIMLi y paquetes relacionados en un ambiente virtual con miniconda.

1.  Instalar [Positron](https://positron.posit.co/download.html)
2.  Instalar [Quarto](https://quarto.org/docs/get-started/)
3.  Instalar [miniconda](https://www.anaconda.com/download), le dan “Skip registration” y descargan la versión para su computadora
4.  Crear el ambiente para pyGIMLi (“pg”), en el Anaconda Prompt poner: `conda create -n pg -c gimli -c conda-forge "pygimli>=1.5.0”`
5.  Activar ambiente “pg”: `conda activate pg`
6.  Agregar canales para buscar paquetes: `conda config --add channels gimli --add channels conda-forge`
7.  Instalar paquetes obspy, pmw, y pyrefra
    -   `conda install obspy`
    -   `pip install pmw`
    -   `pip install pyrefra`

En vez de los pasos 4 a 7, pueden correr este comando que hace todo junto:

-   En Windows `conda env create -f environment-win.yml`

-   En Mac `conda env create -f environment-mac.yml`

Para usar el ambiente “pg” en Positron seleccionarlo de la lista de interpretadores arriba a la derecha y abrir el folder del proyecto.

[Refrapy](https://github.com/viictorjs/Refrapy) se puede usar para el picado (picking) de primeros arribos (`refrapick`) e inversión de los datos (`refrainv`). Para usarlo hay que descargar los archivos de GitHub. Para usar `refrapick.py` y `refrainv.py`, ya sea en el Anaconda Prompt o Terminal de Positron, ir a la carpeta "Refrapy" y correr la aplicación con `python Refrapick.py` o `python Refrainv.py`.

[Pyrefra](https://github.com/HZeyen/PyRefra) es un programa de Python que sirve para el picado e inversión. Para usarlo simplemente escribir `pyrefra` en el Anaconda Prompt o Terminal de Positron.