from google.cloud import storage

print("Iniciando o script...")

client = storage.Client.from_service_account_json('chave/fine-slice-304523-378cca0bed61.json')
print("Client criado com sucesso.")

bucket_name = 'enem-bucket-bronze'
file_path = 'MICRODADOS_ENEM_2019.csv'
destination_blob_name = 'bronze/microdados_enem_2019.csv' 

bucket = client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

print("Tentando fazer upload do arquivo...")
blob.upload_from_filename(file_path)

print(f"Arquivo enviado para gs://{bucket_name}/{destination_blob_name}")
