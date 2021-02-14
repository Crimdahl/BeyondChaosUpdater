from configparser import ConfigParser
from pathlib import Path
import os
import requests
config = ConfigParser()

#plans:
#the updater only will set the version...


def writeConfig(coreVersion, spriteVersion):
    config.read(Path(os.getcwd()+"/config.ini"))
    config.add_section('Version')
    config.set('Version', 'Core', coreVersion)
    config.set('Version', 'Sprite', spriteVersion)
    #config.set('main', 'key3', 'value3')

    with open(Path(os.getcwd()+"/config.ini"), 'w') as f:
        config.write(f)

#def readConfig():
#    config.read(os.getcwd()+'config.ini')
#    CoreVersion = config.get('Version', 'Core') # -> "value1"
#    SpriteVersion= config.get('Version', 'Sprite') # -> "value2"
#    #print config.get('main', 'key3') # -> "value3"


def checkINI():
    my_file = Path(os.getcwd()+"/config.ini")
    if my_file.is_file():
        # file exists
        return True
    else:
        return False

def initConfig():
    CoreVersion = getCoreVersion()
    SpriteVersion = getSpriteVersion()
    writeConfig(CoreVersion, SpriteVersion)

def getSpriteVersion():
    x = requests.get('https://api.github.com/repos/FF6BeyondChaos/BeyondChaosSprites/releases/latest').json()   
    version = x['tag_name']
    return version

def getCoreVersion():
    x = requests.get('https://api.github.com/repos/FF6BeyondChaos/BeyondChaosRandomizer/releases/latest').json()   
    version = x['tag_name']
    return version