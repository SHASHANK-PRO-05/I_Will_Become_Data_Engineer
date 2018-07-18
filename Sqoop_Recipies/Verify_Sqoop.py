# This is a sqoop script that verifies your sqoop2 installation.
# PS. If are looking to change port of your Sqoop. I would recommend
# doing in config file and I won't be covering that. But if you do, you
# can always pass that as command line option --port portno
#
# Sqoop Version Used 1.99.7
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument('--port', required=False, help="port no on which the sqoop2 " +
                                               "server will start")
args = vars(ap.parse_args())
port = args['port'] if not args['port'] else 12000
if __name__ == '__main__':
    import subprocess

    sqoop2_command = ['sqoop2-tool']
    options = ['verify']

    if "VerifyTool has finished correctly" in str(subprocess.check_output(sqoop2_command + options)):
        print("Your Sqoop 2 works perfectly")
    else:
        print("Check your installation dude!!!!")
        exit(1)

    print('######################################')
    print('Starting your server and checking it ')

    sqoop2_command = ['sqoop2-server']
    options_start = ['start']
    options_end = ['stop']
    wget = ['wget']
    wget_options = ['-q0', '-', f"localhost:{port}/sqoop/version"]

    status, output = subprocess.getoutput(''.join(cmd + ' ' for cmd in (sqoop2_command + options_start)))
    if status != 0:
        print('Sqoop 2 server was not able to start')
        exit(1)
    else:
        print('Sqoop is started')

    json_output = json.loads(subprocess.check_output(wget + wget_options))
    print(json_output)

    status, output = subprocess.getoutput(''.join(cmd + ' ' for cmd in (sqoop2_command + options_end)))
    exit(0)
