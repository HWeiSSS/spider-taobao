from settings.library import *


def redis_redis():
    server = SSHTunnelForwarder(
        ssh_address_or_host="121.40.209.59",  # ssh地址
        ssh_username="spider",  # ssh连接的用户名
        ssh_password="spiuIms9w",  # ssh连接的用户名
        remote_bind_address=('127.0.0.1', 6379)
    )

    server.start()
    # try:
    pool = redis.ConnectionPool(host='127.0.0.1', port=server.local_bind_port, decode_responses=True, db=14)
    conn = redis.Redis(connection_pool=pool, decode_responses=True)
    # except Exception:
    #     print('redis链接失败')

    return server, conn


def localhosts_redis():
    return redis.Redis("192.168.120.14", 6379, db=2)


def mongo_mongo():
    server = SSHTunnelForwarder(
        ssh_address_or_host="121.40.209.59",  # ssh地址
        ssh_username="spider",  # ssh连接的用户名
        ssh_password="spiuIms9w",  # ssh连接的用户名
        remote_bind_address=('127.0.0.1', 27017)
    )
# 'sshtunnel.BaseSSHTunnelForwarderError: Could not establish session to SSH gateway'
    server.start()
    conn = pymongo.MongoClient(host='127.0.0.1', port=server.local_bind_port)
    return server, conn


def mysql_mysql():
    server = SSHTunnelForwarder(
        ssh_address_or_host="121.40.209.59",  # ssh地址
        ssh_username="spider",  # ssh连接的用户名
        ssh_password="spiuIms9w",  # ssh连接的用户名
        remote_bind_address=('127.0.0.1', 3306)
    )

    server.start()
    conn = pymysql.conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="weR9=%5wB2*P",
                database="spy", port=server.local_bind_port)
    return server, conn