## Druid
Druid has several process types, briefly described below:

 - Coordinator processes manage data availability on the cluster.
 - Overlord processes control the assignment of data ingestion workloads.
 - Broker processes handle queries from external clients.
 - Router processes are optional; they route requests to Brokers, Coordinators, and Overlords.
 - Historical processes store queryable data.
 - MiddleManager processes ingest data.

<p align="center">
    <img src="druid-architecture.png" alt="Druid Architecture." />
</p>
