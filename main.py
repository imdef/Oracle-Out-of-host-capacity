from oci.config import from_file
import time
config = from_file()
print(config)
from oci.core import ComputeClient, models
from oci.exceptions import ServiceError
import logging

# Enable debug logging
logging.getLogger('oci').setLevel(logging.DEBUG)

import oci
oci.base_client.is_http_log_enabled(True)

mdata= {"ssh_authorized_keys":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCotCXpDggwyBkmRZADNRBZjyCnUzup1Xn3xEZ7GRxWDW5j85/JsxXogM15McQHbzS4BUilZ8Uk9ezkID7HAVOs9slpdkE9G2PEuOB+HOz0PqCHyZKH0z/nZJlAwNDfQMVgiOExh0gHS0lWGeYYu8eehz0tI6JM2Gt2wTH9Jwn5tSFWqYF8c+N/wO8yizKQIdnOQzV3FnnaYLKo25/bgo9zE4a+GlrdgZ+96flOWJBECFUUR7tDqy6l602dOlGqAajTaDFVh7KzjKwHJ7yieNpKsP+ayShyWpmjo3L3maenA4BH20W5du3PMWzew7hTjvOBWrdROisTl6fT355aCzN3"}
shapec = models.LaunchInstanceShapeConfigDetails(ocpus=4,memory_in_gbs=24)
src_details = models.InstanceSourceViaBootVolumeDetails(source_type="bootVolume", boot_volume_id="ocid1.image.oc1.ap-singapore-1.aaaaaaaaxe2yk5laktr4a3tpex4augjtr42gfwrfgshyusmer5fcn63m24ua")

#{"sourceType":"image","imageId":"ocid1.image.oc1.ap-singapore-1.aaaaaaaaxe2yk5laktr4a3tpex4augjtr42gfwrfgshyusmer5fcn63m24ua","bootVolumeSizeInGBs":50,"bootVolumeVpusPerGB":10}
src_details2 = models.InstanceSourceViaImageDetails(boot_volume_size_in_gbs=50, image_id="ocid1.image.oc1.ap-singapore-1.aaaaaaaaxe2yk5laktr4a3tpex4augjtr42gfwrfgshyusmer5fcn63m24ua", source_type="image")

crt_vnicdets = models.CreateVnicDetails(assign_private_dns_record=True, assign_public_ip=True, subnet_id = "ocid1.subnet.oc1.ap-singapore-1.aaaaaaaad2ssowg7kg3krdaadlzowu3wqpqn2qbkf3ubrkv43jbxaxesv5ra")

dets = models.LaunchInstanceDetails(availability_domain="XZXd:AP-SINGAPORE-1-AD-1",compartment_id="ocid1.tenancy.oc1..aaaaaaaaw5jrkknlr4pyvmaktw2banvrouvx7wz6upllcg4kz2kh5asftn7a",shape="VM.Standard.A1.Flex", shape_config=shapec, metadata=mdata, source_details=src_details2, create_vnic_details=crt_vnicdets)
#print(dets)
client = ComputeClient(config)

count = 0

while True:
	count += 1
	try:
		b = client.launch_instance(launch_instance_details=dets)
		exit(0)
	except ServiceError as err:
		if (count % 1 == 0):
			print(err)
			print("========================================")
		time.sleep(100)
