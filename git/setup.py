#init setup script
import os
stream = os.popen('apt update')
output = stream.read()
print(output)
stream = os.popen('apt install -y git')
output = stream.read()
print(output)
stream = os.popen('pip3 install gitpython --system')
output = stream.read()
print(output)
