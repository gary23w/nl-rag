---
title: "Database encryption"
source: https://en.wikipedia.org/wiki/Database_encryption
domain: encryption-at-rest
license: CC-BY-SA-4.0
tags: encryption at rest, full disk encryption, data at rest, linux unified key setup, database encryption
fetched: 2026-07-02
---

# Database encryption

**Database encryption** can generally be defined as a process that uses an algorithm to transform data stored in a database into "cipher text" that is incomprehensible without first being decrypted. It can therefore be said that the purpose of database encryption is to protect the data stored in a database from being accessed by individuals with potentially "malicious" intentions. The act of encrypting a database also reduces the incentive for individuals to hack the aforementioned database as "meaningless" encrypted data adds extra steps for hackers to retrieve the data. There are multiple techniques and technologies available for database encryption, the most important of which will be detailed in this article.

## Transparent/External database encryption

Transparent data encryption (often abbreviated as TDE) is used to encrypt an entire database, which therefore involves encrypting "data at rest". Data at rest can generally be defined as "inactive" data that is not currently being edited or pushed across a network. As an example, a text file stored on a computer is "at rest" until it is opened and edited. Data at rest are stored on physical storage media solutions such as tapes or hard disk drives. The act of storing large amounts of sensitive data on physical storage media naturally raises concerns of security and theft. TDE ensures that the data on physical storage media cannot be read by malicious individuals that may have the intention to steal them. Data that cannot be read is worthless, thus reducing the incentive for theft. Perhaps the most important strength that is attributed to TDE is its transparency. Given that TDE encrypts all data it can be said that no applications need to be altered in order for TDE to run correctly. TDE encrypts the entirety of the database as well as backups of the database. The transparent element of TDE has to do with the fact that TDE encrypts on "the page level", which essentially means that data is encrypted when stored and decrypted when it is called into the system's memory. The contents of the database are encrypted using a symmetric key that is often referred to as a "database encryption key".

## Column-level encryption

In order to explain column-level encryption it is important to outline basic database structure. A typical relational database is divided into tables that are divided into columns that each have rows of data. Whilst TDE usually encrypts an entire database, column-level encryption allows for individual columns within a database to be encrypted. It is important to establish that the granularity of column-level encryption causes specific strengths and weaknesses to arise when compared to encrypting an entire database. Firstly, the ability to encrypt individual columns allows for column-level encryption to be significantly more flexible when compared to encryption systems that encrypt an entire database such as TDE. Secondly, it is possible to use an entirely unique and separate encryption key for each column within a database. This effectively increases the difficulty of generating rainbow tables which thus implies that the data stored within each column is less likely to be lost or leaked. The main disadvantage associated with column-level database encryption is speed, or a loss thereof. Encrypting separate columns with different unique keys in the same database can cause database performance to decrease, and additionally also decreases the speed at which the contents of the database can be indexed or searched.

## Field-level encryption

Experimental work is being done on providing database operations (like searching or arithmetical operations) on encrypted fields without the need to decrypt them. Strong encryption is required to be randomized - a different result must be generated each time. This is known as probabilistic encryption. Field-level encryption is weaker than randomized encryption, but it allows users to test for equality without decrypting the data.

## Filesystem-level encryption

### Encrypting File System (EFS)

It is important to note that traditional database encryption techniques normally encrypt and decrypt the contents of a database. Databases are managed by "Database Management Systems" (DBMS) that run on top of an existing operating system (OS). This raises a potential security concern, as an encrypted database may be running on an accessible and potentially vulnerable operating system. EFS can encrypt data that is not part of a database system, which implies that the scope of encryption for EFS is much wider when compared to a system such as TDE that is only capable of encrypting database files. Whilst EFS does widen the scope of encryption, it also decreases database performance and can cause administration issues as system administrators require operating system access to use EFS. Due to the issues concerning performance, EFS is not typically used in databasing applications that require frequent database input and output. In order to offset the performance issues it is often recommended that EFS systems be used in environments with few users.

## Full disk encryption

BitLocker does not have the same performance concerns associated with EFS.

## Symmetric and asymmetric database encryption

### Symmetric database encryption

Symmetric encryption in the context of database encryption involves a private key being applied to data that is stored and called from a database. This private key alters the data in a way that causes it to be unreadable without first being decrypted. Data is encrypted when saved, and decrypted when opened given that the user knows the private key. Thus if the data is to be shared through a database the receiving individual must have a copy of the secret key used by the sender in order to decrypt and view the data. A clear disadvantage related to symmetric encryption is that sensitive data can be leaked if the private key is spread to individuals that should not have access to the data. However, given that only one key is involved in the encryption process it can generally be said that speed is an advantage of symmetric encryption.

### Asymmetric database encryption

Asymmetric encryption expands on symmetric encryption by incorporating two different types of keys into the encryption method: private and public keys. A public key can be accessed by anyone and is unique to one user whereas a private key is a secret key that is unique to and only known by one user. In most scenarios the public key is the encryption key whereas the private key is the decryption key. As an example, if individual A would like to send a message to individual B using asymmetric encryption, he would encrypt the message using Individual B's public key and then send the encrypted version. Individual B would then be able to decrypt the message using his private key. Individual C would not be able to decrypt Individual A's message, as Individual C's private key is not the same as Individual B's private key. Asymmetric encryption is often described as being more secure in comparison to symmetric database encryption given that private keys do not need to be shared as two separate keys handle encryption and decryption processes. For performance reasons, asymmetric encryption is used in Key management rather than to encrypt the data which is usually done with symmetric encryption.

## Key management

