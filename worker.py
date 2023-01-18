from tasks import init_redis, get_task
import validators
import alchemy
import time

def work(queue):
    task = get_task(queue)
    
    '''If task not exist then sleeping for time before check another one queue'''
    if not task:
        return time.sleep(1)
    
    '''Divide byte string from queue by two parts - username and amount of transaction'''
    '''Then put 2 parts in 2 vars via tuple'''
    uname, amount = tuple(task.decode('utf-8').split(':'))

    '''velidating transaction with next saving in database'''
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
            '''Send new user-queue to handle'''
            work(queue=user)


if __name__ == '__main__':
    main()