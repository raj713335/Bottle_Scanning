# Bottle Scanning
A crossplatform desktop application to read and scan data and validate the data according to the given requirements before saving it to an xml file.

# Bottle Scanning


![](favicon.ico)





## Getting Started
- Clone the repo and cd into the directory
```sh
$ git clone https://github.com/raj713335/Bottle_Scanning.git
$ cd Bottle_Scanning
```

- Install EasyTkinter, tkcalendar, opencv-python and Pillow and pyinstaller

```sh
$ pip install EasyTkinter tkcalendar opencv-python Pillow pyinstaller
```

- Run the app

```sh
$ python master.py
```

## Packaging the app
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.

```sh
$ pyinstaller -i "favicon.ico" --onefile -w --hiddenimport=EasyTkinter --hiddenimport=tkcalendar --hiddenimport=opencv-python --hiddenimport=Pillow  --name Bottle_Scanning master.py
```

Or
```sh
$ python -m EasyTkinter tkcalendar opencv-python Pillow master.py web --noconsole --onefile --icon='favicon.ico'
```

## Packaging the app after running pyinstaller
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.

```sh
Once above writtem pyinstaller command is executed in terminal it creates 3 files i.e dist, build 
and Bottle_Scanning.spec . Then you need to copy the DATA folder inside the dist Folder and 
execute the Bottle_Scanning Application .
```

