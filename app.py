from flask import Flask, request, jsonify
import os
import boto3
from botocore.config import Config

app = Flask(__name__)

my_config = Config(
    region_name = 'us-east-1'
)
rds_data = boto3.client('rds-data', config=my_config, aws_access_key_id='Your access id', aws_secret_access_key='your secret access id')

#Database Configuration Items
aurora_db_name = 'shubhgargdb' #os.environ['DB_NAME']
aurora_cluster_arn = 'your cluster arn' #os.environ['CLUSTER_ARN']
aurora_secret_arn = 'your secret arn' #os.environ['SECRET_ARN']

@app.route('/getPerson') # API 1 - getPerson
def getPerson():
    personId = request.args.get('personId') #extracting the personId from the request
    response = callDbWithStatement("SELECT * FROM Persons WHERE personId='" + str(personId) + "'" )
    person = {} #creating a response object to store our records in
    records = response['records'] #extracting the records array from our response
    for record in records: # we are simply getting the data in an order, it is serialised beacuase that is how dataapi works
        person['personId'] = record[0]['longValue']
        person['firstName'] = record[1]['stringValue']
        person['lastName'] = record[2]['stringValue']
        #basically we a creating an object that maps directly to the result we should get back after we query
    print(person) # printing out the contents so that we can see it in our docker container
    return jsonify(person) # since we can not return a dictonary , we use jsonify to convert it

@app.route('/createPerson',  methods=['POST']) # API 2 - createPerson
def createPerson():
    request_data = request.get_json()
    personId = str(request_data['personId'])
    firstName = request_data['firstName']
    lastName = request_data['lastName']
    callDbWithStatement("INSERT INTO Persons(personId, firstName, lastName) VALUES ('" 
    + personId + "', '" + firstName + "', '" + lastName + "');")
    return ""
    
def callDbWithStatement(statement):
    response = rds_data.execute_statement( # we are calling the execute_statement api
            database = aurora_db_name, # we are passing it the key and credentials
            resourceArn = aurora_cluster_arn,
            secretArn = aurora_secret_arn,
            sql = statement,
            includeResultMetadata = True # for column names 
        )
    print("Making Call " + statement)
    print(response) #Delete this in production
    return response

if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)
