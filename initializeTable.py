import dbFunctions
if __name__ == "__main__":
    connection=dbFunctions.create_server_connection("localhost", "rskuma", "password")


    #dbFunctions.init_database(connection)

    #dbFunctions.init_table(connection)
    dbFunctions.init_table2(connection)
