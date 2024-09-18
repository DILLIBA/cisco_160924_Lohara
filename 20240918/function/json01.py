import json
patient = [
    {'di':101,'name':'mahesh'},
    {'di':102,'name':'dilli'},
    {'di':103,'name':'babu'},
    {'di':103,'name':'danush'}
]
patient_str = json.dumps(patient)
print(patient, patient_str)
with open('patient_data.json','w') as pt_db:
    json.dump(patient,pt_db)


patient_str2 = json.loads(patient_str)
print(patient, patient_str2)

with open('patient_data.json','r') as pt_db:
    patient_str3=json.load(pt_db)
    print(f'read sucessfully{patient_str3}')
