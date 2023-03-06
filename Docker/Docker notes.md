[Source](https://www.youtube.com/watch?v=1UHPfDbmZZ4&list=PL0xeHY_ImQVWZMJ-HF3I2GErIeEl4ca2b&index=2)

What is Docker?
	Docker is a container management tool.

What is container?
	Container is a fully independent APP run time environment with their own resources.
	Container is INIT of ONE USER NS, ONE NET NS, ONE ONE PID NS, ONE MOUNT NS powered by kernel with the help of Docker.

What are the components/resources needed for any app to run?

	Hardware (CPU + RAM + Storage)
	OS (on top of Hardware)
			Kernel: A kernel is a compter program at the core of a computer's operating
						 system that has a complete control over everything on computer
						 system.
						 
						 CGROUPS: It is a Linux kernel feature that limits, accounts for, and
						                 and isolates the resource usage of a collection of processes.
					
					         Number of users, Mount and PID needed for an app to run.
							 NEED IT              ALLOWED BY OS            Can actually get it?
					USER      1                  Multiple              Multiple            
					MOUNT     1                  1                     Multiple            
					PID       1                  1                     Multiple            
					NET       1                  1                     Multiple            
			
					Why only 1 MOUNT, PID and NET is allowed by OS?
					Because of concept of Personal Computing.
		
			STORAGE: FILE SYSTEM == MOUNT
				Collection of files/directories for specific purpose.

	Types of file system:
		1. BOOT FILE SYSTEM aka Kernel file system
		2. ROOT FILE SYSTEM 
		3. USER FILE SYSTEM
		4. APP FILE SYSTEM

Evolution of Computing

	Physical Server -> Virtualization -> Containerization

	Difference between Virtual machines and Container:
![alt text](Images/1.png "virtualization vs containerization")






