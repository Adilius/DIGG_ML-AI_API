import sys

if not sys.version_info.major == 3 or not sys.version_info.minor == 9:
    raise Exception('Wrong Python version in enviroment')
else:
    print(f'Current Python version: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}')

import uvicorn

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    pass