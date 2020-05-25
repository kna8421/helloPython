import cgi
import yate
import athletemodel
import athletelist
#啟用cgi (Common Gateway Interface 通用匣到介面)偵錯功能debug
import cgitb
from athletemodel import get_athlete_from_id, get_namesId_from_store

cgitb.enable()

#athletes = athletemodel.get_from_store()

#取得所有表單資料 並把它放入一個Dic
form_data = cgi.FieldStorage()
athlete_id = form_data['athlete'].value
athlete = get_athlete_from_id(athlete_id)
#HTML
print(yate.start_response())
print(yate.include_header("Coach's Kelly Timing Data"))
#print(yate.header("Athlete: " + athlete_name + ", Birthday: "+
                    #athletes[athlete_name].dob + "."))
print(yate.header("Athlete: " + athlete['Name'] + ", Birthday: "+
                    athlete['DOB'] + "."))
print(yate.para("The top times for this athlete are: "))
#print(yate.u_list(athletes[athlete_name].top3))
print(yate.u_list(athlete['top3']))

print(yate.para("The entire set of timing data is:" + str(athlete['data'])+ " (duplicates removed) ."))
print(yate.include_footer({"Home": "/index.html","Select another athlete": "generate_list.py"}))
