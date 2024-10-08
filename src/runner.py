import runpod
import json
import subprocess
import os.path

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

    # Wait for input file
    input_path = job_input.get('data', '')
    while not os.path.exists(input_path):
        time.sleep(1)
        
    # Parse data
    with open(input_path) as json_file:
        data = json.load(json_file)

    # Compile handler code
    handler = job_input.get('handler', '')
    code = compile(handler, 'handler', 'exec')
    exec(code)

    try:
        # Start runner
        model = Runner.start(
            {
                "output_path": "/data/"
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
