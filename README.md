# quicksnap

## Set-up Instructions
1. Download VS Code https://code.visualstudio.com/download.
2. Download Python https://www.python.org/downloads/.
3. Download Qt https://www.qt.io/download-qt-installer.
4. Download Visual Studio Community > Desktop development with C++ https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16.
5. In terminal, download the following package/s using pip:

    ```
    > pip install virtualenv
    ```

6. Create a virtual environment to isolate QuickSnap's Python configuration from your computer's Python config:

    **PowerShell Terminal**
    ```
    > Set-ExecutionPolicy Unrestricted -Scope CurrentUser
    > py -m virtualenv venv
    > .\\venv\Scripts\activate
    ```

    __Your terminal should now start with (venv).__

7. Install the packages listed in requirements into your virtual environment:

    ```
    > pip install -r requirements.txt
    ```
