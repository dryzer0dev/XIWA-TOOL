@echo off

echo Installation de Python 3.13.3...
start /wait python-3.13.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

python --version
if errorlevel 1 (
    echo L'installation de Python a échoué !
    exit /b 1
)

echo Exécution de setup.py...
python setup.py

echo Done.

echo Mise à jour de pip...
python -m pip install --upgrade pip

echo Installation des dépendances...
pip install -r requirements.txt

echo Installation terminée!
pause