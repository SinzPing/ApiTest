import time
import hmac
import hashlib
import base64
import urllib.parse


def get_sign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SECc7f78be15a6930f95a0095cf5d50a5062eed42dd462114e3ace4b2aef2799202'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)
    params = '&timestamp=%s&sign=%s' % (timestamp, sign)
    return params
