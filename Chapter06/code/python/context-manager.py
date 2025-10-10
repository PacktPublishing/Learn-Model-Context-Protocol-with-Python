class DatabaseConnection:
    def __enter__(self):
        print
        self.conn = self.connect_to_database()
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")
        self.close_connection(self.conn)

    def connect_to_database(self):
        # Logic to connect to the database
        pass

    def close_connection(self, conn):
        # Logic to close the database connection
        pass

with DatabaseConnection() as db_conn:
    print("Using database connection:", db_conn)
    # Perform database operations
    # db_conn.execute("SELECT * FROM table")
    # db_conn.commit()
    # db_conn.rollback()