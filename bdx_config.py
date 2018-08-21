!# SGF BDX8-1

create vlan {vlan_name} tag {vlan_tag}
configure vlan {vlan_name} ipaddress {vlan_bdx_1_ip} {vlan_sm}
configure vlan {vlan_name} add port 1:22 tag
enable ipforwarding vlan {vlan_name}
create vrrp vlan {vlan_name} vrid {vr_id}
conf vrrp vlan {vlan_name} vrid {vr_id} add {vlan_gw}
enable vrrp vlan {vlan_name} vrid {vr_id}
conf ospf add vlan {vlan_name} area 0.0.0.1


!# SGF BDX8-2

create vlan {vlan_name} tag {vlan_tag}
configure vlan {vlan_name} ipaddress {vlan_bdx_2_ip} {vlan_sm}
configure vlan {vlan_name} add port 1:22 tag
enable ipforwarding vlan {vlan_name}
create vrrp vlan {vlan_name} vrid {vr_id}
conf vrrp vlan {vlan_name} vrid {vr_id} add {vlan_gw}
conf vrrp vlan {vlan_name} vrid {vr_id} priority 50
enable vrrp vlan {vlan_name} vrid {vr_id}
conf ospf add vlan {vlan_name} area 0.0.0.2

!# MTN BDX8-1

create vlan {vlan_name} tag {vlan_tag}
configure vlan {vlan_name} ipaddress {vlan_bdx_1_ip} {vlan_sm}
configure vlan {vlan_name} add port 1:27 tag
enable ipforwarding vlan {vlan_name}
create vrrp vlan {vlan_name} vrid {vr_id}
conf vrrp vlan {vlan_name} vrid {vr_id} add {vlan_gw}
enable vrrp vlan {vlan_name} vrid {vr_id}
conf ospf add vlan {vlan_name} area 0.0.0.3


!# MTN BDX8-2

create vlan {vlan_name} tag {vlan_tag}
configure vlan {vlan_name} ipaddress {vlan_bdx_2_ip} {vlan_sm}
configure vlan {vlan_name} add port 1:27 tag
enable ipforwarding vlan {vlan_name}
create vrrp vlan {vlan_name} vrid {vr_id}
conf vrrp vlan {vlan_name} vrid {vr_id} add {vlan_gw}
conf vrrp vlan {vlan_name} vrid {vr_id} priority 50
enable vrrp vlan {vlan_name} vrid {vr_id}
conf ospf add vlan {vlan_name} area 0.0.0.4
s0?Un6;:5<h7