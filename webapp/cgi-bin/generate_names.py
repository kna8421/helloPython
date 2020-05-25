# #!/user/local/bin/python3
import json
import athletemodel
import yate

#names = athletemodel.get_names_from_store()
names = athletemodel.get_namesId_from_store()
print(yate.start_response())
print(json.dumps(sorted(names)))
