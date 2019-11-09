### BlockHack
***
A Blockchain Ledger implementation using python would prevent hackers from rigging the electronic system to manipulate votes. Each vote(Block) is encrypted using sha256 hash, connected subsequently to other blocks, who’s integrity can never be compromised. This system enables a Secure, Reliable and lets private individuals vote from home with biometrics, confirm their votes and who they voted for.
### Why prevent election rigging?
***

Recently there were reports that the US election was rigged.
The fundamentals of Democracy has lost its true value in the modern era of technology.
What if blockchain could make elections fair again.
Blockchain is hack proof due to the millions of users of Blockchain, making it difficult for anyone to
corrupt the network.<br>Each block has a timestamp and a link to the previous block forming a
chronological chain reinforced through cryptography ensuring the records cannot be altered by
others. Due to the transactions needing multiple parties’ authorization before acceptance.
To hack this system requires hackers to take control of all the nodes in the network and would
need the enormous computation power to solve the sha256 hashing mechanism.<br>
### Python implementation 
***

Involves 3 classes message, block and chain.<br><br>
Message class constructor receives the messages, it has functions to hash the message, link
message to the previous one through hash, check whether the message is valid or not.
<br><br>Block class receives block contents like message, prev hash through constructor, it has functions to
validate the message, seal and hash it securely. A complete block with all its data and the
timestamp is created and hashed, which is return to the next block in the chain. This block can be
return in JSON format.<br><br>The Simple Chain class validates the block when creating a chain and also
validates the chain for its integrity by checking if the prev hash and current hash match up for the
chain. A driver function is used to accept candidate name, cast their vote, check for their vote, to
show the blockchain and validate the integrity of the chain.<br><br>
A flask Server implements the block chain through GUI, provides a login where individuals can vote,
check for their vote and verify the integrity of the election.
With the underlying technology it would be impossible to manipulate the votes.
<br><br> Test Username : 1234 Password : 1234

### Technologies Used 
***

Python, flask(Server), HTML5, CSS,JSON.

### Future Implementation
***

* Re-writing the implementation using Solidity(Dapp)
* Adding biometrics support to android app.
