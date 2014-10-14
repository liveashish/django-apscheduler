from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )
    help = 'Help text goes here'

    def handle(self, **options):
         print "This is a command"
         print('Tick! The time is: %s' % datetime.now())

	
		 if __name__ == '__main__':
		     scheduler = BackgroundScheduler()
		     scheduler.add_job(handle, 'interval', seconds=3)
		     scheduler.start()
		     #print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
		 
		     try:
		        # This is here to simulate application activity (which keeps the main thread alive).
		         while True:
		             time.sleep(10)
		     except (KeyboardInterrupt, SystemExit):
		         scheduler.shutdown()  # Not strictly necessary if daemonic mode is enabled but should be done if possible