#! python3

# importing relevant libraries
import mysql.connector
from mysql.connector import errorcode


class connection():
    def __init__(self, connector=mysql.connector, errorcode=errorcode):
        # Creating a database connection configuration
        self.Error = connector.errors.Error
        self.config = {'user': 'root', 'password': 'Valadolis_Creme@2', 'host': '127.0.0.1',
                       'raise_on_warnings': True, 'use_pure': True, 'autocommit': True}
        try:
            self.connection = connector.connect(**self.config)
            self.cursor = self.connection.cursor()

        except self.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Wrong Username/password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("No such database")
            else:
                print("Error while connecting to MySQL", e)
        else:
            print(f"Connection established! @ {self.config['host']}\n")

    def create_database(self, db_Name):
        # This method creates the required database specified by the user.
        self.db_Name = db_Name
        # Creating a connection, testing connection, and catching exceptions
        try:
            create_command = f"CREATE DATABASE IF NOT EXISTS {self.db_Name} DEFAULT CHARACTER SET 'UTF8MB4'"
            self.cursor.execute(create_command)
        except self.Error as e:
            if (e.errno == 1007):
                print(f"Error: {str(e)[6:]}!")
                print(
                    f"\nDo you want to drop the {db_Name} database?\n.Answer with y or n\n")
                choice = input(">>> ").lower()
                flag = True
                while flag:
                    if (choice not in ["y", "n"]):
                        print("\nYou entered something wrong! Try again...\n")
                        print(
                            f"\nDo you want to drop the {self.db_Name} database?\n. Answer with Y or N")
                        choice = input(">>> ")
                    elif choice == "y":
                        try:
                            drop_command = f"DROP DATABASE {db_Name}"
                            self.cursor.execute(drop_command)
                        except self.Error as e:
                            print("\nDropped:" + str(e).split(";")
                                  [1] + " anymore!\n")
                            return
                    else:
                        print("\nExiting database operation\n")
                        flag = False
        else:
            print("Database created!\n")

        finally:
            if __name__ == '__main__':
                self.test_connection()

    def test_connection(self):
        # checking if connected
        if self.connection.is_connected():
            info = self.connection.get_server_info()
            print("Connected to MySQL Server version ", info)
            try:
                commands = [f"USE {self.db_Name};", "SELECT DATABASE();"]
                [self.cursor.execute(command) for command in commands]
                record = self.cursor.fetchone()
            except self.Error as e:
                print(f"\nPlease, re-create the database: {self.db_Name}")
                record = "None"

            finally:
                print("connected to database: ", record)


database = connection()
database.create_database("New_Database")
