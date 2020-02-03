git pull git@gitlab.com:marinesebastian/mazcomunicacion.git

source venv/bin/activate
python manage.py migrate
deactivate

systemctl restart gunicorn.service

echo "Code updated"
