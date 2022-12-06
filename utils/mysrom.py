class MySQLConnect:
    def __init__(self, host, user, password, database):
        from mysql.connector import connect

        self.conn = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def query(self, sql):
        conn = self.conn.cursor()
        conn.execute(sql)
        self.conn.commit()

    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = list(data.keys())
        for x in range(len(values)):
            values[x] = '%s'
        values = ', '.join(values)

        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        val = tuple(list(data.values()))

        conn = self.conn.cursor()
        conn.execute(sql, val)
        self.conn.commit()