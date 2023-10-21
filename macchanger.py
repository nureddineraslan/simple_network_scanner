import subprocess
import optparse
#interface ="eth0"
#mac_adress="00:1E:45:22:77:65"

parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adress")

(user_inputs,arguments)=parse_object.parse_args()

user_interface=user_inputs.interface
user_macadress=user_inputs.mac_adress
print(user_inputs.interface)
print(user_inputs.mac_adress)

print(parse_object.parse_args())
print("Mac changer started")
subprocess.call(["ipconfig",user_interface,"down"])
subprocess.call(["ipconfig",user_interface,"hw","ether",user_macadress])
subprocess.call(["ipconfig",user_interface,"up"])
 

