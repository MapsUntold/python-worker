import runpod
import json
import subprocess

def handler(job):
    job_input = job['input']

    # Make data folder writeable
    cmd = '''
        mkdir /data
        chmod 777 /data
    '''
    subprocess.check_output(cmd, shell=True)

    # Add SSH key
    cmd = '''
        mkdir -p ~/.ssh
        echo "{ssh_key}" >> ~/.ssh/authorized_keys
        chmod 700 -R ~/.ssh
        generate_ssh_keys
        service ssh start 
    '''.format(ssh_key=job_input["ssh_key"])
    subprocess.check_output(cmd, shell=True)

    # Compile handler code
    handler = job_input.get('handler', '')
    code = compile(handler, 'handler', 'exec')
    exec(code)

    # Parse data
    path = job_input.get('data', '')
    with open(path) as json_file:
        data = json.load(json_file)

    try:
        # Start runner
        model = Runner.start(
            {
                "path": "/data/"
            },
            data
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
