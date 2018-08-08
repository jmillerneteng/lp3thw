#from sys import argv


# Select MTN or SGF and pass along to next hop


def start():
    deploy_type = int(input("what type of network?  1) Layer 2 or 2) Layer 3: > "))
    if deploy_type == 1:
        vlan_info()
    else:
        vlan_info()
        vrrp_info()

def vlan_info():
    vlan_name = input("vlan name: ")
    vlan_id = input("vlan_tag: ")
    port_tag = input("ports to be tagged: ")
    print(f"{vlan_name} , {vlan_id} \n tagging ports {port_tag}")
    l2_config = [(vlan_name), (vlan_id), (port_tag)]
    print_l2(l2_config)

def vrrp_info():
    vrrp_network = (input("newtork: "))
    vrrp_subnet = (input("subnet mask: "))
    vrrp_gateway = (input("gateway: "))
    vrrp_id = (input("vrrp id: "))
    print(f"{vrrp_network} {vrrp_subnet} and VRRP ID {vrrp_id}")

def dc_site():
    site = input("What site? > ")
    if site == "SGF":
        dc_sgf()
    elif site == "MTN":
        dc_mtn()


def print_l2(info):
    vlan_name = info[0]
    vlan_id = info[1]
    port_tag = info[2]
    print(f"""
    create vlan {vlan_name} tag {vlan_id}
    configure vlan {vlan_name} add port {port_tag} tagged
    """)


def dc_sgf():
    print("this is sgf land")
    vlan_info()


def dc_mtn():
    print("this is the mtn mtn")


#This is the start of the script file.
start()