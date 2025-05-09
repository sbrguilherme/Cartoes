
@echo off
echo Verificando dependências...

python -m pip install --upgrade pip >nul
pip install -r requirements.txt >nul

echo Iniciando o aplicativo Streamlit...
streamlit run app.py
pause
