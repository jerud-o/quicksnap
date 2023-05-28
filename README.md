# QuickSnap: Dev Guide

## Set-up Instructions
### Download the following:
1. VS Code https://code.visualstudio.com/download.
2. Python **latest 3.10 version** https://www.python.org/downloads/.
3. Qt https://www.qt.io/download-qt-installer.
4. Visual Studio Community > Desktop development with C++ https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16.
5. MS Office, including Word.
6. In VS Code Terminal, download the following package/s using pip:

    ```
    pip install virtualenv
    ```

### Set up Virtual Environment
1. Open requirements.txt file.
2. Click "Create Environment" button at bottom-right
3. Select "Venv", "Python 3.10 Interpreter"
4. Wait until a .venv folder is created.

__Your terminal should now start with (.venv).__

## Environment Variables
Rename .env.example file into .env

    _(Note: After the renaming, **the .env file should be grayed out**)_

## Build QuickSnap
To build the application, run:

    ```
    pyinstaller QuickSnap.spec
    ```

    __It will create a folder named dist that houses the executable file.__