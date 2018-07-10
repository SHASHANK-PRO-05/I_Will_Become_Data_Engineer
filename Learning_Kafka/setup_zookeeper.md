### How to setup zookeeper cluster
Setting up a zookeeper cluster is super easy but has some caveats. 
When I did this the version I was using was 3.4 and I used zookeeper provided with Kafka. My kafka version was 1.1 and scala version of kafka was 2.11.X. 

I am going to setup 3 nodes. Java should already be installed. This will be specific to ubuntu. 

1. Go to the kafka folder; already extracted.
1. Open config/zookeeper.properties and change it to the following
    ```
        syncLimit=5
        initLimit=20 
        tickTime=2000 #2 seconds heartbeat
        dataDir=/var/lib/zookeeper
        clientPort=2181
        server.1=hostname1:2888:3888
        server.2=hostname2:2888:3888
        server.3=hostname3:2888:3888
    ``` 
    same config in all three nodes.
1.  Enable port 2181, 2888, and 3888 on all the nodes. I am using 
    ```
        sudo ufw allow <port no>
    ```
    on cloud you can enable this from security group. 
1. Make the data dir as mentioned in the config and in that make a file called `myid`. This file will have the server id given to that node in config. 
1. Run `./bin/zookeeper-server-start.sh config/zookeeper.properties` on every node. 