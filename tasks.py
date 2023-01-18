import redis

'''Func to create task and push in redis queue'''
def create_task(task, queue):
    conn = redis.Redis(host='localhost', port=6379)
    conn.rpush(queue, task)


'''Func to read task from the beggining of queue'''
def get_task(queue):
    conn = redis.Redis(host='localhost', port=6379)
    
    task = conn.lpop(queue)
    
    return task
