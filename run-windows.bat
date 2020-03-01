for /f "delims=" %%D in ('dir /a:d /b "%userprofile%\AppData\Local\Programs\Python"') do set pythonDirectory=%userprofile%\AppData\Local\Programs\Python\%%~nxD

%pythonDirectory%\python.exe -m pip install -r requirements.txt

%pythonDirectory%\python.exe main.py

pause