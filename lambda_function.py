
import boto3


def get_volume_id_from_arn(volume_arn):
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    
        

def lambda_handler(event, context):
    
# {
#   "version": "0",
#   "id": "cb950f8e-83d9-ab5e-348a-29bac93c1205",
#   "detail-type": "EBS Volume Notification",
#   "source": "aws.ec2",
#   "account": "905418298691",
#   "time": "2024-04-01T05:09:48Z",
#   "region": "ap-south-1",
#   "resources": [
#     "arn:aws:ec2:ap-south-1:905418298691:volume/vol-06699b4ba0c64af0b"
#   ],
#   "detail": {
#     "result": "deleted",
#     "cause": "",
#     "event": "deleteVolume",
#     "request-id": "80adcb8a-09ff-4c49-8857-2342bdb8293f"
#   }
# }

    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn) 
    
    
    
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',
)

