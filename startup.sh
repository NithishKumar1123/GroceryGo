#! /bin/sh
echo "Welcome to the setup." 
echo "This will activate the local virtual env and run the required python files."
echo "You can rerun this without any issues."

if [ -d ".env" ];
then
    echo "Enabling virtual env"
else
    echo "No virtual env. Please run 'local_setup.sh' first"
    exit N
fi

# Activate virtual env
source venv/bin/activate
cd /home/site/wwwroot
gunicorn --bind 0.0.0.0:8000 app:app
