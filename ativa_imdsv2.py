import boto3

session = boto3.Session(
    aws_access_key_id='', 
    aws_secret_access_key='', 
    region_name=''  
)

# Lista de IDs de instância que você deseja atualizar
instance_ids_to_update = ['i-x, i-y']  # Substitua pelos IDs desejados

# Selecionando o serviço ec2
ec2_client = session.client('ec2')

# Atualize as instâncias com base nos IDs fornecidos
for instance_id in instance_ids_to_update:
    print(f"Atualizando instância {instance_id}")
    ec2_client.modify_instance_metadata_options(
        InstanceId=instance_id,
        HttpTokens='required'
    )
    print(f"Instância {instance_id} atualizada para utilizar IMDSv2.")

