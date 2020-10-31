import subprocess

# params = ['param1', 'param2']  # POWERSHELL SCRIPT PARAMETERS ( optional )
script_path = "C:\\Users\\User\\FOLDERS\\SIT\\yr2\\projects\\2202proj\\usbscript.ps1"  # POWERSHELL SCRIPT PATH
commandline_options = ["Powershell.exe", '-ExecutionPolicy', 'Unrestricted', script_path]  # INITIALIZING COMMAND
# for param in params:  # FOREACH LOOP OF PARAMETERS
#   commandline_options.append(param)  # ADDING SCRIPT PARAMETERS TO THE COMMAND

result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)  # RUN THE SCRIPT USING SUBPROCESS WITH PARAMS

print(result.returncode)  # PRINT THE RETURN CODE FROM POWERSHELL SCRIPT
print(result.stdout)  # PRINT THE STANDARD OUTPUT FROM POWERSHELL SCRIPT
print(result.stderr)  # PRINT THE STANDARD ERROR FROM POWERSHELL SCRIPT

