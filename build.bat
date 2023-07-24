pyinstaller --clean --onefile --noconsole --noconfirm --add-data "modules/app.ui;modules" --add-data "modules/icon.ico;modules" --icon "modules/icon.ico" main.py

move "dist\main.exe" "main.exe"

rd /s /q "dist"
rd /s /q "build"
del main.spec