import os

from dotenv import load_dotenv
from tronpy import Tron, providers, keys

load_dotenv()

client = Tron(
    network='mainnet', 
    provider=providers.HTTPProvider(
        endpoint_uri=os.getenv('TRANSATRON_NODE'),
        jw_token=os.getenv('TRANSATRON_API_KEY'),
        timeout=100
    )
)

# private_wallet = client.generate_zkey()

private_wallet = {
    'sk': '0f97c8e16ffe446aa0ca6c8837e04b74f729747f1f9ef496422a7cbc425ceb70', 
    'ask': '1544bc967b72d717234d4d44684301f3fea9af5738a9862fb846270fe2e24e02', 
    'nsk': 'd0daa8ef9191752c2796a6334ec90ba75dba0da7b7f5f82a4129af78f9703f08', 
    'ovk': 'f010d0bf031898e7d7dad9729588b7824bccf219b649182b175dc2f6e26fef2f', 
    'ak': '6245dca6015465d687f4baa73a1585b375b1acbaf5847371dca3564396c5f32e', 
    'nk': 'acdafbf0cb29e78f13a2b69b0243938c99abc651f503f040f4692f16c1725273', 
    'ivk': '4f0ae8f7fba7499d1667934921bfecaf7ff463d1ab541aebbc105846137b7806', 
    'd': '70d74084df6ae9cedd9dad', 
    'pkD': '44fc8079288b2893482789fabff3ed5e4c6bbb329d3b85c396ee5deeb84316eb', 
    'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc'
}

private_wallet_2 = {
    'sk': '041b826c27bfc481da56f099924942bdf9b43c48e5297832836b5b607c6ec6c6', 
    'ask': '3a4c588f4b6c35992f8a06311a537a68c8c87c3c404c579260c2e94f019d2003', 
    'nsk': 'c486a7049b4c94b843523c4a8c06b8fe7ba99c3713582380ea13b16c4ca23e0a', 
    'ovk': '36dfe4a381f9c7c14763925d6acbaa43a0ff02ddd265ecd470a97dbaddc50f37', 
    'ak': 'b51c9ccd3a2a55581364357d7b407c3479f0f1c47d1906331fd2c4baf2f3018a', 
    'nk': '7537ea90a2654370c1c3b2f997060feff3cc71e3b2b7fdc1190fc9e365ce0123', 
    'ivk': '2f40992a1ab1f88d9f5dd4bf4fdbb424be70cc0f08bb45171015870ddd102d03', 
    'd': 'c0a001e96c74c07daa531f', 
    'pkD': '8a58e21a08edec6d6d5b30c624606cd773b6575343f7920e8bed0d11be338b88', 
    'payment_address': 'ztron1czsqr6tvwnq8m2jnr7993cs6prk7cmtdtvcvvfrqdnth8djh2dpl0ysw30ks6yd7xw9cs8q0nq8'}

private_key = keys.PrivateKey(bytes.fromhex(os.getenv('PRIVATE_KEY')))
public_wallet = private_key.public_key.to_base58check_address()




shielded_trc20 = client.get_contract_as_shielded_trc20('TQEuSEVRk1GtfExm5q9T8a1w84GvgQJ13V')

# 0. Mint 3 private notes: 0.25, 0.5, 1 USDT each

allowance = shielded_trc20.trc20.functions.allowance(public_wallet, shielded_trc20.shielded.contract_address)

print('Allowance:', allowance)

if allowance == 0:
    print('Approving...')
    shielded_trc20.trc20.functions.approve('TQEuSEVRk1GtfExm5q9T8a1w84GvgQJ13V', 1 * 10 ** 18).with_owner(public_wallet).build().sign(private_key).broadcast().wait()

# txn = (
#     shielded_trc20.mint(public_wallet, private_wallet['payment_address'], 1 * 10 ** 6, 'memo1usdt').fee_limit(500_000_000).build().sign(private_key)
# )
# print(txn.broadcast().wait())
# https://tronscan.org/#/transaction/602a407e8fc5c29431cb5c9da2de1b58f216b54db78f7c1f5ba1d0460faccbad

# txn = (
#     shielded_trc20.mint(public_wallet, private_wallet['payment_address'], 5 * 10 ** 5, 'memo05usdt').fee_limit(500_000_000).build().sign(private_key)
# )
# print(txn.broadcast().wait())
# https://tronscan.org/#/transaction/a702e8dc588e427cb79431ff94ae57b4ac81b38c41840957090712d2bea750d4

# txn = (
#     shielded_trc20.mint(public_wallet, private_wallet['payment_address'], 25 * 10 ** 4, 'memo025usdt').fee_limit(500_000_000).build().sign(private_key)
# )
# print(txn.broadcast().wait())
# https://tronscan.org/#/transaction/14fde475ee75670943da080408349015b529b535852f94c4aea310f63856bede

