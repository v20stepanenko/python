import json
import os
import hashlib
from datetime import datetime

db = {}

def pass_hash(password):
    b_password = str.encode(password, encoding = 'utf-8')
    return str(hashlib.pbkdf2_hmac('sha256', b_password, b'salt2018', 100000))

def save():
    file = open('db.json', 'w', encoding = 'utf-8')
    file.write(json.dumps(db))
    file.close()
    return True

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def download_by_file():
    if not is_non_zero_file('db.json'):
        return
    file = open('db.json', encoding = 'utf-8')
    if file.read:
        db.update(json.load(file))
    file.close()

def create_user(*, login, password, email):
    if not password or not email or login in db :
        return False
    db[login] = { 'password' : pass_hash(password), 'email' : email, 'notes':[]}
    return save()

def check_authorization(*, login, password):
    if login in db and db[login]['password'] == pass_hash(password) :
        return True
    else:
        return False

def new_note(*, login, title, body):
    user = db[login]
    time_cretae = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
    note = {'title': title, 'body': body, 'datetime': time_cretae}
    user['notes'].append(note)
    return save()

def delete_notes(*, login, num):
    user = db[login]
    index = num - 1
    notes = user['notes']
    if len(notes) > num:
        del notes[index]
        return save()

def get_notes(login):
    user = db[login]
    notes = user['notes']
    list_notes_user = []
    for index in range(0, len(notes)):
        list_notes_user.append([index + 1, notes[index]])
    return list_notes_user

def get_note(*, login, num):
    user = db[login]
    notes = user['notes']
    print(notes[0])
    if len(notes) >= num:
        return notes[num - 1]
