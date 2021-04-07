#!/usr/bin/python
#  -*- coding: utf-8 -*-

# 直接Debug运行脚本就可以使用app 默认的网址http://127.0.0.1:5000/ 进行Debug
#

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route('/user/<username>')
def get_user(username):
    return "resp:{0}".format(username)

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     import argparse
#
#     parser = argparse.ArgumentParser(description='Development Server Help')
#     parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
#                         help="run in debug mode (for use with PyCharm)", default=False)
#     parser.add_argument("-p", "--port", dest="port",
#                         help="port of server (default:%(default)s)", type=int, default=5000)
#
#     cmd_args = parser.parse_args()
#     app_options = {"port": cmd_args.port}
#
#     if cmd_args.debug_mode:
#         app_options["debug"] = True
#         app_options["use_debugger"] = False
#         app_options["use_reloader"] = False
#
#     app.run(**app_options)