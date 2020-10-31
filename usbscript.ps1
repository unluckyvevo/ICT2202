Get-Disk | Where-Object -FilterScript {$_.Bustype -Eq "USB"}

wmic diskdrive get Name,Model,SerialNumber,Size,Status 
Get-Partition -DiskNumber 1

$DiskNo = wmic diskdrive get Name


#-----------------------------------------------------------------------
#Look at only local drives
Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType = '2'"

Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType = '2'" | 
Select-Object -Property DeviceID, DriveType, VolumeName, 
@{l='FreeSpace(GB)';e={$_.FreeSpace / 1GB -as [int]}},
@{l='Capacity(GB)';e={$_.Size / 1GB -as [int]}},
@{l='UsedSpace(GB)';e={($_.Size - $_.FreeSpace) / 1GB -as [int]}},
@{l='%Free';e={$_.FreeSpace / $_.Size * 100 -as [int]}}


$Disk = Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType = '2'"
$Disk.GetRelated()


# Verify the existence of a Logs directory. If it doesn not exist, create it.
If (-not(Test-Path -Path E:\Logs))
    {
        New-Item -Path E: -Name Logs -ItemType directory
    }

# Date and Time
$today = Get-Date
$filename = $today.ToString("yyyy-MM-dd")
# $logFile = "C:\Users\User\Desktop\Logs\EfsDecryptLog_$filename.log"
$logFile = "E:Logs\EfsDecryptLog_$filename.log"

# Get al logical drives en put the output in a variabele named $drive
$drive = Get-WmiObject Win32_logicaldisk | Select-Object -ExpandProperty deviceID
Add-Content $logFile "$today Found the following drives: $drive"

# Let the user know the current status of the script
Write-Host "scanning all logical drives for encrypted files, please be patient..."

# Create a variable named $encryptedfiles that contains all items on all logical drives with a 'encrypted' attribute set

$encryptedfiles += foreach ($d in $drive) {

                    Get-ChildItem $d -Recurse -Force -ErrorAction SilentlyContinue |
                    Where-Object { !$_.PSIsContainer } |
                    Where-Object { $_.Attributes -match "Encrypted" } |
                    Select-Object -ExpandProperty FullName
                    }


# We will write to the logfile now log the amount of encrypted files and all the encrypted files with full pathname
Write-Host "Found $($encryptedfiles.count) encrypted files:"
Add-Content $logFile "$today Found $($encryptedfiles.count) encrypted files:"
Add-Content $logFile ""

gci E:\ * -r -fo -ea silentlycontinue | ? {$_.attributes -ge "encrypted"} | select fullname

foreach ($file in $encryptedfiles){
    Add-Content $logFile "$file"
    }

# Next we'll add some extra lines for easy reading the logfile
Add-Content $logFile "==============================================="
Add-Content $logFile "$today total $($encryptedfiles.count) encrypted files"
Add-Content $logfile ""

