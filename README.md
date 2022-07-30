# My Project
Description

## Python Environment
### Linux
#### To create the python envirnoment:
```bash
$ source ./scripts/create_python_venv_linux.sh
```

#### To activate the python environment
```bash
$ source .linux_env/bin/activate
```
or
```bash
$ source scripts/activate_linux_venv.sh
```

#### To deactivate the python environment
```bash
$ deactivate
```

#### Run the program
After the python env activation
```bash
$ python main.py
```

### Windows Powershell
#### To create the python envirnoment:
```shell
$ .\scripts\create_python_venv_win.sh
```

#### To activate the python environment
```shell
$ .\scripta\activate_win_venv.ps1
```

#### To deactivate the python environment
```shell
$ deactivate
```

#### Run the program
After the python env activation
```shell
$ python main.py
```

#### Create a Windows executable
# TODO check on this
```shell
$ .\scriptas\create_exe.ps1
```

## Software Requirements
 - python 
 - pip python module
 - venv python module


# How to use `MyProject`

## TODO

## Start the application with a different language in linux
 ```bash
 $ LANG=it_IT.UTF-8 python main.py
 $ LANG=en_US.UTF-8 python main.py 
 ```

## Create .po translation file
 ```bash 
 $ xgettext main.py 
 ```
 This will create a `message.po` file in the root directory (if there are any message to translate).

 Rename this file in `main.po` and copy it in the language directory `files/locale/<LANG>/LC_MESSAGES`

## Create .mo translation file from .po
 ```bash
 $ msgfmt files/locale/<LANG>/LC_MESSAGES/main.po -o files/locale/<LANG>/LC_MESSAGES/main.mo
 ```

 Example:
 ```bash
 $ msgfmt files/locale/it_IT/LC_MESSAGES/main.po -o files/locale/it_IT/LC_MESSAGES/main.mo
 ```
