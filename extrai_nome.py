import boto3

# Lista de IDs das instâncias
instance_ids = ["i-090061a33147da08c"]

# Crie uma sessão do Boto3
session = boto3.Session(
        aws_access_key_id = "AKIAUUODX4UCQGWQVUIY",
        aws_secret_access_key = "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",
        region_name="sa-east-1"
    )

# Crie um cliente EC2
ec2_client = session.client("ec2")

# Itere sobre a lista de IDs das instâncias
for instance_id in instance_ids:
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    
    instance = response["Reservations"][0]["Instances"][0]
    
    name = None
    for tag in instance.get("Tags", []):
        if tag["Key"] == "Name":
            name = tag["Value"]
            break
    
    print(f"Instance ID: {instance_id}, Name: {name}")

