# bluestack
Prerequisites:
- Python 3.X installed
- requests, os, pathlib, pytest modules installed

Steps for running the download and install time test
1. Clone the repository:
git clone https://github.com/rahulrt2005/bluestack.git
2. Navigate to cloned repo
3. run the below command: 
  set PYTHONPATH=[Repo Path]\bluestack\bs
4. Run test case using below command: 
  pytest -m bs5 -s test_download_install_time_bs5.py
