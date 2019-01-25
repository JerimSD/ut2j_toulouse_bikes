from crontab import CronTab

cron = CronTab(user=True)

for job in cron:
    print(cron)

cron.remove_all()
cron.write()

print("All clear")
