import pymssql
import os
import json


class mssql(object):
    '''
    此类可对sqlserver进行语句执行、存储过程执行等操作，根据需要返回记录集。

    需根据服务器名找到保存该服务器的配置文件，该文件以json格式保存：\n
    {
        "host": "",
        "port": "",
        "user": "",
        "password": "",
        "database": ""
    }\n
    其中host和database信息需初始化该类的时候传入，其余信息保存在配置文件内。
    '''

    def __init__(self,
                 host,
                 database,
                 query_sql,
                 query_type='SQL',
                 query_args=None):
        '''Constructor
        :param host:服务器名
        :param database:数据库名
        :param query_sql:sql语句或存储过程名称
        :param query_type:查询类型，默认'SQL'为sql语句查询，'Procedure'为存储过程查询
        :param query_args:tuple，查询参数，用于sql语句的%格式化，或为存储过程添加参数
        '''
        self.host = host
        self.database = database
        self.query_sql = query_sql
        self.query_args = query_args
        self.query_type = query_type
        self.conn_args = self.read_conn_args()

    def read_conn_args(self):
        '''从json文件读取配置参数'''
        with open(self.json_filepath()) as file:
            conn_args = json.load(file)
            conn_args['database'] = self.database
            return conn_args

    def json_filepath(self):
        '''根据host获取服务器相应配置文件的路径'''
        return os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'secret',
            self.host + '.json')

    def get_rs(self):
        '''执行语句或存储过程，返回记录集'''
        with pymssql.connect(**self.conn_args) as conn:
            with conn.cursor() as cur:
                if self.query_type == 'SQL':
                    cur.execute(self.query_sql, self.query_args)
                elif self.query_type == 'Procedure':
                    cur.callproc(self.query_sql, self.query_args)
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
host = 'dnb.hxserver.cn'
database = 'test'
tmp_sql = mssql(host, database, sql, query_type='Procedure', query_args=args)
rs = tmp_sql.get_rs()
print(rs)
