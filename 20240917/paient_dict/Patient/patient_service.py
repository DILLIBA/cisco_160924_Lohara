
from Patient import Patient
#2. patients{}
patients = {}

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id]=patient #pateints.append(pateint)
    print("patient data creatded succesfully")
#4. patient_remove(id)
def patient_remove(id):
    global patients
    #for patient in patients:
    patient=patients.get(id)
    if patient == None:
            print(f'no such data id{id}')
            return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        del patients[id]       # patients.remove(patient)
        print('Patient deleted successfully')
        #end if 
    #end for 
#5. patient_display()
# display by id
def patient_displayById(id):
    global patients
    patient =patients.get(id)
    if patient == None:
      print(f'no such id{id}')
      return
    print(patient)

def patient_display():
    global patients
    for id in patients:
        print(patients[id])

def patient_update(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return 
    print(patient)
    name = input(f'Enter new name({patient.name}):')
    patient.name = name 
    print('Patient updated successfully')

