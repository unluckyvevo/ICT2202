import subprocess


script_path = "C:\\Users\\User\\FOLDERS\\SIT\\yr2\\projects\\2202proj\\usbscript.ps1"
# INITIALIZING COMMAND
commandline_options = ["Powershell.exe", '-ExecutionPolicy', 'Unrestricted', script_path]

# RUN THE SCRIPT USING SUBPROCESS WITH PARAMS
result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)
# PRINT THE RETURN CODE FROM POWERSHELL SCRIPT
print(result.returncode)
# PRINT THE STANDARD OUTPUT FROM POWERSHELL SCRIPT
print(result.stdout)
# PRINT THE STANDARD ERROR FROM POWERSHELL SCRIPT
print(result.stderr)

