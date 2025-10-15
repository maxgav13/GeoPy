Instrucciones para instalar pyGIMLi y paquetes relacionados en un ambiente virtual con miniconda.

1. Instalar [Positron](https://positron.posit.co/download.html)
2. Instalar [Quarto](https://quarto.org/docs/get-started/)
3. Instalar [miniconda](https://www.anaconda.com/download), le dan “Skip registration” y descargan la versión para su computadora
4. Crear el ambiente para pyGIMLi (“pg”), en el Anaconda Prompt poner: `conda create -n pg -c gimli -c conda-forge "pygimli>=1.5.0”`
5. Activar ambiente “pg”: `conda activate pg`
6. Agregar canales para buscar paquetes: `conda config --add channels gimli --add channels conda-forge`
7. Instalar paquetes obspy, pmw, y pyrefra
    * `conda install obspy`
    * `pip install pmw`
    * `pip install pyrefra`

Para usar el ambiente “pg” en Positron seleccionarlo de la lista de interpretadores arriba a la derecha y abrir el folder del proyecto.

Para usar `refrapick.py` y `refrainv.py`, ya sea en el Anaconda Prompt o Terminal de Positron, ir a la carpeta Refrapy y correr la aplicación con `python Refrapick.py` o `python Refrainv.py`.
Para usar `pyrefra` simplemente escribirlo en el Anaconda Prompt o Terminal de Positron.