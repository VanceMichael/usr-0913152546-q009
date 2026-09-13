import sqlite3,os
from flask import Flask
app=Flask(__name__);os.makedirs('data',exist_ok=True);DB=os.getenv('DB_PATH','data/results.db')
def init(): c=sqlite3.connect(DB);c.execute('create table if not exists results(id integer primary key,student text,score integer)');c.commit();return c
@app.get('/health')
def health(): return {'status':'ok'}
if __name__=='__main__':init();app.run(host='0.0.0.0',port=8080)
