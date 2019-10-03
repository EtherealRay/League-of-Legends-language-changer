pushd %~dp0
ECHO OFF

REM get token from current logged in session
SET COMMAND="wmic process get CommandLine | findstr ""LeagueClient/LeagueClient.exe"""
FOR /F "delims=" %%A IN ('%COMMAND%') DO (
    SET TEMPVAR=%%A
    GOTO :Print 
)

:Print

ECHO %TEMPVAR% > run_league_of_legends.bat



REM run league of legends in en_US
SETLOCAL ENABLEDELAYEDEXPANSION
for /f "delims=" %%a in (run_league_of_legends.bat) do (
    SET s=%%a
    SET s=!s:th_TH=en_US!
    ECHO !s!
)

ECHO !s! > start_league_of_legends.bat