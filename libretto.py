
## #!c:\env\Scripts\python.exe
import args_processor as ap
import jinja2
import yaml 
import os, glob, sys 
import colorama
from termcolor import colored
from utils import * 
from datetime import datetime

DATA_PATH = 'template_work'
TEMPLATES_PATH = 'templates'
SCHEMAS_PATH = 'schemas'
OUTPUT_PATH = 'output'
ENCODING = 'utf-8'
FILE_READ = 'r'
FILE_WRITE = 'w'

def exists_with_value(value):
    return value is not None and len(value) > 0

def load_template(template_file):
    full_template_path = os.path.join(DATA_PATH, TEMPLATES_PATH, template_file)
    if not os.path.exists(full_template_path):
        print_error(f'Template file not found: {template_file}')
        sys.exit(1)

    template_filename = os.path.basename(full_template_path)
    template_path = os.path.dirname(full_template_path)
    template_loader = jinja2.FileSystemLoader(searchpath=template_path, encoding=ENCODING)
    template_env = jinja2.Environment(loader=template_loader, lstrip_blocks=True, trim_blocks=True)

    template_env.filters['exists_with_value'] = exists_with_value

    loaded_template = template_env.get_template(template_filename)

    return loaded_template

def get_schema_files(schema_file):
    schema_files = []

    if not '*' in schema:
        schema_file = os.path.join(DATA_PATH, SCHEMAS_PATH, schema_file)
        if not os.path.exists(schema_file):
            print_error(f'Schema file not found: {schema_file}')
            sys.exit(1)
        schema_files.append(schema_file)
    else:
        schema_path = os.path.join(DATA_PATH, SCHEMAS_PATH, schema_file)
        schema_files = [f for f in glob.glob(schema_path)]
        if len(schema_files) == 0:
            print_error(f'No schema files match pattern {schema_file}')
            sys.exit(1)

    return schema_files

def get_schema_file_contents(schema_file):
    with open(schema_file, FILE_READ, encoding=ENCODING) as f:
        schema_contents = yaml.safe_load(f)

    return schema_contents        

def get_output_file_name(template_arg, schemafile_arg, outdir_arg):
    template_filename, template_extension = os.path.splitext(template_arg)    
    template_filename_only, template_extension_only = os.path.splitext(template_filename)
    base_template_name = os.path.basename(template_filename_only)

    path, filename = os.path.split(schemafile_arg)
    filename_only, filename_extension = os.path.splitext(filename)
    output_path = os.path.join(DATA_PATH, OUTPUT_PATH, outdir_arg)

    # return os.path.join(output_path, base_template_name + '.' + filename_only + template_extension)
    return os.path.join(output_path, filename_only + template_extension)

def get_specified_output_file_name(specified_file_name, outdir_arg):
    full_filename = os.path.join(DATA_PATH, OUTPUT_PATH, outdir_arg, specified_file_name)
    return full_filename

def vscode_debugger_is_active() -> bool:
    """Return true if the debugger is currently active"""
    gettrace = getattr(sys, 'gettrace', lambda : None) 

    return gettrace() is not None

def populate_schema_with_meta_tokens(schema_file_contents):
    schema_file_contents['_datetime'] = datetime.today().strftime('%Y-%b-%d %H:%M:%S')
    schema_file_contents['_template'] = template
    schema_file_contents['_schema'] = schema #.replace('\\','|')

if __name__ == '__main__':
    colorama.init()

    if vscode_debugger_is_active():
        template = r'asna-com-locations\\locations.tpl.html'
        schema = r'asna-com-locations\\locations.json' 
        outdir = 'asna-com-locations'
        filename = ''

    else:      
        template, schema, outdir, filename =  ap.get_command_line_args()

    #print(template) 
    #print(schema) 
    #print(outdir) 

    #exit()


    if not os.path.exists(os.path.join(DATA_PATH, OUTPUT_PATH, outdir )):
        print_error(f'Ouput path does not exists: {outdir}')
        sys.exit(1)

    loaded_template = load_template(template)
    schema_files = get_schema_files(schema)
    output_file_name = ''

    for schema_file in schema_files:
        schema_file_contents = get_schema_file_contents(schema_file)
        populate_schema_with_meta_tokens(schema_file_contents)
        source_output = loaded_template.render(schema_file_contents)

        if filename == '':
            output_file_name = get_output_file_name(template, schema_file, outdir)
        else:            
            output_file_name = get_specified_output_file_name(filename, outdir)                

        #with open(output_file_name, FILE_WRITE, encoding=ENCODING) as outfile:
        #    outfile.write(source_output)
        #print_success(f'Wrote file: {output_file_name}')            
        
        if source_output != '':
            with open(output_file_name, FILE_WRITE, encoding=ENCODING) as outfile:
                outfile.write(source_output)
            print_success(f'Wrote file: {output_file_name}')       
        else:
            print_success(f'** WARNING No file written--no output: {output_file_name}' )                 
        
