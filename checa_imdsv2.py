import boto3

#Crie uma sessão do Boto3
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='' 
)

#Definindo EC2
ec2_client = session.client('ec2')

#Substitua INSTANCE_IDS pelos IDs das instâncias que você deseja verificar
instance_ids = ['']

for instance_id in instance_ids:
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    imdsv2_status = instance.get('MetadataOptions', {}).get('HttpTokens', 'Unknown')
    print(f"Instância {instance_id} - IMDSv2 Status: {imdsv2_status}")

