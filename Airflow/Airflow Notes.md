Lets say A developer wants to run a piece of code on schedule basis, ways to do it:

	- Cron jobs:   Cron is a utility program that lets users input commands for scheduling
	                          tasks repeatedly at a specific time. Tasks scheduled in cron are
	                          called cron jobs.  
	- Python/bash script

But let's say we have to run multiple cron jobs to monitor, there are various challenges faced:

	1. Monitoring: job status, view historic runs/durations
	2. Manage Failures: alerts on failures , retries and timeouts
	3. Dependies: Check Upstream data, run job1 and job2
	4. Backfills: Rerun historic data ingestions
	5. Scalability: No centralized entity to manage jobs
	6. Deployments: version control orchestration systems

Airflow-Core Components

	1. Scheduler: Trigger schedules workflows and submit tasks to executor to run
	2. Executor: Handles running task
	3. Worker: Run the actual task
	4. Webserver: User interface to inspect, trigger and debug DAGs and tasks behaviour
	5. Metadata database: Stores information about DAGs and tasks states
	6. DAGs folder: Directory where all DAGs code is persisted, read by scheduler and 
		executor
	7. Logs Directory: A location where airflow store logs of all finished tasks.

![image][Images/1.png]

	1. A user first logins to the webserver interface to view and control workflows.
	2. Webserver then retrieves all dags from dags directory as well as pull information 
	     from metadata database about dag states.
	3. When a DAG gets triggered (whether automatically on its scheduled time or manually 
	     by user via webserver), a scheduler then submits the DAG tasks to executor. An 
	     Executor then submits these tasks to workers.
	4. A single worker takes care of one task at a time. For this, a worker fetches DAG code 
	    from dags directory and runs
	5. Upon tasks completion, executor retrieves tasks state from worker and updates into 
	     metadata database.
	6. Finally, executors fetches tasks logs from workers and persists them into logs 
	     directory, to be viewable from UI dashboard.

## Executors Architecture

As discussed earlier, executor define a mechanism by which tasks get run. Airflow come with different type of executors. Lets look at the the high-level architecture of most famous airflow executors

### Sequential Executor

![image][Images/2.png]
The simplest executor that is preconfigured as default with airflow. This executor runs the task within the same machine where scheduler is running as a new python sub-process.  As the name says, this executor runs only one task instance at a time. because of its sequential nature, its the only executor what can run on SQLite database  because this database supports only one connection at a time. Using any other database with this executor will be an overkill.

**Pros**

-   **No Setup Required**: comes as default executor preconfigured with airflow
-   **Light Weight**: no extra nodes required, all tasks run on scheduler node
-   **Cheap**: due to its light weight

**Cons**

-   **Slow**: runs one task at a time
-   **Not Scalable**: because tasks run on same node where scheduler is running
-   **Single point of failure**: Tasks fail if scheduler node dies
-   **Not Suitable for production:** Because of all above


### Local Executor

![image][Images/3.png]
Local Executor is exactly the same as the sequential executor with the only difference being here is it can manage multiple task instances at a time by running multiple sub-processes within the same scheduler node. Because of its this nature, one can use any database other than SQLite for metadata storage. The two ideal ones are MySQL and PostgreSQL.

**Pros:**

-   **Easy to Setup**: simply set environment variable [_AIRFLOW__CORE__EXECUTOR=LocalExecutor_](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#executor)
-   **Cheap & Light Weight**: Task instances run on same machine where scheduler is running, so no extra resources required
-   **Fast**: Can run multiple tasks at a time

**Cons:**

-   **Single point of failure**: Tasks fail if scheduler node dies
-   **Not suitable to scale**: limited to scheduler node resources
-   **Not suitable for production**: because of all above


### Celery Executor

![image][Images/4.png]
Celery executor unlike sequential and local executor runs the task on a dedicated machine. As the name says, it uses [Celery](https://docs.celeryproject.org/en/stable/) distributed tasks queuing mechanism to perform tasks across fixed pool of workers. Airflow Scheduler adds the tasks into a queue and Celery broker then delivers them to the next available Celery worker, to be executed.

By default, a single Celery worker can run upto 16 tasks in parallel. You can limit this by setting environment variable _AIRFLOW__CELERY__WORKER_CONCURRENCY_.  Note that the worker concurrency has upper-limit to dag_concurrency (number of task instances a scheduler is able to schedule at once _per DAG_).

**Pros:**

-   **Horizontally scalable**: Set as many number of workers as required
-   **Fault tolerant**: If a worker goes down, celery executor automatically assigns a task(s) to another healthy worker
-   **Production ready**: due to all above

**Cons:**

-   **Relatively Complex setup**: Additional resource setup required RabbbitMQ broker and workers
-   **Resource wastage if no task scheduled**: Celery workers always running even if the task queue is empty
-   **Not cost effective**: its pricier because of additional resources plus due to resource wastage.

### **Kubernetes Executor**

![image][Images/5.png]
Kubernetes executer leverages the power of Kubernetes for resource management and optimization. It runs the tasks on a dedicated pod. A pod, in Kubernetes world, refers to a dedicated machine capable of running one or more container. This executor uses the Kubernetes API to dynamically launch pod for scheduled task, and monitors its state until it finishes. The task state and logs are then reported back to scheduler, stored in metadata database and made visible to view over the UI dashboard. Each pod can be assigned with different memory allocation according to the task requirements.

**Pros:**

-   **Can Scale down to zero**:  If no task(s) is scheduled, no worker pod will spin-up, whereas it can scale up to as many pods as required. So no resource wastage.
-   **Fault tolerant**: Pods are re-spawned upon non-success termination
-   **Flexible resource allocation**: Each task can individually be assigned its memory allocation, airflow image as well as service account.
-   **Cost & resource effective**: Won’t be charged extra if no tasks(s) is scheduled

**Cons:**

-   **Pod launch time**: A new worker pod spins-up upon new tasks execution. This adds few seconds of latency in workflow.
-   **Complex setup**: Requires kubernetes knowledge, setting up cluster and executor configurations on top


