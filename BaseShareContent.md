VERSION = 0 #Версия шары.
VOTING_VERSION = 0 #desired version
SUCCESSOR = #None/SegwitMiningShare

small_block_header_type:
    version #2/4 bytes
    previuos_block #int 32 bytes
    timestamp #int 4 bytes
    bits # 4 bytes
    nonce # 4 bytes

share_info_type:
    share_data:
        privious_share_hash #int 32 bytes
        coinbase #VarStrType, максимальное количество симповол Str равен максимальному значениию unsigned long long.
        nonce # 4 bytes
        
        if Share.Version >= 34:
            address #VarStrType
        else 
            pubkey_hash # int 20 bytes

        subsidy #int 8 bytes
        donation #int 2 bytes
        stale_info #orphan/doa/None | Enum 1 byte
        desired_version #unsigned long long/unsigned int

        if [Segwit активен в этой версии шары [проверка через is_segwit_activated]]:
            segwit_data:
                segwit_data:
                    txid_merkle_link:
                        branch #list int 32 bytes * the number of objects in the list
                        index # alwasy 0
                    wtxid_merkle_root #int 32 bytes
                txid_merkle_link:
                    branch #list int 32 bytes * the number of objects in the list
                    index # 0
                wtxid_merkle_root #int 32 bytes
                
        
        if Share.Version < 34:
            new_transaction_hashes #list int 32 bytes * the number of objects in the list
            transaction_hash_refs #list unsigned long long/unsigned int * the number of objects in the list
        
        far_share_hash #int 32 bytes
        max_bits # 4 bytes 
        bits # 4 bytes
        timestamp # 4 bytes
        absheight # 4 bytes
        abswork # 16 bytes


share_type:
    min_header #small_block_header_type выше описан.
    share_info:
        [share_info_type,который описан выше]
    ref_merkle_link:
        branch #list int 32 bytes * the number of objects in the list
        index # alwasy 0
    last_txout_nonce #int 8 bytes
    hash_link: [28 строка, data.py]
        state #FixedStr 8 bytes
        extra_data #FixedStr 0 bytes
        lenght # 4 bytes
    merkle_link:
        branch #list int 32 bytes * the number of objects in the list
        index # alwasy 0


ref_type:
    identifier #FixedStr, 1byte?
    share_info:
        [share_info_type,который описан выше]


net #from BaseShare.__init___ agrs
peer_addr #from BaseShare.__init___ agrs
contents #from BaseShare.__init___ agrs

gentx_before_refhash — тут упакован DONATION_SCRIPT, который используется в def generate_transaction[data.py, строка 387],

gentx_size — размер gentx
gentx_weight — вес gentx
cached_types — ?