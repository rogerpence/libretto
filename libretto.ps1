# libretto.py [-h] -t TEMPLATE -s SCHEMA -o OUTDIR [-f FILENAME]
# Example:
#     libretto -t mytemplate.tpl.vr -s myschema.json -o myoutputdir
env\scripts\activate
python libretto.py $args[0] $args[1] $args[2] $args[3] $args[4] $args[5] 
deactivate


