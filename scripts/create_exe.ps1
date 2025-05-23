Remove-Item '.\dist\' -Recurse -ErrorAction Ignore && pyinstaller.exe --onedir --noconsol .\main.py 
