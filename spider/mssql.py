import pymssql


class op_mssql(object):
    '''
    query_type=
    SQL:正常查询语句
    Procedure:存储过程
    '''

    def __init__(self, query_sql, query_type='SQL', query_args=None):

        self.conn_args = {
            'host': '',
            'port': '1433',
            'user': 'sa',
            'password': '',
            'database': 'test'
        }
        self.sql = query_sql
        self.sql_args = query_args
        self.query_type = query_type

    def get_rs(self):
        with pymssql.connect(**self.conn_args) as conn:
            with conn.cursor() as cur:
                if self.query_type == 'SQL':
                    cur.execute(self.sql, self.sql_args)
                elif self.query_type == 'Procedure':
                    cur.callproc(self.sql, self.sql_args)
                    cur.nextset()
                else:
                    print('wrong type!')
                    exit()

                rs = cur.fetchall()
                if rs:
                    return rs
                else:
                    return 'no data'


sql = 'Sp_test1'
args = ('d', '')
tmp_sql = op_mssql(sql, query_type='Procedure', query_args=args)
rs = tmp_sql.get_rs()
print(rs)
