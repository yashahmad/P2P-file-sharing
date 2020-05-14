
# How to create your own decentralized file sharing service using python

**_Abstract_**

_As Q.H. Vu et al in their book Peer-to-peer computing point out “Peer-to-peer (P2P) computing has been hailed as a promising technology that will reconstruct the architecture of distributed computing (or even that of the Internet).” The way peer to peer networks works are they use every node in the network(peer) as a client and a server. In this paper, we discuss how peer to peer networks work, their different architectures, its advantages and disadvantages and finally we try to create our own basic file sharing service using python and socket IO._

# **1 Introduction**

Mostly before 1980’s most of the web was based on a client server model. In 1980s the first peer to peer network was deployed with stand-alone PCs. Though peer to peer networks were developed in early 1980’s they became famous with the advent of Napster. The company that caused a major damage to music industry. Napster allowed users to share music with each other without the use of a central server. (Tyson, J, 2012). Even though Napster was sued and shut, it laid foundation for future technologies that we are all familiar with today. In this paper, we discuss peer to peer network in detail, what is it suitable for and what it is not. What are the security issues concerned with peer to peer networking, its architecture and finally we try to set up our own peer to peer network using Python. We currently live in a world where big giants like Google, Facebook use our data to monetize, this is not what Tim Berners-Lee imagined when he created the world wide web. P2P network is closer to his vision of the world wide web.

# **2 Difference between client server model and peer to peer network**

**2.1 Client-Server Model**

