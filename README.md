# AWS-PROJECT-Docker-based-Flask-App-with-Aurora-Serverless

## SERVICES USED

- AWS RDS
- Postman
- Docker
- AWS Secrets Manager 
- Flask
- Aurora Serverless
- GitHub
- Git


------------



## APPROACH

Creating a Flask based Docker app that interacts with Aurora  Serverless using the Data API. The application will have two endpoints, One for "create Person" and the other for " get Person".


------------



## WALKTHROUGH 

#### Create a RDS DataBase :

We create an Amazon Aurora Serverless database with that will store our "persons" table.
![creating a database](https://user-images.githubusercontent.com/53488130/121803689-65b1a600-cc60-11eb-801f-557471f7bfbc.PNG)
![capacity settings for the database](https://user-images.githubusercontent.com/53488130/121803694-68ac9680-cc60-11eb-9f6e-a3d535a75cdb.PNG)


We will be using the Data API for to interact with Aurora Serveless using a RESTful API. 
It will allow us to run SQL Queries against the DataBase.
![enable the data api in the database](https://user-images.githubusercontent.com/53488130/121803700-6e09e100-cc60-11eb-92d1-10e1037d323b.PNG)

![database created](https://user-images.githubusercontent.com/53488130/121803730-837f0b00-cc60-11eb-94dd-d60a7965f075.PNG)

#### Create a Secret in the AWS Secrets Manager

We create a Secret that will store our Credentials for the RDS DataBase. This secret will then be used by the DataApi to access our RDS Database.
![aws secrets manager details](https://user-images.githubusercontent.com/53488130/121803710-72ce9500-cc60-11eb-9dbc-557b43ca8b8d.PNG)
![give a secret name to the secretsmanager](https://user-images.githubusercontent.com/53488130/121803759-9eea1600-cc60-11eb-99fc-bfa94532c4fa.PNG)
![secret is created](https://user-images.githubusercontent.com/53488130/121803766-a27d9d00-cc60-11eb-9945-f5b653ac8091.PNG)

#### Use the Query Editor to create a query 

We use the RDS query editor to query and use SQL to enter data into a table.
![create a query in our database and connect to it](https://user-images.githubusercontent.com/53488130/121803770-a9a4ab00-cc60-11eb-8dd0-b0feaed80195.PNG)
![create a simple query in the query editot](https://user-images.githubusercontent.com/53488130/121803772-ab6e6e80-cc60-11eb-899d-f0b89863bc5f.PNG)
![ourput of the query](https://user-images.githubusercontent.com/53488130/121803776-ad383200-cc60-11eb-8e8e-d323861a7887.PNG)
![inserting a second query into the database](https://user-images.githubusercontent.com/53488130/121803777-b0cbb900-cc60-11eb-9d48-a8adc4150424.PNG)
![successful output of second query](https://user-images.githubusercontent.com/53488130/121803779-b2957c80-cc60-11eb-9ef3-c50bd83d270a.PNG)

#### Editing our Flask App Code

We make changes to our Flask app code and add our Credentials in it.
While it is advisible to use an environment variable to store the credentials.
I have not done so here.

The code itself is quite easy and it's working is explained in the "app.py" file through code comments.

We change the Following code variables and put in our Credentials from AWS

`- aws_access_key_id`
`- aws_secret_access_key`

Database Configuration Items :

`- aurora_db_name`
`- aurora_cluster_arn`
`- aurora_secret_arn`

![variables to be changed in flask app](https://user-images.githubusercontent.com/53488130/121803793-c0e39880-cc60-11eb-90aa-5fbf3cfd11cc.PNG)

#### Create an IAM Policy

We create/add iam policies ,"AmazonRDSDataFullAccess" and "SecretsManagerReadWrite" to our existing iam user .These policies will allow us to interact with our DataBase with several permissions.
![add policies to your iam user](https://user-images.githubusercontent.com/53488130/121803785-bc1ee480-cc60-11eb-925e-e9f18071c72a.PNG)

#### Starting a Docker Container

We build our Flask app in Docker Container that will interact with our DataBase through the DataApi.

We had the code locally stored so we will do it locally. We can also git the code from our github repo as well.

We change our $PWD to the Flask App and run the following Commands to build our container and run the app : 

`docker build -t flask-app .` 
This will build our current app .

`docker run -d -p 8081:8081 flask-app ` 
This will create our Docker container and run our Flask App in it.
![the docker container running](https://user-images.githubusercontent.com/53488130/121803817-e5d80b80-cc60-11eb-8680-1a19de8d405e.PNG)

We can now see our Container running in docker in our localhost.
![docker container is running](https://user-images.githubusercontent.com/53488130/121803821-e8d2fc00-cc60-11eb-812d-74a146cca077.PNG)

#### Using Postman to make Post/Get Request

We can now simply use Postman to run our Get/Post requests.

![PostMan working Proof](https://user-images.githubusercontent.com/53488130/121803838-f8524500-cc60-11eb-8ebc-17cd41d906bb.jpeg)
![docker container showing logs](https://user-images.githubusercontent.com/53488130/121803862-0e600580-cc61-11eb-8248-ac76e6da7a0e.PNG)

In a similar way we can run POST Requests and those requests can be verified through AWS RDS query editor as well.
(I forgot to take ScreenShot for the same so i am showing a ScreenShot of my friend's rds query editor )
![sending put requests to the api](https://user-images.githubusercontent.com/53488130/121803903-38192c80-cc61-11eb-8808-514039ae6ca2.PNG)
![final result](https://user-images.githubusercontent.com/53488130/121803907-394a5980-cc61-11eb-9537-4b805b188ffc.PNG)

------------


**PROJECT COMPLETE**


------------


