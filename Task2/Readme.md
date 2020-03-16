### Installation  

Install Python3 if it's not yet there.  
To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3.7  
  
For more details or other OSs please follow the documentation:  
https://docs.python.org/3/using/unix.html  
https://docs.python.org/3/using/windows.html  
  
Install PIP if it's not yet there. To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3-pip  

For more details please follow the documentation:  
https://pip.pypa.io/en/stable/installing/  

Install MySQL. To do this on Ubuntu, run:  
sudo apt-get install mysql-server  
For more information, please follow:
https://support.rackspace.com/how-to/install-mysql-server-on-the-ubuntu-operating-system/  
or  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/linux-installation.html  

For the details for others OS please follow:  
https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation.html  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/windows-installation.html  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/solaris-installation.html  

Install flask, mysql-connector-python, pytest, requests if they are not yet there.  

To do this, either run:  

sudo pip3 install -r requirements.txt  

Or, on Ubuntu, run:  

sudo pip3 install flask  
sudo pip3 install mysql-connector-python  
sudo pip3 install pytest  
sudo pip3 install requests  
sudo pip3 install healthcheck  

Or:
sudo pip3 install -r requirements.txt

For more details please follow:  
https://pypi.org/project/Flask/  
https://pypi.org/project/mysql-connector-python/  
https://pypi.org/project/pytest/  
https://pypi.org/project/requests/  
https://github.com/Runscope/healthcheck  

### Endpoints

To run healthcheck use the following endpoint:  
# /healthcheck
method: 'GET'  
input parameter: None  
output parameter: str  
Example:  
http://127.0.0.1:5000/healthcheck  

# /fib/<number>
method: 'GET'
input parameter: number for which arrays of Fibonacci to be counted
output parameter: array of int
Example:  
http://127.0.0.1:5000/fib/18  

### Running tests

Go to tests folder, run:  
pytest endpoint_fib_tests.py  
or  
pytest -v endpoint_fib_tests.py  

### Running application locally

Go to lib/credentials.py and update the username and password of MySQL admin user, as well as username and password of the application user. If you update application username or database name, update also the appropriate queries in db/fibonacchi_db_v1.0.0.sql.  
From the current directory, run:  
python3 api.py  
Click on the link from the console and modify the URL by adding fib/ and number, for example:
http://127.0.0.1:5000/fib/11
There will be status code in the console and array of Fibonacci sequences in the content area of web page.
