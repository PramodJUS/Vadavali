@echo off
echo ========================================
echo  Vadavali Data Export to Excel
echo ========================================
echo.
echo Converting grantha-details.json to Excel...
echo.

python json_to_excel.py

echo.
echo ========================================
echo Press any key to close...
pause >nul
