# Blockchain Implementation
Since bitcoin boom, everybody is losing their mind, and as a result of that, we have another cool kid in the town, BLOCKCHAIN. This is a simple blockchain implementated in python.

**Block**: A block is a unique record in the blockchain which contains transactions, timestamp, index, hash, etc. broadly 3 types of Blocks :
  - Genesis Block: First Block in the Blockchain.
  - Current Block: Last Block in the Blockchain.
  - Orphan Block: Valid Block which is not part of the main chain. They can occur naturally when two miners produce blocks at similar times or they can be caused by an attacker (with enough hashing power) attempting to reverse transactions.

**Mining**: Method of creating new Block.

**Proof Of Work**: is a number(or data) which is difficult to generate but easy to verify. Usually requires some work and processing time by a computer. Generated number/data will be used to create Block.

**Node**: A server will be treated as a single node in a blockchain network. We can compare and map with the unique HTTP servers.

**Consensus**: Consensus algorithm comes into picture when we have more than one node in our blockchain network. To make sure every node in our network has the same blockchain, we use this algorithm.

## Steps
1. Start your Flask app servers
    - <code>python app.py -p 5000</code>
    - <code>python app.py -p 5001</code>
2. Check what we have in the chain
    - <code>curl "http://127.0.0.1:5000/chain"</code>
3. Create a transaction
    - <code>curl -X POST -H "Content-Type: application/json" -d '{"sender": "addr1", "recipient": "addr2", "amount": 3}' "http://127.0.0.1:5000/create-transaction"</code>
4. Mine a new block
    - <code>curl "http://127.0.0.1:5000/mine"</code>
5. Check the chain
    - <code>curl "http://127.0.0.1:5000/chain"</code>
6. Register another node to the server
    - <code>curl -X POST -H "Content-Type: application/json" -d '{"address": "http://127.0.0.1:5001"}' "http://127.0.0.1:5000/register-node"</code>