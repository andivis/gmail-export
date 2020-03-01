# gmail export

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

2. Open a terminal/command prompt window. Depending on your system you may need run `pip` instead of `pip3`.

```
git clone (repository url)
cd (repository name)
pip3 install -r requirements.txt
```

## Instructions

1. Run `python3 main.py`. Depending on your system you may need run `python main.py` instead.

## Options

`user-data/options.ini` accepts the following options:

- `emailsToExport`: What email addresses to export. Default: (blank)