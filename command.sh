# Create bucket
python create_bucket.py --access-key minioadmin --secret-key minioadmin --bucket-name metaflow
# Run pipe
METAFLOW_SERVICE_URL=http://localhost:8080 METAFLOW_DEFAULT_METADATA="service" METAFLOW_DEFAULT_DATASTORE=s3 METAFLOW_DATASTORE_SYSROOT_S3=s3://metaflow METAFLOW_S3_ENDPOINT_URL=http://localhost:9000/ AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin python sample_pipe.py run
# Run jupyter server
METAFLOW_SERVICE_URL=http://localhost:8080 METAFLOW_DEFAULT_METADATA="service" METAFLOW_DEFAULT_DATASTORE=s3 METAFLOW_DATASTORE_SYSROOT_S3=s3://metaflow METAFLOW_S3_ENDPOINT_URL=http://localhost:9000/ AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin jupyter notebook --no-browser --NotebookApp.allow_origin='*'.
