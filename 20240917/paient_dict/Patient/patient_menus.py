import json
from patient_menu import menus
#8. driver program
menus()
with open('patient_dict.json','w') as pt_db:
    json.dump(Patient.name,pt_db)
    print('written file succefull') 