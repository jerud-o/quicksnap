# quicksnap

## Set-up Instructions
1. Download VS Code https://code.visualstudio.com/download.
2. Download Python **latest 3.10 version** https://www.python.org/downloads/.
3. Download Qt https://www.qt.io/download-qt-installer.
4. Download Visual Studio Community > Desktop development with C++ https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16.
5. Download MS Office, including Word.
6. In terminal, download the following package/s using pip:

    ```
    pip install virtualenv
    ```

7. Create a virtual environment to isolate QuickSnap's Python configuration from your computer's Python config:

    **PowerShell Terminal in VS Code**
    ```
    Set-ExecutionPolicy Unrestricted -Scope CurrentUser ; py -m virtualenv venv ; .\\venv\Scripts\activate
    ```

    __Your terminal should now start with (venv).__

8. Install cmake package into your virtual environment:

    ```
    pip install cmake
    ```

9. Install the packages listed in requirements into your virtual environment:

    ```
    pip install -r requirements.txt
    ```

10. Rename .env.example file into .env

    _(Note: After the renaming, **the .env file should be grayed out**)_

11. To build the application, run:

    ```
    pyinstaller --onefile --icon=package/resource/img/quicksnap.ico --name="QuickSnap" main.py
    ```

    __It will create a folder named dist that houses the executable file.__