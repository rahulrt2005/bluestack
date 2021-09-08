import requests
import subprocess
import time
import os
from pathlib import Path


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f"Time Taken to execute {method.__name__} method ::: {(te - ts)} seconds")
        return result
    return timed


def download_bs5():
    """
    This method will download bs5 installer and return the directory path and downloaded file name
    :return: dictionary with file name and path of downloaded file
    """
    bs5_download_url = "https://cdn3.bluestacks.com/downloads/windows/nxt/5.2.110.1003" \
                       "/4b37f8a27d79ab796aef0455dcca9eb4/x64/BlueStacksFullInstaller_5.2.110.1003_amd64_native.exe"

    file_name = "bs5_offline_installer.exe"
    file_path = Path(os.getcwd())/file_name
    r = requests.get(bs5_download_url, stream=True)
    print("Downloading Bluestacks 5 offline installer !!!!! ")
    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Downloading Bluestacks 5 offline installer finished !!!!! ")
    return {"file_name": file_name, 'path': file_path}


@timeit
def install_bs5(file_path):
    """

    :param file_path: Path of file to be installed
    :return: Install Directory
    """
    cmd = f"{file_path} -s"
    try:
        subprocess.check_output(cmd)
        print(f"BlueStacks 5 installation complete")
    except:
        print(f"Error occurred while installing")
    finally:
        Path.unlink(file_path)
