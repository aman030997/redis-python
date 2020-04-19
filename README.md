# redis-python
Redis functionality using python
redis-py requires a running Redis server. 

redis-py can be installed using pip similar to other Python packages. Do not use sudo with pip. It is usually good to work in a virtualenv or venv to avoid conflicts with other package managers and Python projects. 

To install redis-py, simply:

$ pip install redis
or from source:

$ python setup.py install


Getting Started


--> import redis


--> r = redis.Redis(host='localhost', port=6379, db=0)


--> r.set('foo', 'bar')

True

--> r.get('foo')

b'bar'



This repository contain 2 files:

pyredis.py --> This file is built from scratch that has functionalities similar to redis get, set, expire, zadd and zrank.
	       This file is built using Object Oriented Concepts and python dictionary is mainly used data structure as adding and fetching 		       value is done at constant time complexity using dictionary.

pyredig.py --> This file contains redis in-built functionalities that are rendered by redis-py module.

Why use Python?

Python is a high level, interpreted and general purpose dynamic programming language that is widely used for analysis.
Redis is commonly used for caching, transient data storage and as a holding area for data during analysis in Python applications.
Also python is simple and easy to read and learn programming language that provides a large standard library which includes areas like internet protocols, string operations, web services tools and operating system interfaces.
