import sys
import requests
import pymysql
import time

create_table_sql = """CREATE TABLE `temp` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `time` DATETIME NOT NULL,
    `temperature` INTEGER NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;"""

def get_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='my-secret-pw',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def init():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)
        connection.commit()
    finally:
        connection.close()

def add():
    resp = requests.get("http://wttr.in/Detroit?format=j1")
    weather = resp.json()
    temperature = weather['current_condition'][0]['FeelsLikeC']

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `temp` (`time`, `temperature`) VALUES (%s, %s)"
            cursor.execute(sql, (time.strftime('%Y-%m-%d %H:%M:%S'), temperature))
        connection.commit()
    finally:
        connection.close()


def list_entries():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `id`, `time`, `temperature` FROM `temp`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                print(f"{data['id']}: {data['temperature']} at {data['time']}")
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Podaj komendę")
    elif sys.argv[1] == "init":
        init()
    elif sys.argv[1] == "add":
        add()
    elif sys.argv[1] == "list":
        list_entries()
