"""
# coding:utf-8
@Time    : 2021/01/03
@Author  : oriyao
@mail    : ylzhangyao@gmail.com
@File    : models.py
@Describe: User model
"""
from flask_login import UserMixin
from app import login_manager,mongo
from flask import current_app


class Mongouser(UserMixin):
    def __init__(self,username):
        self.username = username
    @staticmethod
    def check_password(password1,password2):
        if password1 == password2:
            return True
        return False
    def get_id(self):
        return self.username

@login_manager.user_loader
def user_loader(username):
    collection_users = mongo.db['oriyao_users']
    users = collection_users.find_one({"name": username})
    current_app.logger.info('login_manager.user_loader：' + str(users))
    if users:
        return Mongouser(username=users['name'])
    return None

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    collection_users = mongo.db['oriyao_users']
    current_app.logger.info('Login manager request loader：' + str(collection_users))
    users = collection_users.find_one({"name": username})
    if users:
        return Mongouser(username=users['name'])
    return None
