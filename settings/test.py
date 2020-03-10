from settings import database
from bson import ObjectId

server, rediss = database.redis_redis()
mongo_server, conn = database.mongo_mongo()
mongo_conn = conn.parse.con_shop_product_info

jd_data = mongo_conn.find({'status': {'$ne': '0'}, 'platform_id': '3'})
tm_data = mongo_conn.find({'status': {'$ne': '0'}, 'platform_id': '1'})


def mongo_data():
    for i in jd_data:
        # rediss.sadd("jd_item_id_set1", i['item_id'])         # 京东评论信息
        rediss.sadd("jd_item_id_set2", i['item_id'])         # 京东商品信息

    for i in tm_data:
        # rediss.sadd("tm_item_id_set1", i['item_id'])         # 天猫评论信息
        rediss.sadd("tm_item_id_set2", i['item_id'])         # 天猫商品信息
    print('完成')


def redis_data():
    for i in rediss.smembers("jd_item_id_set"):
        rediss.sadd("jd_item_id_set1", str(i, encoding="utf8"))         # 京东评论信息
        rediss.sadd("jd_item_id_set2", str(i, encoding="utf8"))         # 京东商品信息

    for i in rediss.smembers("tm_item_id_set"):
        rediss.sadd("tm_item_id_set1", i)         # 天猫评论信息
        rediss.sadd("tm_item_id_set2", i)         # 天猫商品信息
    print('完成')


if __name__ == '__main__':
    mongo_data()