import runpod

def handler(job):
    job_input = job['input']

    requirements = job_input.get('requirements', '')
    handler = job_input.get('handler', '')
    data = job_input.get('data', '')

    return f"Hello, {handler}!"


runpod.serverless.start({"handler": handler})
