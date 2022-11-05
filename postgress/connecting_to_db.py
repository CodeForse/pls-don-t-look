import psycopg2
import pydantic

class Env_keys(pydantic.BaseSettings):
    db_pass: str

keys=Env_keys(_env_file='.env',_env_file_encoding='utf-8')

connect=psycopg2.connect(database='First Test',user='postgres',host='localhost',password=keys.db_pass)
cursor=connect.cursor()
cursor.execute('select * from Notifications where id=1')
print(cursor.fetchall())