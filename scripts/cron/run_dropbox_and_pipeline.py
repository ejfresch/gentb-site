"""
12/4/2015 - quick fix

Until, the HMS cron server is able to run needed MySQL libs,
this is a hackish workaround.

Supervisor will be used to keep this script alive--at least for the weekend.
"""
import subprocess
import time

CMD_LOAD_ENVIRONMENT = ' . /etc/profile.d/Modules.sh'
#CMD_LOAD_ENVIRONMENT = ' . /opt/lsf/conf/profile.lsf'

class DropboxPipelineWorkaround(object):
    """
    Poor man's cron substitute.  Infinite looping script under supervisord
    """

    def __init__(self, run_forever=True):

        if run_forever is True:
            while 1:
                self.run_workaround()
        else:
            self.run_workaround()

    def pause(self, num_minutes=10):
        """
        Pause for several minutes
        """
        print 'Pausing for %s minutes' % num_minutes
        num_seconds = num_minutes * 60
        time.sleep(num_seconds)

    def run_workaround(self):
        """
        Run dropbox retrieveal, pause
        Run pipeline, pause
        """
        self.run_dropbox_retrieval_command()
        self.pause(num_minutes=10)

        self.run_pipeline_command()
        self.pause(num_minutes=10)

    def run_dropbox_retrieval_command(self):
        """
        Run what should usually be a cron job to retrieve Dropbox files
        """
        print 'Run Dropbox retrieval command--and not waiting for results'

        cmd_dropbox_retrieval = '%s;\
         /www/gentb.hms.harvard.edu/code/gentb-site/gentb_website/cron_scripts/get_dropbox_files_prod_hms.sh'\
          % (CMD_LOAD_ENVIRONMENT)

        #cmd_args = cmd_dropbox_retrieval.split()

        cmd_process = subprocess.Popen(cmd_dropbox_retrieval,\
                shell=True,\
                stdin=None,\
                stdout=None,\
                stderr=None)
                #close_fds=True)


    def run_pipeline_command(self):
        """
        Run the pipeline command
        """

        print 'Run pipeline command--and not waiting for results'

        cmd_pipeline = '%s; /www/gentb.hms.harvard.edu/code/gentb-site/gentb_website/cron_scripts/run_pipeline_prod_hms.sh' % (CMD_LOAD_ENVIRONMENT)

        #cmd_args = cmd_pipeline.split()

        cmd_process = subprocess.Popen(cmd_pipeline,\
                shell=True,\
                stdin=None,\
                stdout=None,\
                stderr=None)
                #close_fds=True)



if __name__ == '__main__':
    DropboxPipelineWorkaround(run_forever=True)