import sqlite3
import glob
import athletemodel
from _sqlite3 import OperationalError

try:
    conn = sqlite3.connect('coachdata.sqlite')
    cursor = conn.cursor()

    data_file = glob.glob('data/*.txt')
    athletes = athletemodel.put_to_store(data_file)
    print(athletes)

    for each_ath in athletes:
        name = athletes[each_ath].name
        dob = athletes[each_ath].dob
        print(name+ " : " + dob)
        cursor.execute("INSERT INTO athletes (name, dob) VALUES (?,?)",(name,dob))
        conn.commit()

        cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?",(name,dob))
        the_current_id = cursor.fetchone()[0]
        for each_time in athletes[each_ath].clean_data:
            print(str(the_current_id) + " : " + str(each_time))
            cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?,?)", (the_current_id,  each_time))

        conn.commit()

#conn.close()
except OperationalError as oerror:
    print(str(oerror))
finally:
    conn.close()