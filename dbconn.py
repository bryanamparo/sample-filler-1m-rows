import psycopg2


class DBConnection():

    def __init__(self, host, port, username, password, database):
        self.__connection = psycopg2.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database
        )
        # cursor = self.__connection.cursor()
        # cursor.execute('SET NAMES utf8mb4')
        # cursor.execute("SET CHARACTER SET utf8mb4")
        # cursor.execute("SET character_set_connection=utf8mb4")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(exc_type, exc_value, traceback)
            self.__connection.rollback()
        else:
            self.__connection.commit()
        self.__connection.close()

    def fetch_single(self, query, params=None):
        cur = self._execute_query(query, params)
        row = cur.fetchone()
        return row

    def fetch_multiple(self, query, params=None):
        cur = self._execute_query(query, params)
        rows = [dict((cur.description[i][0], value)
                     for i, value in enumerate(row))
                for row in cur.fetchall()]
        return rows

    def _execute_query(self, query, params=None):
        cur = self.__connection.cursor()
        if (params is None):
            cur.execute(query)
        else:
            cur.execute(query, params)
        return cur

    def update_object(self, query, params):
        cur = self.__connection.cursor()
        cur.execute(query, params)
