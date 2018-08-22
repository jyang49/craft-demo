import boto3

profile = 'default'
region = 'us-west-2'

def get_resource(service):
    session = boto3.Session(profile_name=profile, region_name=region)

    return session.resource(service)

