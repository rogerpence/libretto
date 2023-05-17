
## Libretto 2023

The Libretto is a template-based code generator written in Pyhon. It reads a Json schema and a [Jinja3 template](https://jinja.palletsprojects.com/en/3.0.x/) to produce a source file. 

* **Generate many output files at once**. Libretto can version can read all of the schemas in a directory and produce and output file for each schema found--or you can produce code for a Json single schema.  
* **Language agnostic**. The Libretto works with any Json schema you throw at it. 
* **Vastly better templating capabilities**. The Libretto uses the very popular [Jinja3 template engine](https://jinja2docs.readthedocs.io/en/stable/). You can use all of its cool filters and other features in Libretto templates. 

This version of Libretto is a command-line only version. This core engine is written in Python (which is freely available for all platforms including [Windows 10](https://www.python.org/downloads/windows/)). There is a point-and-click UI for it (see below for more information).

### What does Libretto do

Given a Json schema and a template, it produces an output file for use with your favorite compiler or intepreter. 

![](https://rogerpence.dev/wp-content/uploads/2022/03/l0CkJzFwxz.png)

Schema file: `examples.states.json`

```
{
  "dbname": "*public/dg net local",
  "library": "examples",
  "file": "states",
  "format": "rstates",
  "description": "",
  "type": "physical",
  "recordlength": "50",
  "keylength": "48",
  "basefile": "",
  "duplicatekeys": "not allowed",
  "sqlserveruniqueindex": "unique",
  "alias": "states",
  "keyfieldslist": "state",
  "allfieldslist": "state, abbrev",
  "fields": [
    {
      "name": "state",
      "description": "",
      "alias": "state",
      "fulltype": "Type(*char) Len(48)",
      "type": "*char",
      "length": "48",
      "decimals": "",
      "systemtype": "System.String",
      "iskey": true,
      "keyposition": 0,
      "allownull": false,
      "sqlservertype": "varchar(48)",
      "sqlservernull": "NOT NULL",
      "sqlserverprimarykey": "PRIMARY KEY"
    },
    {
      "name": "abbrev",
      "description": "",
      "alias": "abbrev",
      "fulltype": "Type(*char) Len(2)",
      "type": "*char",
      "length": "2",
      "decimals": "",
      "systemtype": "System.String",
      "iskey": false,
      "keyposition": -1,
      "allownull": false,
      "sqlservertype": "varchar(2)",
      "sqlservernull": "NOT NULL",
      "sqlserverprimarykey": ""
    }
  ],
  "keyfields": [
    {
      "name": "state",
      "description": "",
      "alias": "state",
      "fulltype": "Type(*char) Len(48)",
      "type": "*char",
      "length": "48",
      "decimals": "",
      "systemtype": "System.String",
      "iskey": true,
      "keyposition": 0,
      "allownull": false,
      "sqlservertype": "varchar(48)",
      "sqlservernull": "NOT NULL",
      "sqlserverprimarykey": "PRIMARY KEY"
    }
  ],
  "nonkeyfields": [
    {
      "name": "abbrev",
      "description": "",
      "alias": "abbrev",
      "fulltype": "Type(*char) Len(2)",
      "type": "*char",
      "length": "2",
      "decimals": "",
      "systemtype": "System.String",
      "iskey": false,
      "keyposition": -1,
      "allownull": false,
      "sqlservertype": "varchar(2)",
      "sqlservernull": "NOT NULL",
      "sqlserverprimarykey": ""
    }
  ]
}
```

Template file: `file-schema.tpl.txt`

```
Database Name.: {{dbname}}
Library.......: {{library}}
File..........: {{file}}
Format........: {{format}}
Key field(s)..: {{keyfieldslist}}
Type..........: {{type}}
Base file.....: {{basefile}}
Description...: {{description}}
Record length.: {{recordlength}}

Field name        Data type                    Description
----------------------------------------------------------------------------
{% if keyfields|length > 0 %}
{% for field in keyfields %}
{{field.name.ljust(17)}} {{field.fulltype.ljust(28)}} {{field.description}}
{% endfor %}

{% endif %}
{% for field in nonkeyfields %}
{{field.name.ljust(17)}} {{field.fulltype.ljust(28)}} {{field.description}}
{% endfor %}
----------------------------------------------------------------------------
```

The Schema and Template above produce this file: `file-schema.examples.states.txt`

```
Database Name.: *public/dg net local
Library.......: examples
File..........: states
Format........: rstates
Key field(s)..: state
Type..........: physical
Base file.....: 
Description...: 
Record length.: 50

Field name        Data type                    Description
----------------------------------------------------------------------------
state             Type(*char) Len(48)          
abbrev            Type(*char) Len(2)           
----------------------------------------------------------------------------
```

### Naming conventions

The template naming file convention is:

```
*.tpl.xxx
```

where '*' is the file name and 'xxx' is the extension used for the output file. 

The convention for schema file names is:

```
[database].[table].json
```

If template is named `file-schema.tpl.txt`. Using the schema named `examples.cmastnewl2.json` with that template results in this output file name:

```
file-schema.examples.cmastnewl2.txt
```

Generally, you should be able to look at an output file and be able to quickly determine:

The template name from which it was derived
The database and table for which the output file applies
What language the template its is for (with its extension)

### Producing the output 

To produce this output you would either: 

Run this command line from the `libretto.py` parent folder:

```
Python libretto.py -t "file-schema.tpl.txt" -s "datagate_examples\examples_states.json" -o "datagate"
```
or use the LibrettoUI point-and-click UI:

![](https://rogerpence.dev/wp-content/uploads/2022/03/LibrettoUI-2_JDLQCnt93S.png)

The LibrettoUIX point-and-click interface is a relatively new addition to Libretto. [Read more about it here.](https://github.com/rogerpence/librettoUIX) This UI is a Windows WPF application that is essentially a front-end that builds the command lines that `libretto.py` needs. This UI doesn't directly perform template translation, under the covers it launches a process that runs `libretto.py` to do that.

### Command line arguments

#### --template, -t

Template files are expected to be in the `template_work\templates` folder directly under the `libretto.py` script file.

This specifies the Jinja template to use. 

#### --schema, -s 

Template files are expected to be in the `template_work\schemas` folder directly under the `libretto.py` script file.

Schema files provide the primary data for a Jinja2 template. Schema files can be either `Json` or `Yaml` format. 


This specifies the schema file used. It can be either be a single file:

    -s schema/examples_cmastnewl2.yaml

or multiple files 

    -s schema/examples_*.json

When multiple files are specified, the template processor prompts for prompted values once before all the schema files are processed (thereby ensuring that the template uses the same value for every schema file in the group).

#### --outdir, -o 

Output is produced in a directory relative to the `template_work\output` directory.

### LibrettoX paths

All LibrettoX paths assumes that in the folder where `libretto.py` resides there is a `template_work` folder. Command lines are relative to this folder: 

* schema path is relative to `template-work\schemas` path
* template path ise relative to `template_work\templates` path
* output paths is relative to the `template_work\output` path

The directory listing below shows one the `librettox.py` file but there are also a few other files there (args_process.py, utils.py. a __pycache__ folder and probably a few others)

```
+---librettox
    librettox.py
    +---template_work
    |   +---libretto_batch_files
    |   +---libretto_sets
    |   |   \---sugarfoot
    |   +---output
    |   |   +---classes
    |   |   +---dapper
    |   |   +---dg_examples
    |   |   +---examples
    |   |   \---sugarfoot
    |   +---schemas
    |   |   +---argybargy
    |   |   +---dg_examples
    |   |   \---sql-server
    |   |       \---sugarfoot_db
    |   \---templates
    |       +---datagate
    |       \---dapper
```

### Libretto sets and batch files

The [LibrettoXUI](https://github.com/rogerpence/librettoUIX) WPF LibrettoX command line front-end can save a given Libretto session as a Libretto Set. A Libretto Set can later be opened to re-estalish that Libretto session. Libretto Set files are in the `libretto_sets` folder.

When a Libretto Set is saved, a corresponding batch file is also saved in the `libretto_batch_files` folder. This lets you re-run the Libretto Set from the command line.



Packages needed

- jinja2
- pyyaml
- colorama
- termcolor

