from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management import call_command

def backup_database_every_two_hours():
    print('Database Backed UP')
    call_command('dbbackup',clean=True)
    # This meean -->>> python manage.py dbbackup --clean

@util.close_old_connections
def delete_old_job_executions(max_age=10):
  DjangoJobExecution.objects.delete_old_job_executions(max_age)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(),'default')
    scheduler.add_job(backup_database_every_two_hours,'interval',seconds=10,jobstore='default',id="backup_database_every_two_hours",replace_existing=True)
    scheduler.add_job(delete_old_job_executions,'interval',seconds=10,jobstore='default',id='delete_old_job_executions',replace_existing=True)
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
     