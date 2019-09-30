# http://p2pool_node_address:port/web/share/FULL_SHARE_HASH
import json
x = '''{"parent": "01b37570d7d051cbabbfe5346e2616a01b2d30fb3891482d57d584682a893544", "far_parent": "7c4d2a8cc178da712051adbae96d64bfdf41e3ab46fa704936e4a88d8838f636", "children": ["0e0aded8ae4118f918aa64e0601a793338ea9c23b7b4119c201b26a12187ee50"], "type_name": "SegwitMiningShare", "local": {"verified": True, "time_first_seen": 1569855014.741917, "peer_first_received_from": ["104.42.74.172", 42926]}, "share_data": {"timestamp": 1569855009, "target": 204855675758224598306640411455836090894735482053417996229890015232, "max_target": 4405512243804544602843994967992560721082963273026172177170334482432, "payout_address": "LWsbt5xb5poxz8UYjUjXzCvoMNwLaM5Qhk", "donation": 0.0, "stale_info": None, "nonce": 3877144208, "desired_version": 34, "absheight": 12816371, "abswork": 29467199543963842321}, "block": {
    "hash": "dc9aceecac61bc89961294e600391127755159d8a06948f7f1075a1ad2537061", "header": {"version": 536870912, "previous_block": "6c234ce57c79efea6111bce210cb6dd0b10bd3c313a5457936192781328050c5", "merkle_root": "7860d9eecc2c6cdba891dd1e3dc2ffd8a6b48feeb43cb422f09c44353b9721f5", "timestamp": 1569854995, "target": 2486002006428317978918043680667014355192849654093261981089792, "nonce": 599714903}, "gentx": {"hash": "dcced93f40a773dbfbd0cf8e809b4fcd139a0dce4d810c3c27c88c6f826d6c8c", "coinbase": "03621d1a0766727374727472", "value": 12.50408574, "last_txout_nonce": "0000000300000000"}, "other_transaction_hashes": []}}'''
# share data example output


def share_parser(share_json_string):
    # Normalizing json data according to python standards, i.e true = True, false = False, null = None
    share_json = json.loads(share_json_string)

    for n in share_json:
        print n
        if n == 'share_data':
            print 'SHARE DATA:', '\n'
            for n1 in share_json[n]:
                print '\t', n1, ':', share_json[n][n1], '\n'
        elif n == 'local':
            print 'LOCAL:', '\n'
            for n2 in share_json[n]:
                print '\t', n2, ':', share_json[n][n2], '\n'
        elif n == 'block':
            print 'BLOCK:', '\n'
            for n3 in share_json[n]:
                if n3 == 'header':
                    print '\t', 'HEADER:', '\n'
                    for n4 in share_json[n][n3]:
                        print '\t\t', n4, ':', share_json[n][n3][n4], '\n'
                elif n3 == 'gentx':
                    print '\t', 'GENTX:', '\n'
                    for n4 in share_json[n][n3]:
                        if n4 == 'coinbase':
                            r_string = share_json[n][n3][n4].decode("hex")
                            print '\t\t', n4, ':', r_string, '\n'
                        else:
                            print '\t\t', n4, ':', share_json[n][n3][n4], '\n'
                else:
                    print '\t', n3, ':', share_json[n][n3], '\n'
        else:
            print n, ':', share_json[n], '\n'


share_parser(x)
