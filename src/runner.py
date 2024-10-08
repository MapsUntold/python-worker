import runpod
import json
import subprocess
import os.path
from minio import Minio

tmp_path = "/data/data.json"

def get_from_s3(url, access_key, secret_key, bucket, filename):


def handler(job):
    job_input = job['input']

    # Job inputs
    task_id = job_input["task_id"]
    minio_url = job_input.get("minio_url", "")
    minio_bucket = job_input.get("minio_bucket", ""),
    minio_access_key = job_input.get("minio_access_key", "")
    minio_secret_key = job_input.get("minio_secret_key", ""),

    # Create minio client
    client = Minio(
        minio_url,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
    )

    # Download and parse input from minio
    input_path = job_input.get('input_path', "")
    client.fget_object(minio_bucket, input_path, tmp_path)
    with open(data_path) as json_file:
        data = json.load(json_file)

    # Compile handler code
    handler = job_input.get('handler', '')
    code = compile(handler, 'handler', 'exec')
    exec(code)

    try:
        # Start runner
        model_path = Runner.start(data)

        # Upload model to minio
        client.fput_object(
            "mu-algo-v1",
            task_name + "/" + str(i) + ".json",
            "/home/jovyan/mu_algo_v1/data/xx/" + str(i) + ".json"
        )

        return json.dumps({
            "success": True,
            "model": model,
        })
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        })


runpod.serverless.start({"handler": handler})
