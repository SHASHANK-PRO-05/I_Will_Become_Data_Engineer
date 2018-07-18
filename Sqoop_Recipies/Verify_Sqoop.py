import subprocess

sqoop2_command = ['sqoop2-tool']
options = ['verify']

print(subprocess.check_output(sqoop2_command + options))
