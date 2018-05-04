from uuid import uuid4

import requests
from flask import Flask, jsonify, url_for, request

from blockchain import BlockChain


app = Flask(__name__)

blockchain = BlockChain()

node_address = uuid4().hex  # Unique address for current node

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-p', '--port', default=5000, type=int)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=True)