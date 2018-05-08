
from picamera import PiCamera
from paramiko import SSHClient
from scp import SCPClient

camera = PiCamera()

camera.capture('gotcha.jpg')

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('skillpouch.com')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('gotcha.jpg')
#scp.get('test2.txt')

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
#scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
