# PL P2P

## Description
The p2p trading has two problems in regards to scalability, the fairness algorithm and the amount of transactions it produces.

* Fairness algorithm: Seems highly solvable with many possible solutions as presented in the repo, matmul is extremely scalable and at first glance the algorithm can potentially be made stateless allowing for distributed computation or to be run on GPU.

* Blockchain transactions: The amount of transactions the algorithm above produces can be quite high and thereforce not very blockchain friendly. I think a potential solution to this problem is to not see the output as transactions but as data.
For example 1000 producers trading with 1000 consumers would produce 1000000 transactions, unfeasible for any blockchain.
But thinking about data only, 1000000 transactions * 4 Bytes (float32) = 4MB, which is nothing for todays hard drive capabilities.
With this approach the issue turns from a technological problem (support millions of tps) into a cost problem (cost of storing 4MB on the blockchain), therefore doable today, using a permissioned blockchain the cost is irrelevant. Furthermore data can be compressed as transactions not so much.

## P2P_NP
Simple algorithm using numpy, pretty fast, can handle more than 1M producers and 1M consumers.