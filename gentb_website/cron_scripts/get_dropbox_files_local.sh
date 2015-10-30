#! /bin/bash

# invoke virtualenv
export WORKON_HOME=/Users/rmp553/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon gentb

# Set the django module
#
export DJANGO_SETTINGS_MODULE=tb_website.settings.local

# run the script
cd /Users/rmp553/Documents/iqss-git/gentb-site/gentb_website/tb_website/apps/dropbox_helper/
python dropbox_retrieval_runner.py
