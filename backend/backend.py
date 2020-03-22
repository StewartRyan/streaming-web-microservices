import redis
conn = redis.Redis('redis-service')

user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}

conn.hmset("pythonDict", )

t = conn.hgetall("pythonDict")

print(t)
