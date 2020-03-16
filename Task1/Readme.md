### Installation  

Install Python3 if it's not yet there.  
To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3.7  
  
For more details or other OSs please follow the documentation:  
https://docs.python.org/3/using/unix.html  
https://docs.python.org/3/using/windows.html  
  
### Running application locally

From the current directory, run:  
python3 Task1.py  

### Running application on image

From the current directory, run:  
docker build --tag=history_statistics .  
docker run history_statistics:latest  