![](https://miro.medium.com/max/975/1*dxOs7C7GOvDhMvI757gTiA.png)

**Fig 2.0 (TechDifference, 2017)**

The web which we are used to these days is mostly based on a client server model. Various protocols that we have studied use a client server model e.g. FTP, SMTP, HTTP. There is a powerful machine(server) which listens to requests in a constant loop from less powerful machines(clients). It is the server that does processing of the request, logic, assembling data and returns the result to the client machine. A client server model can be visualized in Fig 2.0

There are different types of client server architecture.

**2-tier system —** In this kind of a system the client communicates directly with the database server. The client has the code and the business logic. For this kind of architecture to work the client should have access to the database without any intermediary. E.g. a client machine writes a code where it stores data directly into a SQL server. (H.S Oluwatosin, 2014)

**3-tier system —** In this kind of system there are 3 layers. The client which makes the request. The client in this case only contains the presentation code of the logic. Then there is the database server that stores all the data then finally there is a middleware layer between the client and the database server called application server. (H.S Oluwatosin, 2014). The most obvious example of an application layer is Google search where it takes in a request the application does the business logic where it understands what the request is about (indexing) and then sends the request to various servers. This is how it fetches images, web searches, ads, videos at the same time to our query. (Google, 2018)

**2.2 Peer-to-peer**

Contrary to the client server model where the server acts as the center that deals with all the requests. In peer to peer network there is a decentralized model where each node acts as a peer. There is no dedicated server and each peer can act as both a server and a client. Fig 2.1 helps visualize what a peer to peer network looks like.

![](https://miro.medium.com/max/447/1*ATlSk1LnXMSGy0dvrjPORw.png)

**Fig 2.1**

In this form of a network each peer can make request to other peers and at the same time can respond to request from other peers. The performance of such a network increases as the number of peers join the network. These peers can then collaborate and share bandwidth with each other to complete the task at hand. Various peer to peer networks for file sharing have come into existence since the demise of Napster e.g. KaZaA, WinMX and BitTorrent etc. (HKSAR, 2008).

# **3 Peer to Peer network architecture**

In peer to peer networks the data is still transferred through the physical layer but it is at the application layer where peers are able to communicate with each other directly.

**Fig 3.1** shows a tree of how different architecture of peer to peer network are classified.

![](https://miro.medium.com/max/841/1*xiTTfq2hna8jZnOqV1tPjg.png)

**Fig 3.1**

**3.1 Centralized**

In centralized peer to peer systems we can see the properties of both client-server and peer to peer network. Just like a client server model a peer sends a request to the central server to get the list of the peers which have the required resource. Once the peer gets this list it communicates directly with the other peers without the help of the central server. This is how Napster and Berkeley Open Infrastructure for Network Computing (BOINC) work (Q.H. Vu et al). This architecture though has less tolerance compared to other two peer to peer networks but is more scalable. (HKSAR, 2008)

**3.2 Decentralized**

In this architecture, each peer has equal rights and responsibilities. Each peer only sees the partial network and can only offer certain resources. Locating peers that offer the required resources becomes a critical issue in this architecture. Decentralized architecture can further be classified based on network structure and topology. (Q.H. Vu et al). This kind of structure though not being scalable has high fault tolerance (HKSAR, 2008)

**3.2.1 Network Structure**

The network structure in this architecture can be further classified into _flat_ and _hierarchical._  In flat structure the functionality and load is uniformly distributed among peers, whereas in hierarchical structure there are various layers of routing structure. (Q.H. Vu et al)

**3.2.2 Topology**

Decentralized networks can also be classified based on their network topology i.e. wether they are _structured_ or _unstructured_.

In **unstructured** systems, each peer is only responsible for its own resources and contains a list of its neighbors that it may forward the query for additional resources. This leads to a search time worst case of O(n) as the query may have to go through the entire network to find the data.

On the other hand, in **structured** systems data is mapped with its peers in the form of some strategy generally in the form of distributed hash tables (DHT). Very often for security reasons it is not the actual data that is mapped to the peers but only the meta data. This reduces search time for the additional cost of maintain the DHT. (Q.H. Vu et al)

**3.3 Hybrid Peer to Peer Systems**

This system takes advantage of both centralized and decentralized systems where peer nodes that are more powerful that other peers can act as servers thus being called super peers. In this way resource can be located both using decentralized architecture and centralized architecture with super peers acting as servers. (Q.H. Vu et al).

# **4 Advantages and drawbacks of peer to peer network**

Like any other software out there, P2P network has both its advantages and disadvantages. In this section, we discuss the advantages and disadvantages of a P2P network and scenarios where P2P networks actually make sense.

**4.1 Advantages**

The cost related with a peer to peer network is relatively low compared to a client-server network. In a client server network an expensive powerful server needs to be purchased, whereas in the case of peer to peer network a user’s machine acts as a both a server and a client and therefore no additional cost such as technical cost of maintaining the server is not there. (Khan, M, 2014)

Additionally, peer to networks are more fault tolerant. In client-server model if the server fails no communication can take place and neither can transfer of resources. Whereas in a peer to peer network if one peer fails another peer can be used as a server. Additionally, if the number of clients increase the load on the server increases, on the contrary if the number of peers increase in a P2P network the bandwidth is shared among various peers. This can be seen in the case of a BitTorrent file sharing. The larger the number of peers the faster it is to download a file as the same file can be downloaded from various peers.

**4.2 Disadvantages**

P2P network though associated with various advantages comes with various drawbacks also. One of the major disadvantage of a peer to peer network is the security threats which are associated with it. Distribution of virus, TCP port issues and downloading of illegal content are some that we discuss in a further section.

The cost related with peer to peer networks are so low then why are not big companies using this instead of client-server model? There is a reason for that, files and folders cannot be centrally backed up (Tech-ICT, 2003). Since the content is distributed among various machines in a P2P network, backups cannot be created and files cannot be indexed. Since files are distributed over various systems it might be difficult to find a resource on the network. These are few reasons why P2P network is not the industry standard.

# **5 Application of peer to peer network**

Since the days of Napster P2P networks have come a long way. P2P network have now various applications such as instant messaging, file sharing, VOIP and even the finance sector. In this section, we discuss how P2P has affected these areas.

**Instant Messaging —** This was the first area where P2P networks were used. Before P2P networking gopher and IRC servers were used for communication which was not highly effective as it limited the number of people who could be in a chat room and the chat slowed down as the server approached its limits. This changed with P2P networks which allowed sharing of bandwidth and removing the load on a single server leading to faster and more scalable communication. (ReadWrite, 2007).

**File sharing —** Napster showed the potential of P2P for file sharing. File sharing has come a long way since Napster, with protocols such as BitTorrent. BitTorrent worked on the idea of making download as fast as possible and ignoring search, solving the freeloader problem, tit for tat protocol a user has to download and upload simultaneously and quickly distribution the hot content in the network. (Dartmouth, 2015) BitTorrent has become so famous that it resulted in 18.8 % traffic in North America in 2011. (Schonfeld. E, 2011)

**VOIP —** VOIP was a revolution as it allowed people on other ends of the world to get connected easily and Skype was at the fore front of this. Skype used a Hybrid architecture of P2P networks making some peers as the super peers or super hosts. (ReadWrite, 2007). With the help of overlays for connecting various users and having hot standby connections, Skype soon became one of the biggest VOIP channel of communication. (Dartmouth, 2015)

**Finance —** The main reason for the presence of institutions for commerce on internet is they act as trusted third parties to keep a record of the transactions. Satoshi Nakamoto came up with a way to use P2P network to revolutionize the financial sector. Bitcoin was developed so that instead of using banks for trust, a cryptographic proof based model was made. (Nakamoto, 2009). Bitcoin broke down the ledger of transactions into small blocks and distributed it over all the nodes with each block containing a link to the previous and next blog organizing them into a real time-related chain. (D’Aliessi, 2016)

# **6 Security issues in peer to peer network**

We will look at the security issues in peer to peer network with the help of file sharing. Later in this section we suggest some ways a user and a business could protect itself from security threats associated with peer to peer network.

**6.1 Security Threats**

· **TCP port issues —** P2P applications require you to open a large number of ports in the firewall. It is not a good idea to open a large number of ports in the firewall as each open port provides the attacker with a potential avenue to attack the network (HKSAR, 2008).

· **Propagation of malicious code such as viruses —** In a P2P network the user acts as both the client and the server. It is the user that is uploading a file. An attacker can upload a virus which other users download and then upload and which is downloaded by other users. This way a virus can quickly spread across to several machines. Various viruses such as VBS.Gnutella and various Trojan horses are known to spread across various machines.

· **Risk of downloaded content-** It is impossible to tell who the peers are in a p2p network. A user does not who he is downloading the resources from. Other than downloading viruses, a user can accidentally download content which might be illegal and lead the user be exposed to civil or criminal litigation. Untrusted sources should never be trusted.

· **Vulnerability in peer to peer software —** Like any other software peer to peer is also vulnerable to bugs. If an attacker can find a bug in the server side of the code they can exploit the bug and use it to spread viruses or cause denial of service attack. Eg an attacker in 2003 found a bug in P2P software called Kazaa Media Desktop, this could cause a DOD attack.

**6.2 Security measures**

In order to prevent being attacked an organization and users can use appropriate security and prevention measures to protect themselves.

An organization should look into if they actually need a P2P network, and if it is not required unnecessary port ranges (6881–6999 for Bit Torrent) should be blocked across the network. Additionally, P2P network is not the recommended method of sharing sensitive information as the channels are not encrypted and susceptible to being easily sniffed. Additionally, organizations should use IDS/IPS (Intrusion Detection Systems and Intrusion Prevention systems) to constantly monitor the traffic and keep a check on any unauthorized P2P network traffic. At the user level, Anti-Virus software with the latest patches should be installed and personal firewall should be set up to block any ports that are not required. Similarly, a home user should also have the latest version of the anti-virus software and should never download from an untrustworthy source. Pirated software should never be downloaded.

# **7 Setting up your own peer to peer network using python**

In this section, we use python and leverage the help of sockets to create a peer to peer network. We make our module in such a way that when a server disconnects it automatically makes another peer a server. The server side of the program and the client part of the program are in different files but part of the same program. We would first go through our server side of the program, then the client side of the program and then finally discuss how they integrate with each other.

**7.1 Server.py**

We first create a socket and then bind it to a Host and port. The port I use is 5000 and the host is 0.0.0.0 which basically listens to all incoming traffic. We accept the connections to the server and add the list of connections to a list. Then we have a method called the handler method that deals with the uploading of bytes. We run this method in a different thread so that it does not bottleneck the entire program. The client sends a request to receive data called REQUEST_STRING. When the server sees this request, it starts uploading the data. We have to be sure that the data we are uploading is in the format of bytes. We also make sure that when we receive the signal ‘q’ from the peer we know that, that peer is disconnecting from the network. This can be seen on Fig 7.1

![](https://miro.medium.com/max/747/1*IjGUM-4slubuhYm_-pdEBQ.png)

Fig 7.1

Whenever a peer gets connected or disconnected, we broadcast the list of peers to all the peers in thus creating a decentralized architecture. We achieve this with the help of a class called P2P as shown as Fig 7.2

![](https://miro.medium.com/max/838/1*_yBJX4_3avMvXL1h9AeP0g.png)

Fig 7.2

**7.2 Client.py**

This file also first creates a socket and then connects to the peer that is acting as the server. The peer sends a request to the peer acting as the server requesting the file. The server responds to this request and starts uploading the file. The client also starts receiving the bytes on a different thread. The receiving part of the program is shown in Fig 7.3

![](https://miro.medium.com/max/878/1*TsHOyqugsVrg2fi5igwFUQ.png)

Fig 7.3

**Q.) How do we sync the peers and differentiate it from the data being sent as bytes ?**

The way we deal with this problem is every instance of the program has its P2P class as mentioned earlier. The data that contains a list of peers is appended with a byte “\x11’. The client checks on receiving the data that weather it has this byte in front of it use the data to decode the bytes and update the list of peers in that instance of the program. Fig 7.4

![](https://miro.medium.com/max/672/1*7tA2Wj0lEvJGD0ut0N_2Kw.png)

Fig 7.4

Finally, the driver of our program deals with creating a peer as the server and then when the server disconnects it takes care making another peer as the server. This is done by constantly looping over the list of peers and trying to make all the peers clients and then try making itself as the server. So, when that particular instance of the program disconnects another instance tries to become the server. This can be seen in the code in figure 7.5

![](https://miro.medium.com/max/803/1*6w90pm-3eea7oaYTHf0qMw.png)

Fig 7.5

# **Conclusion**

In this paper, we discussed how a peer to peer network works and what are its advantages such as fault tolerance and low cost and disadvantages such as no central backup and time taken to gather the files. We also discuss the security vulnerabilities that are associated with P2P network and finally implemented our P2P network using python. P2P network like any other software is not perfect, but if there were ever to exist a network where giants like Google, Facebook are unable to use our data to monetize from it P2P is the solution.


# **References**

· Tyson, J. (2018). How the Old Napster Worked. [online] HowStuffWorks. Available at: [https://computer.howstuffworks.com/napster2.htm](https://computer.howstuffworks.com/napster2.htm) [Accessed 29 Jun. 2018].

· Oluwatosin, H. (2014). Client-Server Model. IOSR Journal of Computer Engineering, [online] 16(1), pp.67–71. Available at: [https://pdfs.semanticscholar.org/e1d2/133541a5d22d0ee60ee39a0fece970a4ddbf.pdf](https://pdfs.semanticscholar.org/e1d2/133541a5d22d0ee60ee39a0fece970a4ddbf.pdf) [Accessed 30 Jun. 2018].

· Inc, G. (2018). How Google Search works | Useful responses. [online] Google.com. Available at: [https://www.google.com/search/howsearchworks/responses/#?modal_active=none](https://www.google.com/search/howsearchworks/responses/#?modal_active=none) [Accessed 29 Jul. 2018].

· Infosec.gov.hk. (2018). [online] Available at: [https://www.infosec.gov.hk/english/technical/files/peer.pdf](https://www.infosec.gov.hk/english/technical/files/peer.pdf) [Accessed 03 Jul. 2018].

· Boinc.berkeley.edu. (2018). BOINC. [online] Available at: [https://boinc.berkeley.edu/](https://boinc.berkeley.edu/) [Accessed 29 Jul. 2018].

· Vu Q.H., Lupu M., Ooi B.C. (2010) Architecture of Peer-to-Peer Systems. In: Peer-to-Peer Computing. Springer, Berlin, Heidelberg

· Khan, M. (2018). Peer-to-Peer Networks. [online] Getrevising.co.uk. Available at: [https://getrevising.co.uk/grids/peer_to_peer_networks](https://getrevising.co.uk/grids/peer_to_peer_networks) [Accessed 16 Jul. 2018].

· ICT, T. (2018). Teach ICT — GCSE ICT — network topologies, network hardware, hubs, switches, routers, repeaters, bridges, modems, WAP, network cards. [online] Teach-ict.com. Available at: [http://www.teach-ict.com/gcse_new/networks/peer_peer/miniweb/pg5.htm](http://www.teach-ict.com/gcse_new/networks/peer_peer/miniweb/pg5.htm) [Accessed 17 Jul. 2018].

· Neagu, C. (2017). Simple questions: What is P2P (peer-to-peer) and why is it useful? | Digital Citizen. [online] Digital Citizen. Available at: [https://www.digitalcitizen.life/what-is-p2p-peer-to-peer](https://www.digitalcitizen.life/what-is-p2p-peer-to-peer) [Accessed 21 Jul. 2018].

· D’Aliessi, M. (2018). How Does the Blockchain Work? — Michele D’Aliessi — Medium. [online] Medium. Available at: [https://medium.com/@micheledaliessi/how-does-the-blockchain-work-98c8cd01d2ae](https://medium.com/@micheledaliessi/how-does-the-blockchain-work-98c8cd01d2ae) [Accessed 28 Jul. 2018].

· Readwrite.com. (2007). P2P: Introduction and Real World Applications — ReadWrite. [online] Available at: [https://readwrite.com/2007/03/29/p2p_introduction_real_world_applications/](https://readwrite.com/2007/03/29/p2p_introduction_real_world_applications/) [Accessed 25 Jul. 2018].

· Nakamoto, S. (2009). Bitcoin: A Peer-to-Peer Electronic Cash System. [online] Bitcoin.org. Available at: [https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) [Accessed 19 Jul. 2018].

· Schonfeld, E. (2011). Netflix Now The Largest Single Source of Internet Traffic In North America. [online] TechCrunch. Available at: [https://techcrunch.com/2011/05/17/netflix-largest-internet-traffic/](https://techcrunch.com/2011/05/17/netflix-largest-internet-traffic/) [Accessed 30 Jul. 2018].

· Cs.dartmouth.edu. (2015). [online] Available at: [http://www.cs.dartmouth.edu/~campbell/cs60/p2p-examples.pdf](http://www.cs.dartmouth.edu/~campbell/cs60/p2p-examples.pdf) [Accessed 26 Jul. 2018].

· Patentimages.storage.googleapis.com. (n.d.). [online] Available at: [https://patentimages.storage.googleapis.com/88/2f/27/b52fa7dce8a0c4/US7343418.pdf](https://patentimages.storage.googleapis.com/88/2f/27/b52fa7dce8a0c4/US7343418.pdf) [Accessed 30 Jul. 2018].
