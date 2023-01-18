from tasks import init_redis, get_task
import validators
import alchemy
import time

def work(pool, queue):
    task = get_task(pool, queue)
    
    if not task:
        return time.sleep(1)
    
    uname, amount = tuple(task.decode('utf-8').split(':'))

    validators.validate_transaction(
        uname=uname,
        amount=int(amount),
        withdrawal=True
        )
        


def main():

    while True:
        '''users names are names of the queues'''
        users = alchemy.get_users_list()
        
        for user in users:
            work(pool='', queue=user)


if __name__ == '__main__':
    main()