import redis
client = redis.Redis(host='localhost',port=6379)
client.set('language','Python') 
print(client.get('language'))
print(client.expire('language',10))
print(client.get('language'))

client.execute_command('ZADD', "Aman_Srivastava", 1, "Current Amazon SDE Intern")
client.execute_command('ZADD', "Aman_Srivastava", 2, "Former HackerRank SDE Intern")
client.execute_command('ZADD', "Aman_Srivastava", 3, "General Secretary, JGEC")
client.execute_command('ZADD', "Aman_Srivastava", 4, "Coders Club Secretary, JGEC")

print(client.execute_command('ZRANK', "Aman_Srivastava" , "Current Amazon SDE Intern"))

client.execute_command('ZADD', "Examination_Preparation", 1, "Unacademy")
client.execute_command('ZADD', "Examination_Preparation", 2, "GradeUp")
client.execute_command('ZADD', "Examination_Preparation", 3, "BYJUS")

print(client.execute_command('ZRANK', "Aman_Srivastava" , "General Secretary, JGEC"))
print(client.execute_command('ZRANGE', "Examination_Preparation",0,2))