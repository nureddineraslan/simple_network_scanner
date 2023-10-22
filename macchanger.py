import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Enter IP address")
    (user_input, arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input    

def scan_my_network(ip):
    arp_request_pack = scapy.ARP(pdst=ip, psrc="your_source_ip_address")
    broadcast_pack = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_pack/arp_request_pack
    answered_list, unanswered_list = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_input = get_user_input()
scan_my_network(user_input.ip_address)
