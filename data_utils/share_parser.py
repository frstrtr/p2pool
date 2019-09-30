# http://p2pool_node_address:port/web/share/FULL_SHARE_HASH
import json
from datetime import datetime

x = '''{"parent": "54e5bc1b56158efc9acd69bf43ac51238affb07a1b06e21a07a3083766793b80", "far_parent": "7e4c77963a07ce6b4eb0ee680d93aef30db0ec4bcd7d37f48c0a1c93a9e09a9e", "children": ["82fcc2a71b6fd5ce31d01d6472ba3a165939f23a763d84d091a0a36572a93a05"], "type_name": "SegwitMiningShare", "local": {"verified": true, "time_first_seen": 1569869196.022098, "peer_first_received_from": ["95.79.35.133", 9326]}, "share_data": {"timestamp": 1569869193, "target": 156927141650155954348325850089668575111908255560852417124191174656, "max_target": 4707815856442722889440051044652149594519850189028566296518570541056, "payout_address": "LRW6WhZbr4uWCSYD5Eg2Roztnzhp9K6w2h", "donation": 0.0, "stale_info": null, "nonce": 1385289580, "desired_version": 34, "absheight": 12817311, "abswork": 29467678264036718636}, "block": {"hash": "ca5fca0931f3740a6cb22926a6ea0f67e9699cf1f55ce7dbffcdc46cc0f1acc0", "header": {"version": 536870912, "previous_block": "db7291fe459eff090c5926c289052e30ad23035fdc3f89de71c9d452af4517b9", "merkle_root": "248e2f04c34817abe3799aed4a651f9c94c7e83441ae462ccc62a8138bb9b15c", "timestamp": 1569869190, "target": 2486002006428317978918043680667014355192849654093261981089792, "nonce": 2103207830}, "gentx": {"hash": "22f295abf113dc1c80586827594ea8ded9b88c2f5841946b1a352b380a18a6d8", "coinbase": "03be1d1a", "value": 12.51564297, "last_txout_nonce": "0000000100000004"}, "other_transaction_hashes": []}}'''
# share data example output


def share_parser(share_json_string):
    # Normalizing json data according to python standards, i.e true = True, false = False, null = None
    share_json = json.loads(share_json_string)

    for n in share_json:
        if n == 'share_data':
            print 'SHARE DATA:', '\n'
            for n1 in share_json[n]:
                print '\t', n1, ':', share_json[n][n1], '\n'
                if n1 == 'timestamp':
                    print '\t', n1, 'human friendly:', datetime.utcfromtimestamp(
                        share_json[n][n1]).strftime('%Y-%m-%d %H:%M:%S'), '\n'
        elif n == 'local':
            print 'LOCAL:', '\n'
            for n2 in share_json[n]:
                print '\t', n2, ':', share_json[n][n2], '\n'
                if n2 == 'time_first_seen':
                    print '\t', n2, 'human friendly:', datetime.utcfromtimestamp(
                        share_json[n][n2]).strftime('%Y-%m-%d %H:%M:%S'), '\n'

        elif n == 'block':
            print 'BLOCK:', '\n'
            for n3 in share_json[n]:
                if n3 == 'header':
                    print '\t', 'HEADER:', '\n'
                    for n4 in share_json[n][n3]:
                        print '\t\t', n4, ':', share_json[n][n3][n4], '\n'
                        if n4 == 'timestamp':
                            print '\t\t', n4, 'human friendly:', datetime.utcfromtimestamp(
                                share_json[n][n3][n4]).strftime('%Y-%m-%d %H:%M:%S'), '\n'
                elif n3 == 'gentx':
                    print '\t', 'GENTX:', '\n'
                    for n4 in share_json[n][n3]:
                        if n4 == 'coinbase':
                            # Add esc symbols for string output (better look)
                            repr_string = repr(
                                share_json[n][n3][n4].decode("hex"))
                            print '\t\t', n4, ':', repr_string, '\n'
                        else:
                            print '\t\t', n4, ':', share_json[n][n3][n4], '\n'
                else:
                    print '\t', n3, ':', share_json[n][n3], '\n'
        else:
            print n, ':', share_json[n], '\n'


share_parser(x)
