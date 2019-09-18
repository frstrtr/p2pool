import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


# P2P_PREFIX = 'f9beb4d9'.decode('hex') # disk magic and old net magic
P2P_PREFIX = 'e3e1f3e8'.decode('hex')  # new net magic
P2P_PORT = 8333
ADDRESS_VERSION = 0
ADDRESS_P2SH_VERSION = 5
HUMAN_READABLE_PART = 'bitcoincash'
RPC_PORT = 8332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
    (yield helper.check_block_header(bitcoind, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')) and  # genesis block
    # 478559 -- Bitcoin Cash fork
    (yield helper.check_block_header(bitcoind, '000000000000000000651ef99cb9fcbe0dadde1d424bd9f15ff20136191a5eec')) and
    # 556767 -- Bitcoin SV fork
    (yield helper.check_block_header(bitcoind, '000000000000000001d956714215d96ffc00e0afda4cd0a96c96f8d802b1662b')) and
    (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
))


def SUBSIDY_FUNC(height): return 50*100000000 >> (height + 1)//210000


POW_FUNC = data.hash256
BLOCK_PERIOD = 600  # s
SYMBOL = 'BSV'


def CONF_FILE_FUNC(): return os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser(
    '~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf')


BLOCK_EXPLORER_URL_PREFIX = 'https://blockchair.com/bitcoin-sv/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://blockchair.com/bitcoin-sv/address/'
TX_EXPLORER_URL_PREFIX = 'https://blockchair.com/bitcoin-sv/transaction/'
SANE_TARGET_RANGE = (2**256//2**32//100000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
