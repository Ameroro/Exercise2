 # Mutex and Channel basics
 
 ### What is an atomic operation?
-> *Your answer here*
+> An atomic operation a an operation that can simulatniously read a location and write in the same bus operation. This prevents other processor or input/ouput devices from writing or reading until the atomic operation is done. 
+
+Atomic operations must be preformed entirely or not at all. 
+
+In other words, an atomic operation can't be seen as half done by other threads, it has to be completed before other threads proceed. 
+
 
 ### What is a semaphore?
-> *Your answer here*
+>  In concurrent systems with multiple processes, a semaphore is a variable that controls access to common resources. Making sure that only a certain amount of processes have access to the resource.
 
 ### What is a mutex?
-> *Your answer here*
+> A mutex allows us to control what thread has access to the resource. Only processes "holding" the mutex, can use a resource at a given time. 
 
 ### What is the difference between a mutex and a binary semaphore?
-> *Your answer here*
+> The difference between these two is that a mutex is a locking mechanism, which means that a certain task has the ownership of the mutex, and only this task can forwars ownership. The semaphore is a singnal mechanism which means that it signals tasks when they can use the resource, and when they can't.
 
 ### What is a critical section?
-> *Your answer here*
+> Parts of program that access shared resources are called critical sections. Only one precess can execute here. 
 
 ### What is the difference between race conditions and data races?
- > *Your answer here*
+ > Race conditions are basically flaws that happen when the ordering of events affects a program's ability to produce the correct result. This is typicaly due to external timing.
+ 
+ Data race happens when two or more memory accesses that target the same location, are preformed concurrently, and both operations alter the resource. 
 
 ### List some advantages of using message passing over lock-based synchronization primitives.
-> The biggest advantages of massage passing is that it is easier to build for parallell processes, it is also more tolerant of higher latancies than lock based synchronization systems. 
+> 
 
 ### List some advantages of using lock-based synchronization primitives over message passing.
 > Lock based programming makes our pragram more secure, less chance of errors. Easier to find bottlenecks. 
