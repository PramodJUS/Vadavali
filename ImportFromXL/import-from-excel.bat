@echo off
echo ========================================
echo  Vadavali Data Import from Excel
echo ========================================
echo.
echo Importing Excel data to grantha-details.json...
echo.

python import_excel_to_json.py

echo.
echo ========================================
echo.
echo Import complete! Data merged into grantha-details.json
echo.
echo Press any key to close...
pause >nul
