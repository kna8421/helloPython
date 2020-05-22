import json
#import nester
from nester import print_list


movices = ['Frozen','Thor',["HP1","HP2","HP3","HP4"]]
#nester.print_list(movices,1)
print_list(movices,True)

to_transfer_json = json.dumps(movices)
print(to_transfer_json)

from_transfer = json.loads(to_transfer_json)
print(from_transfer)