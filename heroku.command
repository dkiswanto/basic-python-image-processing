# For existing repositories, simply add the heroku remote
heroku git:remote -a kinto-pcd

# running python script
heroku run python manage.py shell