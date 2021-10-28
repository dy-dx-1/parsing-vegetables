import pymysql 
from assets import Connect

def get_all_data(): 
    with open(r"C:\Users\Nicolas\Desktop\sql_login.txt", "r") as file:
        l_cred = [line[:-1] for line in file] 
    l_cred[3] = int(l_cred[3]) 
    celery_d = Connect(l_cred[0], l_cred[1], l_cred[2], l_cred[3], l_cred[4]).return_info()

    connection = pymysql.connect(user = celery_d[0], passwd = celery_d[1], host = celery_d[2], port = celery_d[3],
    database = celery_d[4], cursorclass=pymysql.cursors.DictCursor) 

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings") 
        all_listings = cursor.fetchall() 
        cursor.execute("SELECT * FROM price_changes")
        all_price_changes = cursor.fetchall() 
    return all_listings, all_price_changes