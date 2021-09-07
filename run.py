import sys
import uvicorn

PYTHON_VERSION = (3,9)
def checkPythonVersion():
    if not sys.version_info.major == PYTHON_VERSION[0] or not sys.version_info.minor == PYTHON_VERSION[1]:
        raise Exception('Wrong Python version in enviroment')
    else:
        print(f'Current Python version: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}')

if __name__=="__main__":
    checkPythonVersion()
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)