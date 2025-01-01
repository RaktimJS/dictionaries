import os
from pathlib import Path

def pack(FileName = str, RemoveLocalPycache = False):
        dirName = Path(FileName).parent
        fileNameWithoutExtension = os.path.splitext(os.path.basename(os.path.abspath(FileName)))[0]

        if os.path.isfile(fileNameWithoutExtension + '.exe') == False:
                os.system(f'pyinstaller --onefile --distpath "." {fileNameWithoutExtension}.py')

        if os.path.exists(dirName):
                os.system(f'rmdir /s /q "{dirName}\\build"')

        if RemoveLocalPycache == True:
                if os.path.exists(dirName):
                        os.system(f'rmdir /s /q "{dirName}"\\__pycache__')

        if os.path.isfile(fileNameWithoutExtension + '.spec'):
                os.remove(fileNameWithoutExtension + '.spec')
