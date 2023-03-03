import os

BuildType = input("C/S:")

if (BuildType == "C"):
    os.system("mkdir ClientBuild")
    os.system("cp Client/Main.py ClientBuild")
    os.system("cp Client/Etc.py ClientBuild")
    os.system("cp Client/Encrypt.py ClientBuild")
    os.system("cp Client/User.py ClientBuild")
    os.system("cp Client/Update.py ClientBuild")
    os.system("cp -r Client/AppData ClientBuild")

    os.system("pyminify ClientBuild/ --in-place")
    os.system("pyinstaller --onefile ClientBuild/Main.py")
    os.system("cp dist/Main ClientBuild")
    os.system("rm -r dist")
    os.system("rm -r build")
    os.system("rm Main.spec")
    os.system("rm ClientBuild/*.py")
