#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author @morihi_soc
# (c) 2018 @morihi_soc
import sys
import traceback
import base64
args = sys.argv

MAX_DISPLAY_NUM = 15
DIFFERENT_IP = True
attacker_ip = {}
target_port = {}
path = {}
account_name = {}
account_pass = {}

if len(args) != 2:
    print("Usage: make-wsw.py wowhoneypot_log")
    sys.exit(1)

filename = args[1]

def htmlspecialchars(str):
    return str.replace("&", "&amp;").replace("\"", "&quot;").replace("'", "&apos;").replace("<", "&lt;").replace(">", "&gt;")

index = 1
try:
    with open(filename, "r") as input_file:
        line = input_file.readline()
        while line:
            lines = line.split(" ")

            if not len(lines) == 10:
                line = input_file.readline()
                continue

            try:
                rawdata = base64.b64decode(lines[9]).decode('utf-8')
            except:
                line = input_file.readline()
                continue
            if "\nAuthorization: Basic " in rawdata:
                if DIFFERENT_IP:
                    if lines[2] in attacker_ip.values():
                        line = input_file.readline()
                        continue

                s = rawdata.find("Authorization: Basic ")
                e = rawdata.find("\n", s+21, len(rawdata))
                try:
                    auth = base64.b64decode(rawdata[s+21:e]).decode('utf-8').split(":")
                    if len(auth[0]) < 1 and len(auth[1]) < 1:
                        line = input_file.readline()
                        continue
                except:
                    line = input_file.readline()
                    continue
                account_name[index] = auth[0]
                account_pass[index] = auth[1]

                attacker_ip[index] = lines[2]
                target_port[index] = lines[3].split(":")[1]
                path[index] = lines[4].split('"')[1] + " " + lines[5] + " " + lines[6].split('"')[0]
                index = (index + 1) % MAX_DISPLAY_NUM
            line = input_file.readline()
except:
    ex, ms, tb = sys.exc_info()
    traceback.print_tb(tb)

index = 1
output_data = ""
while index < MAX_DISPLAY_NUM:
    if not index in attacker_ip or len(attacker_ip[index]) < 1:
        sys.exit(0)
    data = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\r".format(htmlspecialchars(attacker_ip[index]),
                                                                                    htmlspecialchars(target_port[index]),
                                                                                    htmlspecialchars(path[index]),
                                                                                    htmlspecialchars(account_name[index]),
                                                                                    htmlspecialchars(account_pass[index]))
    index = index + 1
    output_data = output_data + data

html_before = '''\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Wall of Sheep for WOWHoneypot</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  </head>
  <body style="background-color:black;">
    <font color="lime">
    <header><center><h1>Wall of Sheep for WOWHoneypot</h1></center></header>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-2"></div>
        <div class="col-md-8">
          <table class="table">
            <thead>
              <tr>
                <th>Attacker IP</th>
                <th>Target Port</th>
                <th>Path</th>
                <th>Account Name</th>
                <th>Account Password</th>
              </tr>
            </thead>
            <tbody>
<!-- data start -->
'''

html_after = '''\
<!-- data end -->
          </tbody>
          </table>
        </div>
        <div class="col-md-2"></div>
      </div>
    </div>
    </font>
    <footer>
      <div class="row">
        <div class="col-md-10"></div>
        <div class="col-md-2"><font color="white">(c)2018 <a href="https://www.morihi-soc.net/">morihi-soc</a></font></div>
      </div>
    </footer>
  </body>
</html>
'''

with open("index.html", "w") as file:
    file.write(html_before)
    file.write(output_data)
    file.write(html_after)
