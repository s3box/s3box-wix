regasm /codebase .\s3-box-overlay.dll

rem Restart Explorer
taskkill.exe /f /im explorer.exe > nul
start explorer.exe > nul
exit
