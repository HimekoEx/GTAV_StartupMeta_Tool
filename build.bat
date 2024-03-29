@echo off

REM 设置入口文件名和图标文件名
set ENTRY_FILE=src\MainWindow.py
set ICON_FILE=src\res\icon_512.ico
set ADD_DATA=src\res:res
set APP_NAME=GTAV_SMT

REM 清理之前的构建结果
rmdir /s /q dist
rmdir /s /q build
del /f /q %APP_NAME%.spec
del /f /q %APP_NAME%.exe

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 执行PyInstaller命令
pyinstaller -F -w --onefile --icon=%ICON_FILE% ^
 --add-data=%ADD_DATA% %ENTRY_FILE% --name=%APP_NAME% --clean

REM 移动可执行文件到根目录
move dist\%APP_NAME%.exe .

REM 删除其他缓存文件夹
rmdir /s /q build
rmdir /s /q dist
del /f /q %APP_NAME%.spec

echo Build completed...
pause
