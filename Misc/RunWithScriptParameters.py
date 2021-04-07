#!/usr/bin/python
# -*- coding: utf-8 -*-

# 运行带默认参数的脚本
# Run->Edit configurations Or 选中文件,点击Create ....

def print_num(number):
    pass

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-n", "--n", dest="number",
                        help="number for print",type=int, default=1)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)


    cmd_args = parser.parse_args()
    print(cmd_args.number)
