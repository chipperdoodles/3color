import os

#flask instance folder, currently foldern named 3color Press in user's home folder
instfolder = os.path.join(os.path.expanduser("~"), '3color Press')

#Directory for custom themes in instance folder
THEME_DIR = os.path.join(instfolder, 'themes')
