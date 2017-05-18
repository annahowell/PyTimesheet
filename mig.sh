#!/usr/bin/env bash

set -x

project_folder="/Users/anna/Python/timesheet"

echo -n "Enter app "
read app

python3 ${project_folder}/manage.py makemigrations ${app}


echo -n "Enter migration "
read mig


python3 ${project_folder}/manage.py sqlmigrate ${app} ${mig}
python3 ${project_folder}/manage.py migrate
