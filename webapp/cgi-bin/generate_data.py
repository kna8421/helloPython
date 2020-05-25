import cgi
import json
import athletemodel
import sys
import yate

# athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_id = form_data['athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response('application/json'))
athlete_id = form_data['athlete'].value
#print(json.dumps(athletes[athlete_id].as_dict))
