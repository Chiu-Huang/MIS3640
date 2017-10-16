import cx_Freeze

executables = [cx_Freeze.Executable("test.py")]

cx_freeze.setup(
    name = "DND first trial",
    options = {"build_exe": {"packages":["pygame"],"include_files":["racecar.png"]}},
    executables = executables
)