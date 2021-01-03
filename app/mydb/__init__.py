from flask import current_app
import pymongo


def initial_mongodb():
    current_app.logger.info('Initial my mongodb.')

    # app.logger.info(app.config["MONGO_URI_WITHOUTDB"])
    myclient = pymongo.MongoClient(current_app.config['MONGO_URI_WITHOUTDB'])
    dblist = myclient.list_database_names()
    current_app.logger.info(dblist)
    #
    mymongodb = input("Input your new database name:")

    if mymongodb in dblist:
        print("DB already exist!")
        print("Delete DB First:" + mymongodb)
        myclient.drop_database(mymongodb)
    else:
        print("Create new database!")
        # ADD user to admin, for new database connection
    print("Create new admin user!")
    # myclient.admin.add_user(current_app.config['MONGO_DATABASE_ADMIN_USER'],current_app.config['MONGO_DATABASE_PASSWD'], roles=[{'role': 'readWrite', 'db': mymongodb}])
    myclient.admin.add_user('testuser',
                            'testpassword', roles=[{'role': 'readWrite', 'db': mymongodb}])
    # Connect to new databse
    my_mongo_db = myclient[mymongodb]
    # Create collection for users
    print("Create new collection!")
    collection_users = my_mongo_db["oriyao_users"]
    # Create default admin user document
    default_admin = {"name": current_app.config['MONGO_DATABASE_USER'],
                     "email": current_app.config['MONGO_DATABASE_EMAIL'],
                     "password": current_app.config['MONGO_DATABASE_PASSWD'],
                     "is_admin": 'True',
                     "is_locked": 'False',
                     "create_time": '',
                     "last_login_time": ''
                     }
    collection_users.insert_one(default_admin)
    print("Create new collection user!")
    collection_list = my_mongo_db.list_collection_names()
    print(collection_list)
    users = collection_users.find_one({"name": 'oriyao'})
    print(users)