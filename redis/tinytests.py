from tinyredis import TinyRedis

"""
Stand up Redis server on MacOS:
  brew install redis
  redis-server
"""

cli = TinyRedis()

print "SET a 1"
print cli.set('a', 1)
print "GET a"
print cli.get('a')

print "SADD b 1 2 3"
print cli.sadd('b', 1, 2, 3)
print "SMEMBERS b"
print cli.smembers('b')