# notes = shielded_trc20.scan_incoming_notes(private_wallet, client.get_latest_block_number() - 1000)
notes = [
    {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f3175736474', 'value': 1000000, 'rcm': '8b29f281c751baeac9f5cb0939ae09938c05f3a4537048a3a8c3f380d55e1e0d'}, 'txid': '602a407e8fc5c29431cb5c9da2de1b58f216b54db78f7c1f5ba1d0460faccbad', 'index': 0, 'position': 61265, 'is_spent': False}, 
    {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f303575736474', 'value': 500000, 'rcm': '9f8b75205857a791ee22a52da43ee462f68aec4936e209b80b0d19404c518b0c'}, 'txid': 'a702e8dc588e427cb79431ff94ae57b4ac81b38c41840957090712d2bea750d4', 'index': 0, 'position': 61266, 'is_spent': False}, 
    {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f30323575736474', 'value': 250000, 'rcm': '92e95179216aa4a16d744462f1450004d4058ef4d339916d3edf18dfcead0603'}, 'txid': '14fde475ee75670943da080408349015b529b535852f94c4aea310f63856bede', 'index': 0, 'position': 61267, 'is_spent': False}
]


# 1. Consolidate 2 notes (transfer) into 2 private notes (1 for the user and 1 for us)

# txn = (
#     shielded_trc20.transfer(
#         private_wallet, 
#         [notes[1], notes[2]],
#         ((private_wallet['payment_address'], 600000, "memo06usdt"), (private_wallet_2['payment_address'], 150000, "memo015usdt"))
#     )
#     .with_owner(public_wallet)
#     .fee_limit(500_000_000)
#     .build()
#     .sign(private_key)
# )
# print(txn.broadcast().result())
# https://tronscan.org/#/transaction/a0b2c38df03d191f1d764ec461b040ebd935f036ff6c9e8caee68dee36ce85be

# notes_1 = shielded_trc20.scan_incoming_notes(private_wallet, client.get_latest_block_number() - 1000)
notes_1 = [
    {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f3175736474', 'value': 1000000, 'rcm': '8b29f281c751baeac9f5cb0939ae09938c05f3a4537048a3a8c3f380d55e1e0d'}, 'txid': '602a407e8fc5c29431cb5c9da2de1b58f216b54db78f7c1f5ba1d0460faccbad', 'index': 0, 'position': 61265, 'is_spent': False}, 
    # SPENT {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f303575736474', 'value': 500000, 'rcm': '9f8b75205857a791ee22a52da43ee462f68aec4936e209b80b0d19404c518b0c'}, 'is_spent': True, 'txid': 'a702e8dc588e427cb79431ff94ae57b4ac81b38c41840957090712d2bea750d4', 'index': 0, 'position': 61266}, 
    # SPENT {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f30323575736474', 'value': 250000, 'rcm': '92e95179216aa4a16d744462f1450004d4058ef4d339916d3edf18dfcead0603'}, 'is_spent': True, 'txid': '14fde475ee75670943da080408349015b529b535852f94c4aea310f63856bede', 'index': 0, 'position': 61267}, 
    {'note': {'payment_address': 'ztron1wrt5ppxldt5uahva44z0eqre9z9j3y6gy7yl40lna40yc6amx2wnhpwrjmh9mm4cgvtwkprldmc', 'memo': '6d656d6f303675736474', 'value': 600000, 'rcm': '8122a6d83cd676de0d4d71a5036f11be18afaa2dbf35e0cd657932126ef7da02'}, 'txid': 'a0b2c38df03d191f1d764ec461b040ebd935f036ff6c9e8caee68dee36ce85be', 'index': 0, 'position': 61268, 'is_spent': False}
]

# notes_2 = shielded_trc20.scan_incoming_notes(private_wallet_2, client.get_latest_block_number() - 1000)
notes_2 = [
    {'note': {'payment_address': 'ztron1czsqr6tvwnq8m2jnr7993cs6prk7cmtdtvcvvfrqdnth8djh2dpl0ysw30ks6yd7xw9cs8q0nq8', 'memo': '6d656d6f30313575736474', 'value': 150000, 'rcm': '5895e0f7d8e3a999f3c2364d41ff9128f1a89ec01ca0d3e24a69fff223ad170b'}, 'txid': 'a0b2c38df03d191f1d764ec461b040ebd935f036ff6c9e8caee68dee36ce85be', 'index': 1, 'position': 61269, 'is_spent': False}
]


# 2. Burn 1 note into 1 public output and 1 public/private output

txn = (
    shielded_trc20.burn(private_wallet, notes_1[0], (public_wallet, 750000, "memo075usdt"), (private_wallet_2['payment_address'], 250000, "memo025usdt"))
    .with_owner(public_wallet)
    .fee_limit(500_000_000)
    .build()
    .sign(private_key)
)
print(txn.broadcast().result())
# Transaction failed: tronpy.exceptions.UnknownError: ('Account resource insufficient error.', 'BANDWITH_ERROR')
# Will fix this later