#get
#set
#expiry
import time
class Redis:
    __redis_dict = dict()
    def get(self, key):
        if self.__redis_dict.get(key):
            if self.__redis_dict[key][1] and self.redis_dict[key][1] > time.time():
                return self.__redis_dict[key][0]
            else:
                del self.__redis_dict[key]
            return None
    def set(self, key, value):
        if type(value) != str:
            return None
        if self.__redis_dict.get(key):
            self.__redis_dict[key][0] = value
        else:
            self.__redis_dict[key] = [value, "None"]
        return "OK"
        
    def expire(self, key, exp):
        if not self.__redis_dict.get(key):
            return 0
        self.__redis_dict[key][1] = time.time()+exp
        return 1
        
redis = Redis()
print("Setting value unacademy to key key1:")
print(redis.set("key1", "unacademy"))
print("setting expiry time 10 seconds")
print(redis.expire("key1", 10))
time.sleep(12)
print("After 12 seconds we find that there is no key1")
print(redis.get("key"))
################################RedisSET###################################################
#zadd
#zrank
class RedisSet:
    __redis_set = dict()
    def zadd(self, key, rank, value):
        if not self.__redis_set.get(key):
            a=set()
            a.add(value)
            self.__redis_set[key]=dict()
            self.__redis_set[key][rank]=a
        else:
            if not self.__redis_set[key].get(rank):
                a=set()
                a.add(value)
                self.__redis_set[key][rank]=a
            else:
                self.__redis_set[key][rank].add(value)
    
    def zrank(self, key, value):
        if self.__redis_set.get(key):
            c=0
            for k in self.__redis_set[key]:
                for v in self.__redis_set[key][k]:
                    print(v)
                    if v==value:
                        return c
                    else:
                        c+=1
        return None
redisSet=RedisSet()
print("setting values in myset:")
redisSet.zadd("myset", 2, "zaman")
redisSet.zadd("myset", 1, "bbb")
redisSet.zadd("myset", 1, "aaa")
print("fetching rank of aaa in myset")
print(redisSet.zrank("myset", "aaa"))