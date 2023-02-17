from oci.config import from_file
import time
config = from_file()
#print(config)
from oci.core import ComputeClient, models
from oci.exceptions import ServiceError

mdata= {"ssh_authorized_keys":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCotCXpDggwyBkmRZADNRBZjyCnUzup1Xn3xEZ7GRxWDW5j85/JsxXogM15McQHbzS4BUilZ8Uk9ezkID7HAVOs9slpdkE9G2PEuOB+HOz0PqCHyZKH0z/nZJlAwNDfQMVgiOExh0gHS0lWGeYYu8eehz0tI6JM2Gt2wTH9Jwn5tSFWqYF8c+N/wO8yizKQIdnOQzV3FnnaYLKo25/bgo9zE4a+GlrdgZ+96flOWJBECFUUR7tDqy6l602dOlGqAajTaDFVh7KzjKwHJ7yieNpKsP+ayShyWpmjo3L3maenA4BH20W5du3PMWzew7hTjvOBWrdROisTl6fT355aCzN3"}
shapec = models.LaunchInstanceShapeConfigDetails(ocpus=4,memory_in_gbs=24)
src_details = models.InstanceSourceViaBootVolumeDetails(source_type="bootVolume", boot_volume_id="ocid1.bootvolume.oc1.ap-singapore-1.")
crt_vnicdets = models.CreateVnicDetails(assign_private_dns_record=True, assign_public_ip=True, subnet_id = "ocid1.subnet.oc1.ap-singapore-1.")

dets = models.LaunchInstanceDetails(availability_domain="XZXd:AP-SINGAPORE-1-AD-1",compartment_id="ocid1.tenancy.oc1..",shape="VM.Standard.A1.Flex", shape_config=shapec, metadata=mdata, source_details=src_details, create_vnic_details=crt_vnicdets)
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
			print(err)
			print("========================================")
		time.sleep(10)

'''
{"code":"NotAuthenticated","message":"Date 'Fri, 17 Feb 2023 03:47:56 UTC' is not within allowed clock skew. Current 'Fri, 17 Feb 2023 03:53:53 UTC', valid datetime range: ['Fri, 17 Feb 2023 03:48:53 UTC', 'Fri, 17 Feb 2023 03:58:54 UTC']"}
'''
