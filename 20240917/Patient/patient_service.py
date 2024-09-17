from Patient import Patient
#2. patients[]
patients = []

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
#5. patient_display()
# display by id
def patient_displayById(id):
    global patients
    for patient in patients:
     if patient.id == id:
      print(patients)
     else:
      print("pateint not found")

def patient_display():
    global patients
    for patient in patients:
        print(patient)