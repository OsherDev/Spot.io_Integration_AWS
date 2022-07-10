import json
import requests
import os

def lambda_handler(event, context):
  #Vars
  account_id = os.environ["Account_Id"]
  cluster_id = os.environ["Cluster_Id"]
  auth_token = os.environ["Auth_Token"]
  batch_size = os.environ["BatchSize"]
  #URL
  url = 'https://api.spotinst.io/aws/ec2/group/{0}/clusterRoll?accountId={1}'.format(cluster_id,account_id)

  #Payload
  payload = json.dumps({
      "roll": {
      "comment": "This roll has been performed as part of Windows Update process and developers responsibility" ,
      "batchSizePercentage": batch_size
      }
  })
  #Headers
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+auth_token}
  #Send Response
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
