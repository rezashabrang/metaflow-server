"""Create a bucket in S3"""
import boto3
from metaflow._vendor import click
from botocore.client import Config


@click.command()
@click.option("--access-key", required=True)
@click.option("--secret-key", required=True)
@click.option("--bucket-name", default="metaflow")
@click.option("--endpoint-url", default="http://localhost:9000")
def main(access_key, secret_key, bucket_name, endpoint_url):
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=None,
        config=Config(signature_version="s3v4"),
        verify=False,
    )

    # Example: Create a new bucket
    already_present_buckets = s3.list_buckets()["Buckets"]
    if not any([bucket["Name"] == bucket_name for bucket in already_present_buckets]):
        s3.create_bucket(Bucket=bucket_name)
        click.secho(
            f"Bucket {bucket_name} created successfully.", fg="green", bold=True
        )
    else:
        click.secho(
            f"Bucket {bucket_name} already present. Skipping creation.", fg="yellow"
        )


if __name__ == "__main__":
    main()