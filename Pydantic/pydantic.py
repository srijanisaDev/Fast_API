def insert_patient_data(name : str , age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted  into database.')

    else :
        raise TypeError("Incorrect Datatype")



insert_patient_data('srijan' , 21)     

## insert_patient_data('srijan' , '21')  ..... this will raise an error (TypeError)