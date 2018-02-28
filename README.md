# ScaleFBX
---

This tool is designed to scale any ascii .fbx file by a specified ammount. 

## Dependencies

- Python 3.x

## Usage

Download the ScaleFBX.py

Open your terminal or command prompt and run:

`python /path/to/ScaleFBX.py /path/to/FBX.fbx /path/for/scaled.fbx --scale 2.54`

The first argument is the path to your existing .fbx file  
The second argument is the path to the new scaled fbx file that the script will create  
The --scale argument is how much you want to scale the .fbx by. `2` would double the size. `0.5` would make it half the size  

---

This tool only works on ascii FBX files. If you have a binary .fbx file you can convert it to ascii by using the Autodesk FBX converter tool found here: http://usa.autodesk.com/adsk/servlet/pc/item?siteID=123112&id=22694909
