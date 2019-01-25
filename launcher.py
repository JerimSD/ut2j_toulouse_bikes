import environment
from crontab import CronTab

cron = CronTab(user=True)

for job in cron:
    print(cron)

job = cron.new(command='python3 ' + environment.SCRIPT_PATH_FOLDER + 'main.py' +
                       ' >> ' + environment.LOG_PATH_FOLDER + 'main.log 2>&1')
job.minute.every(1)
cron.write()
