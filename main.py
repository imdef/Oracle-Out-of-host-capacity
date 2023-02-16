from oci.config import from_file
import time
config = from_file()
#print(config)
from oci.core import ComputeClient, models
from oci.exceptions import ServiceError

'''
Get "availabilityDomain", "subnetID", "imageId" from browser request
Get ssh_authorized_keys

'''

mdata= {"ssh_authorized_keys":""}
shapec = models.LaunchInstanceShapeConfigDetails(ocpus=4,memory_in_gbs=24)
dets = models.LaunchInstanceDetails(availability_domain="XZXd:AP-SINGAPORE-1-AD-1",compartment_id="",shape="VM.Standard.A1.Flex", shape_config=shapec, image_id="" ,subnet_id="", metadata=mdata)
#print(dets)
client = ComputeClient(config)

count = 0

while True:
	count += 1
	try:
		b = client.launch_instance(launch_instance_details=dets)
		exit(0)
	except ServiceError as err:
		if (count % 100 == 0):
			print(err.status)
		time.sleep(10)
