# Unreserved Railway Ticket System (UTS)

# How to Run This Project :

  1. Make sure you have installed the latest version of Python and MySQL
  2. You can use any IDE (eg : Spyder, Pycharm, IDLE)
  3. Download all the files from this repository
  4. Make sure that all the files are in the same folder
  5. You will have to change the username, password, etc wherever SQL database connection is mentioned in the Master file
  6. Launch MySQL, make sure your connection has been established
  7. Run the Master file and make sure everything works as desired
  
# How to Convert Python Script to Application (For MAC) :
  
   NOTE : USE THE UPLOADED SETUP FILE ONLY FOR REFRENCE, REMOVE THE FILE BEFORE BEGINING THE CONVERSION

    1. Open your Terminal 
    2. Make sure you have installed the latest version of py2app library on your system (pip3 install -U py2app)
    3. Make sure you're in the dicrectory where you have stored all your supporting files
    4. Next run this command (py2applet --make-setup MyApplication.py) (Enter the desired name of your setup file in place of (MyApplication))
    5. Your Setup file is created 
    6. Mention the required changes as per your wish (Use uploaded setup file for refrence)
    7. Next Command (python setup.py py2app -A)
    8. Your Python Script has been converted to Apllication
    9. Its advised to run the application from terminal for the first time using the following command (./dist/application_name.app/Contents/MacOS/application_name)
    10. You've succesfully converted your Python Script to Application
