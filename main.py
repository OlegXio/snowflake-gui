import eel
import os
import requests

if not os.path.exists('web'):
    os.makedirs('web')

with requests.get('https://snowflake.torproject.org/embed.html') as response:
    if response.status_code == 200:
        htmlfile = open('web/index.html','w')
        htmlfile.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SNOWFLAKE PROXY RELAY</title>
    <script src="eel.js"></script>
</head>
<body bgcolor="green">
    <iframe src="https://snowflake.torproject.org/embed.html" width="320" height="240" frameborder="0" scrolling="no"></iframe>
</body>
</html>''')
        htmlfile.close()

eel.init("web")
eel.start("index.html",size=(370, 298),mode='chrome')
