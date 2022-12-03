# loadbalancer
Create a Load Balancer from scratch

As stated in our original project proposal: 

1)    Program a server-side load balancer that listens on the port where external clients connect to access services. 

a. We create four Docker containers (each represents a server) and we send requests from the localhost. 


2)    The server must be able to distribute incoming requests over a number of backend servers in the cluster according to a scheduling algorithm.

a. We use Round Robin Scheduling to decide which server to use for each incoming request. Currently, the plan is to use a static counter which resets back to 1 once it sends the first four requests to four different Docker containers. 



3)    The server should also return the result to the original client successfully and should not become a single point of failure. 

a. Successful request: The server displays a message on the browser showing that the request has been routed correctly. 

b. Failing request: Each time a request comes in, we check to see if it has a NULL response. If one server is down, send the request to the next. If all are down, send a message to the client saying that no server is available. 



4)    A side functionality of a load balancer would be that it would prevent the client from directly communicating with the servers which provides additional security to the network. 
