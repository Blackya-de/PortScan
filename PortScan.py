import socket
import sys

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument")

print("-"*50)
print("Scaning target " + target)
print("-"*50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target , port))
        if result == 0 :
            print("Port " + str(port) + " is open")

        s.close()

except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    sys.exit()
except socket.error:
    sys.exit()
