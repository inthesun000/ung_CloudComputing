import os, uuid
import sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


try:
  print("한국방송통신대학교 4학년 2학기 클라우드 컴퓨팅")

  connect_str = ""
  container_name = "mall-blob-container"
  local_path = "../ung_CloudComputing/blobs/"

  if not os.path.exists(local_path):
    os.makedirs(local_path)

  container_client = blob_service_client.get_container_client(container=container_name)

  generator = container_client.list_blobs()

  for blob in generator:
    download_file_path = os.path.join(local_path, blob.name)
    print(f"\nDownloading {blob.name} to \t" + local_path + blob.name)
    with open(download_file_path, "wb") as download_file:
      download_file.write(container_client.download_blob(blob.name).readall())

except Exception as ex: 
  print('Exception:')
  print(ex)
  
