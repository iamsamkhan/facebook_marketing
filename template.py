import os , sys
from pathlib import Path
import logging 


while True:
    project_name=input("enter the project name : ")
    if project_name !="":
        break

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/video/__init__.py",
    f"{project_name}/check/__init__.py",
    f"{project_name}/addbootstrap/__init__.py",
    f"{project_name}/trackrecods/__init__.py",
    f"{project_name}/contantshare/__init__.py"
    f"config/config.yaml",
    "schema.ymal",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py" 

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
    #if os.path.exists(filepth)==True:
        with open(filepath,"w") as f:
            pass
           # f.write()
    else:
        logging.info("file already exist : {filepath}")
