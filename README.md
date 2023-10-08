# BertGeo: An Accurate, Scalable, and Fast IP Geolocation System
IP geolocation is essential for various location-aware Internet applications spanning from targeted online advertising to cybercrime traceability. However, previous IP geolocation works are hampered by limited geolocation accuracy, poor region scalability, and bad real-time performance. In this paper, we propose a novel IP geolocation system, BertGeo, which innovatively constructs a global large-scale graph model for geospatial and cyberspace geolocation information to solve the scalability bottleneck and utilizes a pre-trained large language model, Bert, for IP geolocation for the first time to address the real-time performance challenge. The real-world experiments show that BertGeo enables accurate, highly scalable, and real-time IP geolocation. BertGeo achieves an average geolocation error of 21.87km globally, improving by 70% compared to state-of-the-art technologies. Specifically, it can achieve an average error of 1km in dominant regions and 50km even in the worst performance regions, which is an improvement of over 400% compared to other methods. Furthermore, the average time for real-time geolocation of target IPs is sub-minute, 12x shorter than other methods, which can be used for online IP geolocation services. Ultimately, we develop BertGeo to achieve accurate, real-time geolocation of 3.7 billion IPv4 addresses and 1.2 billion IPv6 addresses. 

## Introduction
To make it easier for readers to reproduce our research, we make the source code, test data, and graph datasets of BertGeo publically available. Please cite our paper if you use the BertGeo code and dataset, thank you! 

Our project mainly consists of three parts: GeoNetGraph, GraphBert and GeolocationService. 

## Misc
### Ethical and Privacy Concerns
All code and data we publish has been desensitized and does not involve user privacy. Please cite our paper when using. 

### Future work
We are actively deploying the distributed BertGeo IP geolocation system and are constantly updating our datasets and services. If you would like to join us, please send us emails. 