GitHub: https://github.com/oluwadara03/Health-Fitness-Club-Management-System
Explanation Video: https://youtu.be/Wv84ngvxiMo

Step 1: Download the source code from GitHub, and save it somewhere you can access.

Step 2: Open pgAdmin 4 and create a PostgreSQL database with the name "Health and Fitness Club".

Step 3: Using the given DDL file, run the DDL script in the "Health and Fitness Club" database using the query tool. This will create the necessary tables and schema for the application.

Step 4: If you want to test the DML file with this, run the DML script in the "Health and Fitness Club" database using the query tool. This will populate data for the application. 

NOTE: For any installations below, the terminal may return a prompt to install the latest version. Updating to the latest version is not necessary, because the non-upgraded version works for everything below.  

Step 5: Open a terminal and install pyscopg2 using the following command in your terminal: "pip install psycopg2". Psycopg is the most popular PostgreSQL database adapter for the Python programming language, and it allows you to preform queries in PostgreSQL (more specifically in pgAdmin4).

Step 6: Please install prettytable - to do so, enter "python -m pip install -U prettytable".

Step 7: Install datetime and argparse - enter "pip install datetime" and "pip install argparse".

NOTE: There is no need to install logging. The "import logging" in the code does the job.

Step 8: In the dataAccess.py file, update the dbName, dbUser, and dbPassword variables with the appropriate values for your PostgreSQL database. The dbHost of "localhost" can remain the same. Also, unless you renamed the PostgreSQL database with another name other than "Health and Fitness Club", then you do not have to change the value for dbName.

Step 9: Navigate to the directory you saved the source code, and run the application using the command: "python appLogic.py [command-line argument]". As for the command-line arguments, type "python appLogic.py --help" or "python appLogic.py --h" to view the entire list.

Step 10: Play around with the application, use the command line arguments to view/update/change data as you please.
