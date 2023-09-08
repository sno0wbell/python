import boto3

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='' 
)

ambientes_para_atualizar = ["nome-ambiente-1", "nome-ambiente-2"]

eb_clientt = session.client('elasticbeanstalk')

# Loop pelos nomes dos ambientes e atualiza a configuração DisableIMDSv1
for ambiente in ambientes_para_atualizar:
    elasticbeanstalk = session.client('elasticbeanstalk')
    response = elasticbeanstalk.update_environment(
        EnvironmentName=ambiente,
        OptionSettings=[
            {
                'Namespace': 'aws:autoscaling:launchconfiguration',
                'OptionName': 'DisableIMDSv1',
                'Value': 'true'
            },
        ]
    )
    print(f"Configuração DisableIMDSv1 atualizada para o ambiente {ambiente}")

print("Atualizações concluídas para todos os ambientes.")

