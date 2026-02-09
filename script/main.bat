@echo off
cd ../
call .\venv\Scripts\activate.bat
python main.py
call .\venv\Scripts\deactivate.bat
