import rancher
import json
r = rancher.Client(url="http://127.0.0.1:8080/v2-beta", access_key="16AE439773F86224BB9D",
                   secret_key="ProvbtkakdHCMJwU12fpXoiW9wSiXUGUcPw9Ned4")
# project: '1a5'
# stack: '1st5'
# service: '1s7'
a = r.by_id_project('1a5')
st = r.by_id_stack('1st5')
s = r.by_id_service('1s5')

ss = a.services()
ss.create_service(name="s1")

print(a.services())
pass
