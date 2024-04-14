import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('no_iv.dat','rb') as f:
    ct = f.read()

for hours in range(24):
    for minutes in range(60):
        try_key = f"2024-02-14 {hours:02}:{minutes:02}".encode('ascii')
        cipher = AES.new(key=try_key, mode=AES.MODE_CBC, IV=b'superdupersecret')
        try:
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            try_key = try_key.decode('utf-8')
            with open(f'{try_key}','wb') as f:
                f.write(pt)
        except:
            pass
