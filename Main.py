from API import Server
import os 


if __name__ == '__main__':
     os.chdir(os.getcwd()+"/UI")
     os.system("npm start") 
     Server.start_server()