import redis


def create_task(task, queue):
    conn = redis.Redis(host='localhost', port=6379)
    conn.rpush(queue, task)


def get_task(queue):
    conn = redis.Redis(host='localhost', port=6379)
    
    task = conn.lpop(queue)
    
    return task
