from cx_Freeze import setup, Executable
import platform

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["threecolor"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if platform.system() == "win32":
    base = "Win32GUI"
elif platform.system() == "Windows":
    base = "Console"
else:
    base = None

WinCon = Executable(
        script="threecolor/manager.py",
        targetName="3color",
        compress=True,
        appendScriptToLibrary=False,
        appendScriptToExe=True,
        base=base)

setup(name="threecolor",
      version="0.1",
      description="derp",
      options={"build_exe": build_exe_options},
      executables=[Executable("threecolor/cli.py", base=base)])
