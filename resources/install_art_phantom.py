#!/usr/bin/python
import json
import base64
import requests
file_contents = open('/phantom_apps/phatomicredteam.tgz', 'rb').read()
encoded_contents = base64.b64encode(file_contents)
payload = {'app': encoded_contents}
requests.post('https://192.168.38.110/rest/app',
                auth=('admin', 'password'),
                data=json.dumps(payload))