The Symmetric & Asymmetric Database Encryption section introduced the concept of public and private keys with basic examples in which users exchange keys. The act of exchanging keys becomes impractical from a logistical point of view, when many different individuals need to communicate with each-other. In database encryption the system handles the storage and exchange of keys. This process is called key management. If encryption keys are not managed and stored properly, highly sensitive data may be leaked. Additionally, if a key management system deletes or loses a key, the information that was encrypted via said key is essentially rendered "lost" as well. The complexity of key management logistics is also a topic that needs to be taken into consideration. As the number of application that a firm uses increases, the number of keys that need to be stored and managed increases as well. Thus it is necessary to establish a way in which keys from all applications can be managed through a single channel, which is also known as enterprise key management. Enterprise Key Management Solutions are sold by a great number of suppliers in the technology industry. These systems essentially provide a centralised key management solution that allows administrators to manage all keys in a system through one hub. Thus it can be said that the introduction of enterprise key management solutions has the potential to lessen the risks associated with key management in the context of database encryption, as well as to reduce the logistical troubles that arise when many individuals attempt to manually share keys.

## Hashing

Hashing is used in database systems as a method to protect sensitive data such as passwords; however it is also used to improve the efficiency of database referencing. Inputted data is manipulated by a hashing algorithm. The hashing algorithm converts the inputted data into a string of fixed length that can then be stored in a database. Hashing systems have two crucially important characteristics that will now be outlined. Firstly, hashes are "unique and repeatable". As an example, running the word "cat" through the same hashing algorithm multiple times will always yield the same hash, however it is extremely difficult to find a word that will return the same hash that "cat" does. Secondly, hashing algorithms are not reversible. To relate this back to the example provided above, it would be nearly impossible to convert the output of the hashing algorithm back to the original input, which was "cat". In the context of database encryption, hashing is often used in password systems. When a user first creates their password it is run through a hashing algorithm and saved as a hash. When the user logs back into the website, the password that they enter is run through the hashing algorithm and is then compared to the stored hash. Given the fact that hashes are unique, if both hashes match then it is said that the user inputted the correct password. One example of a popular hash function is SHA-256.

### Salting

One issue that arises when using hashing for password management in the context of database encryption is the fact that a malicious user could potentially use an Input to Hash table rainbow table for the specific hashing algorithm that the system uses. This would effectively allow the individual to decrypt the hash and thus have access to stored passwords. A solution for this issue is to 'salt' the hash. Salting is the process of encrypting more than just the password in a database. The more information that is added to a string that is to be hashed, the more difficult it becomes to collate rainbow tables. As an example, a system may combine a user's email and password into a single hash. This increase in the complexity of a hash means that it is far more difficult and thus less likely for rainbow tables to be generated. This naturally implies that the threat of sensitive data loss is minimised through salting hashes.

### Pepper

Some systems incorporate a "pepper" in addition to salts in their hashing systems. Pepper systems are controversial, however it is still necessary to explain their use. A pepper is a value that is added to a hashed password that has been salted. This pepper is often unique to one website or service, and it is important to note that the same pepper is usually added to all passwords saved in a database. In theory the inclusion of peppers in password hashing systems has the potential to decrease the risk of rainbow (Input : Hash) tables, given the system-level specificity of peppers, however the real world benefits of pepper implementation are highly disputed.

## Application-level encryption

In application-level encryption, the process of encrypting data is completed by the application that has been used to generate or modify the data that is to be encrypted. Essentially this means that data is encrypted before it is written to the database. This unique approach to encryption allows for the encryption process to be tailored to each user based on the information (such as entitlements or roles) that the application knows about its users.

According to Eugene Pilyankevich, "Application-level encryption is becoming a good practice for systems with increased security requirements, with a general drift toward perimeter-less and more exposed cloud systems".

### Advantages of application-level encryption

One of the most important advantages of application-level encryption is the fact that application-level encryption has the potential to simplify the encryption process used by a company. If an application encrypts the data that it writes/modifies from a database then a secondary encryption tool will not need to be integrated into the system. The second main advantage relates to the overarching theme of theft. Given that data is encrypted before it is written to the server, a hacker would need to have access to the database contents as well as the applications that were used to encrypt and decrypt the contents of the database in order to decrypt sensitive data.

### Disadvantages of application-level encryption

The first important disadvantage of Application-level encryption is that applications used by a firm will need to be modified to encrypt data themselves. This has the potential to consume a significant amount of time and other resources. Given the nature of opportunity cost firms may not believe that application-level encryption is worth the investment. In addition, application-level encryption may have a limiting effect on database performance. If all data on a database is encrypted by a multitude of different applications then it becomes impossible to index or search data on the database. To ground this in reality in the form of a basic example: it would be impossible to construct a glossary in a single language for a book that was written in 30 languages. Lastly the complexity of key management increases, as multiple different applications need to have the authority and access to encrypt data and write it to the database.

## Risks of database encryption

When discussing the topic of database encryption it is imperative to be aware of the risks that are involved in the process. The first set of risks are related to key management. If private keys are not managed in an "isolated system", system administrators with malicious intentions may have the ability to decrypt sensitive data using keys that they have access to. The fundamental principle of keys also gives rise to a potentially devastating risk: if keys are lost then the encrypted data is essentially lost as well, as decryption without keys is almost impossible.

## How can encryption be used to secure data in a database?

Encryption can be employed to enhance the security of data stored in a database by converting the information into an unreadable format using an algorithm. The encrypted data can only be accessed and deciphered with a decryption key, ensuring that even if the database is compromised, the information remains confidential.

By encrypting sensitive data such as passwords, financial records, and personal information, organizations can safeguard their data from unauthorized access and data breaches. This process mitigates the risk of data theft and ensures compliance with data protection regulations.

Implementing encryption in a database involves utilizing encryption technologies such as Advanced Encryption Standard (AES) or Transport Layer Security (TLS). Encryption keys must be securely managed to prevent unauthorized decryption of data.
