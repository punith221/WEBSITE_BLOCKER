import blocker_window
import mysql.connector
import config
import db_operations

class Blocker:
    def __init__(self, urls):
        self.urls = urls
        try:
            # self.dataBase = mysql.connector.connect(
            #     host=config.hostName,
            #     user=config.user,
            #     passwd=config.password,
            #     database=config.database
            # )
            # self.cursorObject = self.dataBase.cursor()
            self.connection = db_operations.get_db_connection()

        except mysql.connector.Error as e:
            print("Failed Establish Connection to database")
            print(e)

    def block(self, datetime):
        website_lists = list(self.urls.split(","))
        with open(config.host_path, 'r+') as host_file:
            file_content = host_file.readlines()
            for website in website_lists:
                if website in file_content:
                    blocker_window.BlockerWindow.display_label("Already Blocked.. !!")
                    pass
                else:
                    host_file.write(config.ip_address + " " + website + '\n')

                    query = "INSERT INTO SITES_INFO(website_Name, time_date, status) VALUES (%s, %s, %s)"
                    val = (website, datetime, "active")
                    cursor = self.connection.cursor()
                    db_operations.db_write(cursor,query,val)
                    db_operations.close_db_connection(cursor,self.connection)
                    print(website+" Blocked")

    def unblock(self):
        # currently unblocks all the websites
        website_lists = list(self.urls.split(","))
        with open(config.host_path, "r+") as host_file:
            file_content = host_file.readlines()
            host_file.seek(0)
            for website in file_content:
                if not any(site in website for site in website_lists):
                    host_file.write(website)
                host_file.truncate()
                print("All sites Unblocked")
                break
