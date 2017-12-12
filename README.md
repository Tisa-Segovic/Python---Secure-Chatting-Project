# Python-Secure-Chatting-Project
This project is focused on reliable chatting server-clients system, more specifically on implementing the two-dimentional parity algorithm used to provide service of reliable-messaging.

*Inspiration for the Project*:

The project was inspired by Chapter 5 - Error-Correcting Codes: Mistakes That Fix Themselves from the book Nine Algorithms that Changed the Future by MacCormick, 2012 edition. In this chapter, the parity algorithm is described in detail, however, without any implementation, so I decided to implement it.

*How It Works*:

In the chat system, the server is responsible for passing a message from A to B (two chat clients). The server emulates "the noisy location" by flipping bits of the message randomly. Here, the checksum on the client-side is implemented, so that in case if the server is bad, the clients read each other's messages without any problem. Thus, it uses the fact that bits being passed carry enough information to recover what the environment might have corrupted from either or both of the client's messages. 
