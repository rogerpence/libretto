@echo off
REM libretto.py [-h] -t TEMPLATE -s SCHEMA -o OUTDIR [-f FILENAME]
REM Example:
REM    libretto -t mytemplate.tpl.vr -s myschema.json -o myoutputdir
env\scripts\activate && python libretto.py %1 %2 %3 %4 %5 %6  && deactivate


