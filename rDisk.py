# importing datetime module
import os
from datetime import *
import subprocess

subprocess.call([r'C:\Users\User\FOLDERS\SIT\yr2\2202\proj\GetFileInfo.bat'])

d1, m1, y1 = [int(x) for x in input("Enter date of first"
                                    " file(DD/MM/YYYY) : ").split('/')]

b1 = date(y1, m1, d1)

# Input for second date
d2, m2, y2 = [int(x) for x in input("Enter date of second"
                                    " file (DD/MM/YYYY) : ").split('/')]

b2 = date(y2, m2, d2)

# Compare the dates
if b1 == b2:
    print("Both files are of equal age")

elif b1 > b2:
    print("The second file is older")

else:
    print("The first file is older")
