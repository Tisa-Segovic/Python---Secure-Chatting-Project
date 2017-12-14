# Python-Secure-Chatting-Project
*About the Project - General*

This project is focused on reliable chatting server-clients system, more specifically on implementing the two-dimentional parity algorithm used to provide service of reliable-messaging. The project was done in collaborative work between Tisa Segovic and Ruofan (Brandon) Zhao at New York Univeristy, Shanghai Campus in Fall 2017 Semester. Mentor and consultant for the project was Xianbin Gu, as well as previous work of the students done in Introduction to Computer Science Class.

*Inspiration for the Project*:

The project was particularly inspired by Chapter 5 - Error-Correcting Codes: Mistakes That Fix Themselves from the book Nine Algorithms that Changed the Future by MacCormick, 2012 edition. In the chapter, the parity algorithm is described in detail, however, without any implementation, so we decided to implement it.

*How It Works*:

In the chat system, the server is responsible for passing a message from A to B (two chat clients for example). The server emulates "the noisy location" by flipping bits of the message randomly as it goes along. Here, the checksum on the client-side is implemented, so that in case if the server is bad, the clients read each other's messages without any problem. Thus, it uses the fact that bits being passed carry enough information to recover what the environment might have corrupted from either or both of the client's messages. 

*Outcomes of the Project*

We have sucessfully built the project and finished building it. Some improvements that we could have made are to implement Fletcher's Checksum, instead of implementing the Simple Checksum. By doing this, we would significantly increase the speed of the checksum algorithm, as well as to overall improve the error-detection scheme.

*Note on Collaboration*

Parts of professor's Zheng Zhang's in-class code were used to build the specifically client-side of the project. Pseudocode from the MacCormick's book for building the parity algorithm was used as well. The rest of the code was written by Tisa and Brandon.
