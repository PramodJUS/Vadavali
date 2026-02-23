@echo off
echo ========================================
echo  Vadavali Data Import from Excel
echo ========================================
echo.
echo Converting Excel to grantha-details.json...
echo.

python excel_to_json.py

echo.
echo ========================================
echo.
echo IMPORTANT: Review grantha-details-new.json before using!
echo.
echo Press any key to close...
pause >nul
