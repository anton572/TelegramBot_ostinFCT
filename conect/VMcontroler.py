from google.oauth2 import service_account
from google.cloud import compute_v1
class userVM():
    def __init__(self,P,Z,N,Loger=None):
        self._instance_client = compute_v1.InstancesClient()
        self.project_id=P
        self.zone=Z
        self.instance_name=N
        self.Loger=Loger
    def StartVM(self):
        operation = self._instance_client.start(
            project=self.project_id,
            zone=self.zone,
            instance=self.instance_name)
        self.Loger.print(operation.result())
    def StopVM(self):
        operation = self._instance_client.stop(
            project=self.project_id,
            zone=self.zone,
            instance=self.instance_name
        )
        self.Loger.print(operation.result())
    def get_stait(self):
        request =compute_v1.AggregatedListInstancesRequest()
        request.project =self.project_id
        respons=self._instance_client.aggregated_list(request=request)
        for zone, response in respons:
            if response.instances and self.zone == zone:
                for instance in response.instances:
                    if instance.name==self.instance_name:
                        stait=instance.status
                        return stait
