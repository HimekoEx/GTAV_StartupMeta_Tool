@echo off

REM 设置入口文件名和图标文件名
set ENTRY_FILE=src\Main.py
set ICON_FILE=resource\icon.ico
set APP_NAME=GTAV战局锁工具

REM 清理之前的构建结果
rmdir /s /q dist
rmdir /s /q build
del /f /q %APP_NAME%.spec
del /f /q %APP_NAME%.exe

REM 执行PyInstaller命令
pyinstaller --onefile --icon=%ICON_FILE% %ENTRY_FILE% --name=%APP_NAME% --clean

REM 移动可执行文件到根目录
move dist\%APP_NAME%.exe .

REM 删除其他缓存文件夹
rmdir /s /q build
rmdir /s /q dist
del /f /q %APP_NAME%.spec

echo Build completed.
pause
