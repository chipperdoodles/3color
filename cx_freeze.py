from cx_Freeze import setup, Executable
import platform

base=None

if platform.system() == "win32":
    base = "Win32GUI"

build_exe_options = {"packages": ["threecolor"]}

# executables=[Executable("threecolor/gui.py", base=base)]

executables = [Executable(
        script="threecolor/gui.py",
        targetName="3color",
        compress=True,
        appendScriptToLibrary=True,
        appendScriptToExe=True,
        base=base
        )]

setup(name="threecolor",
      version="0.2.3",
      description="derp",
      options={"build_exe": build_exe_options},
      executables=executables)
