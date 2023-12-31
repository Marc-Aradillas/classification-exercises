import os

import pandas as pd

from env import get_connection





db_url = get_connection('titanic_db')

query = '''
        SELECT * 
        FROM passengers
        '''

titanic_data = pd.read_sql(query, db_url)
titanic_data.head()





def get_titanic_data():

    filename = 'titanic.csv'

    if os.path.isfile(filename):

        print('Found your sauce my bro')

        return pd.read_csv(filename)
        
    else:

        print('Searching for the sauce my guy')
        
        url = get_connection('titanic_db')

        query = '''
                SELECT * 
                FROM passengers
                '''
        
        titanic_df = pd.read_sql(query, url)
        titanic_df.to_csv(filename, index = 0)

        return titanic_df

get_titanic_data()






db_url = get_connection('iris_db')

query = '''
        SELECT * 
        FROM species
        '''

iris_data = pd.read_sql(query, db_url)
iris_data.head()





def get_iris_data():

    filename = 'iris.csv'

    if os.path.isfile(filename):

        print('Found your sauce my bro')

        return pd.read_csv(filename)
        
    else:

        print('Searching for the sauce my guy')
        
        url = get_connection('iris_db')

        query = '''
                SELECT * 
                FROM species
                LEFT JOIN measurements ON species.species_id = measurements.species_id
                ;
                '''
        
        iris_df = pd.read_sql(query, url)
        iris_df.to_csv(filename, index = 0)

        return iris_df 

get_iris_data()






db_url = get_connection('telco_churn')

query = '''
        SELECT internet_service_type_id, contract_type_id, payment_type_id
        FROM customers
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        ;
        '''

telco_data = pd.read_sql(query, db_url)
telco_data.head()




def get_telco_data():

    filename = 'telco.csv'

    if os.path.isfile(filename):

        print('Found your sauce my bro')

        return pd.read_csv(filename)
        
    else:

        print('Searching for the sauce my guy')
        
        url = get_connection('telco_churn')

        query = '''
                SELECT *
                FROM customers
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN contract_types USING (contract_type_id)
                JOIN payment_types USING (payment_type_id)
                ;
                '''
        
        telco_df = pd.read_sql(query, url)
        telco_df.to_csv(filename, index = 0)
        
        return telco_df


get_telco_data()