@echo off
call :filedialog file1
call :filedialog file2
echo First File Selected is : %file1%
echo File Details:
@echo off
FOR %%? IN ("%file1%") DO (
    ECHO File Name Only       : %%~n?
    ECHO File Extension       : %%~x?
    ECHO File Attributes      : %%~a?
    ECHO Located on Drive     : %%~d?
    ECHO File Size            : %%~z?
    ECHO Last-Modified Date   : %%~t?
set t1=%%~t?
    ECHO Drive and Path       : %%~dp?
    ECHO Drive                : %%~d?

)
echo(
echo Second file selected is : %file2%
FOR %%? IN ("%file2%") DO (
    ECHO File Name Only       : %%~n?
    ECHO File Extension       : %%~x?
    ECHO File Attributes      : %%~a?
    ECHO Located on Drive     : %%~d?
    ECHO File Size            : %%~z?
    ECHO Last-Modified Date   : %%~t?
set t2=%%~t?
    ECHO Drive and Path       : %%~dp?
    ECHO Drive                : %%~d?
)


echo(
echo File Timestamp Comparison:
FOR %%a IN ("%File1%") DO SET DATE1=%t1%
echo First File: %DATE1%
FOR %%a IN ("%File2%") DO SET DATE2=%t2%
echo Second File: %DATE2%
exit /b

 
:filedialog :: &file
setlocal
set dialog="about:<input type=file id=FILE><script>FILE.click();new ActiveXObject
set dialog=%dialog%('Scripting.FileSystemObject').GetStandardStream(1).WriteLine(FILE.value);
set dialog=%dialog%close();resizeTo(0,0);</script>"
for /f "tokens=* delims=" %%p in ('mshta.exe %dialog%') do set "file=%%p"
endlocal  & set %1=%file%
