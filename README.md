# 🔭 K8s-Peer-Discovery: Brokerless Kubernetes Networking

Hey there! Welcome to **K8s-Peer-Discovery**. 

When building distributed Python systems in Kubernetes, you often need the different instances (nodes) of your app to talk to each other. Usually, developers add a heavy message broker like Redis, RabbitMQ, or ZooKeeper just to let the nodes know they exist. 

I thought: *Why add extra infrastructure when Kubernetes already knows where everything is?*

This library solves that problem. It uses native Kubernetes Headless Services to let your asyncio Python applications discover each other directly—no brokers required!

## 💡 How It Works (The Sequence)

It's surprisingly simple under the hood. Here is a sequence diagram showing how a new application node finds its friends using just standard DNS:

```mermaid
sequenceDiagram
    %% Friendly styling
    autonumber
    
    participant Node1 as 🐍 App Node 1
    participant DNS as 🌐 K8s Core DNS
    participant Node2 as 🐍 App Node 2
    
    Note over Node1,DNS: Node 1 boots up and needs to find peers
    Node1->>DNS: "Hey DNS, who else is in the 'my-app' cluster?"
    DNS-->>Node1: "I found IPs: 10.0.1.5, 10.0.1.6"
    
    Note over Node1: Node 1 updates its internal peer list
    
    Node1->>Node2: "Hi Node 2! Let's sync data directly."
    Node2-->>Node1: "Hello Node 1! Syncing now."
```

## ✨ Key Benefits

- **Zero Extra Infrastructure**: You don't have to manage or pay for a Redis/Zookeeper cluster.
- **Pythonic & Modern**: Built specifically for modern `asyncio` workflows.
- **Event-Driven**: You can easily hook into events (e.g., trigger a function when a new node joins or leaves).

Whether you're building a chat server, a multiplayer game backend, or a distributed cache, this library keeps your deployment extremely lean.
