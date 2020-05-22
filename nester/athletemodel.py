import os
import pickle
from Athlete import AthleteList, get_coach_data

#Get and Pull from Pickle
def put_to_store(file_list):
    
    os.chdir('../nester/source')
    print(os.getcwd())
    all_athlete = {}
    for f in file_list:
        ath = get_coach_data(f)
        all_athlete[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athlete,athf)
    except IOError as ioerror:
        print('IO Error (put to store):' + str(ioerror))
    return all_athlete


def get_from_store():
    all_athlete ={}
    os.chdir('../nester/source')
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioerror:
        print('IO Error (get from store):' + str(ioerror))
    return all_athlete

#Run...
#print(dir())

# the_files = ['james.txt','sarah.txt','mikey.txt','julie.txt']
# data = put_to_store(the_files)
# print(data)

# for athlete in data:
#     print(data[athlete].name + ' ' + data[athlete].birthday)

data_copy = get_from_store()
for athlete in data_copy:
    print(data_copy[athlete].name + ' ' + data_copy[athlete].bir)