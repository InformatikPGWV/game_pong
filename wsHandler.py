# Imports
try:
    from websockets import connect
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    from websockets import connect
