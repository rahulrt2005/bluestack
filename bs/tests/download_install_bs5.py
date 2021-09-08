"""
Q1) Create a script to install BlueStacks 5 App player setup on Windows 10. You are free to create this script in any programming language of your choice (Python is preferred).
Minimum requirements in the application:
⦁	The script should download the setup from ⦁	bluestacks.com
⦁	Once the download is completed, it should launch the setup.exe
⦁	The script should complete all the installation steps without any input from the user (license agreement, choosing installation path, other configuration etc.)
⦁	Once the installation is completed, the script should display total time taken in the installation.
⦁	This script should work on all major screen resolutions (1920x1080, 1366x768 etc.) and DPI settings (125%, 150%) on Win 10 operating system.
⦁	You must handle all the edge case scenarios in your code.

<TODO> Check Space om disk before download
<TODO> Check if installer is already present
"""

from steps import steps_bs5

# Download offline installer
downloader_details = steps_bs5.download_bs5()
print(f"downloader_details ::: {downloader_details}")

# Installing BS 5
steps_bs5.install_bs5(downloader_details["path"])


