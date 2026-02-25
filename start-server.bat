@echo off
echo ========================================
echo  Vadavali Local Web Server
echo ========================================
echo.
echo Starting web server at http://localhost:8080
echo.
echo Open your browser and go to:
echo   http://localhost:8080
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python -m http.server 8080

pause
