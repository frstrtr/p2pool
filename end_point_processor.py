# http://p2pool_node_address/peer_versions

# endpoint example output

x = {"208.84.223.121:9326": "16.0-172-g6339c1e", "66.151.242.154:9326": "77.0.0-12-g5493200-dirty", "185.25.60.199:9326": "16.0-156-gf63da63-dirty", "92.169.160.5:60772": "16.0-160-g9b5938a",
     "96.241.229.65:41798": "16.0-157-g280e48f-dirty", "40.78.105.218:9326": "16.0-157-g280e48f-dirty", "95.79.35.133:9326": "16.0-160-g9b5938a-dirty", "178.238.236.130:9326": "16.0-160-g9b5938a-dirty"}
n = 1
for ip_addr in x:

    port = ip_addr.split(':')
    ver_split = x[ip_addr].split('-')
    #print ver_split
    if len(ver_split) == 4:
        if len(port[0]) > 14:
            print n, '\t', port[0], '\t', port[1], '\t\t', ver_split[0], '\t\t', ver_split[1], '\t\t', ver_split[2], '\t\t', ver_split[3]
        else:
            print n, '\t', port[0], '\t\t', port[1], '\t\t', ver_split[
                0], '\t\t', ver_split[1], '\t\t', ver_split[2], '\t\t', ver_split[3]
    elif len(ver_split) == 3:
        if len(port[0]) > 14:
            print n, '\t', port[0], '\t', port[1], '\t\t', ver_split[0], '\t\t', ver_split[1], '\t\t', ver_split[2]
        else:
            print n, '\t', port[0], '\t\t', port[1], '\t\t', ver_split[0], '\t\t', ver_split[1], '\t\t', ver_split[2]
    else:
        if len(port[0]) > 14:
            print n, '\t', port[0], '\t', port[1], '\t\t', x[ip_addr]
        else:
            print n, '\t', port[0], '\t\t', port[1], '\t\t', x[ip_addr]
    n += 1
