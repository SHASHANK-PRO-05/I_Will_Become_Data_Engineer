import subprocess

sqoop2_command = ['sqoop2-tool']
options = ['verify']

if "VerifyTool has finished correctly" in subprocess.check_output(sqoop2_command + options):
    print("Your Sqoop 2 works perfectly")
else:
    print("Check your installation dude!!!!")
    exit(1)
    
print('######################################')
print('Starting your server and checking it ')
