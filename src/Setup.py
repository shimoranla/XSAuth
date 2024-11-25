import json
import pathlib
import platform
import os


SystemName = platform.system()

if SystemName.startswith("win"):
    DataSpace = pathlib.Path(os.environ["systemdrive"]).parent.joinpath(":/ProgramData")



def set(dataspace,name,value):
    with open(pathlib.Path().parent.joinpath()) as f: