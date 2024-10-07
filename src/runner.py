import runpod

def handler(job):
    job_input = job['input']

    handler = job_input.get('handler', '')
    data = job_input.get('data', '')

    code = compile(handler, 'handler', 'exec')
    output = exec(code)

    return f"Hello, {output}!"


runpod.serverless.start({"handler": handler})
