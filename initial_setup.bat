@echo off

rem Install MySQL
echo Installing MySQL...
start /wait msiexec /i "path\to\mysql_installer.msi" /qn
if errorlevel 1 (
    echo Failed to install MySQL.
    exit /b 1
)
echo MySQL installed successfully.

rem Run MySQL configuration (adjust the command as needed)
echo Configuring MySQL...
start /wait "path\to\mysql\bin\mysql_config.exe" --parameter=value --another-parameter=value
if errorlevel 1 (
    echo Failed to configure MySQL.
    exit /b 1
)
echo MySQL configured successfully.

rem Run Python migration script
echo Running Python migration script...
"path\to\python.exe" "path\to\migrate.py"
if errorlevel 1 (
    echo Python migration script failed.
    exit /b 1
)
echo Python migration script completed successfully.

echo Batch file completed.
exit /b 0
