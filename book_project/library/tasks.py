from celery import shared_task


@shared_task
def add(x, y):
    return x + y

""" Ветка bugfix """


gef greting(name):
    print("Привет", name)


greting("Alex")
greting("Noy")

