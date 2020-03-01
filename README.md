# gmail export

## Video

https://www.loom.com/share/ee0baba59065404897d75bcb6d27b76d

## Installation

1. Make sure Python 3.8 or higher and git are installed.

    Windows:

    https://www.python.org/downloads/windows/

    If the installer asks to add Python to the path, check yes.

    https://git-scm.com/download/win

    MacOS:

    Open Terminal. Paste the following commands and press enter.

    ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile
    brew install python
    ```

    Linux:

    Open a terminal window. Paste the following commands and press enter.

    ```
    sudo apt install -y python3
    sudo apt install -y python3-pip
    sudo apt install -y git
    ```

3. Open a terminal/command prompt window. Run the following command.

    ```
    git clone https://github.com/andivis/gmail-export.git
    ```

4. On Windows you can simply go to the `gmail-export` folder and double click `run-windows.bat`. Otherwise do the following step.

5. Run the following commands in the same terminal/command prompt window you just opened. Depending on your system you may need run `pip` instead of `pip3`.

    ```
    cd gmail-export
    pip3 install -r requirements.txt
    ```

## Instructions

1. On Windows you can simply double click `run-windows.bat`. Otherwise do the following step.

2. Run `python3 main.py`. Depending on your system you may need run `python main.py` instead.

## Options

`user-data/options.ini` accepts the following options:

- `emailsToExport`: The email addresses to export, separated by commas. Default: (blank).