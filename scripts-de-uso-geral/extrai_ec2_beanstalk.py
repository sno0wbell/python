import boto3

session = boto3.Session(
    aws_access_key_id='',  
    aws_secret_access_key='', 
    region_name=''  
)

#Define o serviço do beanstalk
eb_client = session.client('elasticbeanstalk')

#Pega uma lista de todos os ambientes
response = eb_client.describe_environments()
environments = response['Environments']

#Para cada ambiente, obtenha as informações das instâncias
instance_ids = []

for environment in environments:
    environment_name = environment['EnvironmentName']
    response = eb_client.describe_environment_resources(
        EnvironmentName=environment_name
    )
    instances = response['EnvironmentResources']['Instances']
    
    for instance in instances:
        instance_ids.append(instance['Id'])

print(instance_ids)
