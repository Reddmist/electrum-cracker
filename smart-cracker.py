import itertools
import electrum

words = u'cargo series gloom wing normal velvet view sock wing rib fat acid'
pub = "xpub661MyMwAqRbcFdEFzAGcVaokv2MXeRTFRjZVUu5eNusyYYkcmV4HWBCjuodH82WhmRytEyHLQSRsNSuNo8DjtzDoYk69o7pfHwi9N5gTqa7"


i = 0
z = len(words.split()) - 1
while i < z:
  s = electrum.WalletStorage('/home/clint/.electrum/wallets/smart-cr-tst')
  arr = words.split()
  arr[i], arr[i+1] = arr[i+1], arr[i]
  seed = " ".join(arr)
  try:
    w = electrum.Wallet.from_text(seed, None, s)
    print seed
    if w.get_master_public_key() == pub:
      print 'success'
      break
  except BaseException:
    pass
  i += 1
