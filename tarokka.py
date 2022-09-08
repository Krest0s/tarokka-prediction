import sqlite3
import random
from flask import Flask

con = sqlite3.connect("tarokka.db")
cursor = con.cursor()
random_list = list(range(1, 41))
a = []
for i in range(3):
    prediction = random.choice(random_list)
    random_list.remove(prediction)
    cursor.execute(f"Select player_speech from treasure_location where id = {prediction}")
    a.append(cursor.fetchone()[0])
    print(a)
    # cursor.execute(f"Select master_info from treasure_location where id = {prediction}")
    # print(cursor.fetchone()[0])
    # cursor.execute(f"Select map from treasure_location where id = {prediction}")
    # print(cursor.fetchone()[0])
    # print()
con.close()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return a[0]


if __name__ == '__main__':
    app.run()
