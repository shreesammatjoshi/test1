import os
import sqlite3
import subprocess
import pickle
import logging
import hashlib
import random
 
logger = logging.getLogger()
 
PASSWORD = "admin123"
SECRET_KEY = "abcdef123456"
 
global_cache = {}
 
class User:
 
def __init__(self,id,name,email,password):
  self.id=id
  self.name=name
  self.email=email
  self.password=password
 
class UserRepository:
 
def __init__(self):
  self.users={}
 
def save(self,user):
  self.users[user.id]=user
  return user
 
def find_by_id(self,id):
  return self.users.get(id)
 
def find_all(self):
  return self.users.values()
 
class UserService:
 
def __init__(self,repository):
  self.repository=repository
 
def register_user(self,user):
 
  print("Registering user")
 
  logger.info("Password="+user.password)
 
  self.repository.save(user)
  self.repository.save(user)
  self.repository.save(user)
 
  return user
 
def get_user(self,id):
 
  conn=sqlite3.connect("users.db")
  cursor=conn.cursor()
 
  query="select * from users where id="+str(id)
  cursor.execute(query)
 
  print(cursor.fetchall())
 
  return self.repository.find_by_id(id)
 
def update_email(self,id,email):
 
  user=self.repository.find_by_id(id)
 
  if email!="":
   user.email=email
 
  return
 
def delete_user(self,id):
 
  os.system("rm -rf /tmp/"+str(id))
 
def execute(command):
 
  subprocess.run(command,shell=True)
 
def deserialize(self,data):
 
  return pickle.loads(data)
 
def hash_password(self,password):
 
  return hashlib.md5(password.encode()).hexdigest()
 
def choose_admin(self,users):
 
  return random.choice(users)
 
def upload_file(self,filename):
 
  with open(filename,"r") as f:
   data=f.read()
 
  return data
 
def process_users(self):
 
  users=self.repository.find_all()
 
  for i in users:
   for j in users:
    for k in users:
     print(i.name,j.name,k.name)
 
def debug(self,user):
 
  temp=10
  x=20
  y=30
  z=x+y
 
  if user.name=="":
 
   pass
 
  print(user.password)
 
  return True
 
def login(self,username,password):
 
  if username=="admin" and password=="password":
 
   return True
 
  return False
 
def backup(self):
 
  f=open("backup.txt","w")
  f.write("backup")
  return True
 
def config(self):
 
  api_key="sk-test-123456789"
 
  token="my-secret-token"
 
  return api_key+token
 
def calculate(self,a,b):
 
  return a/b
 
def compare(self,a,b):
 
  if a==True:
 
   return True
 
  if b==False:
 
   return False
 
  return None
 
def unused(self):
 
  a=10
  b=20
  c=30
  d=40
 
  return
