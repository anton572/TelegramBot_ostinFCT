import os
import json
token=os.environ.get('API_token_bot')
vm_data=os.environ.get("VMDATA")

vm_data=json.loads(vm_data)
vm_data['private_key']=vm_data['private_key'].replace('{__--]','\n')

P,Z,N=os.environ.get("PZN").split('\\')
