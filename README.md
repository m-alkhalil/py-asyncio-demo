asyncio module (https://docs.python.org/3/library/asyncio.html) 
    is a python library used to write a concurrent code!

    
** [[[asyncio will be used in the comprehensive python API application]]]

"time is the most valuable asset"
    Concurrency programming briefly refers to making a program to run multiple tasks at the same time; so time is saved, and resources are utilized efficiently.

The efficient use of the compute resources can be achieved by:
    Concurrency: write the program code in a way that tasks can overlap in execution, that will reduce the execution time and keep the
                 resources busy so it's not sitting idle.
    Parallelism*: generally split tasks to be executed at the same time. * Might have multiple compute resources  

when writing a code, it can be written to run as Synchronous or Asynchronous or mixture of both!
    Synchronous: means task execution is sequential as in the order it was received so once a task is finished the next task starts.
    Asynchronous: means different tasks can start and finish in overlapping periods of time. 

Both terms take us to the following 2 terms Subroutine and Coroutine.
    Subroutine: is the block of the code which we call when needed and then resume the execution after it finishes execution and it can't be interrupted before it finishes the execution. we can say it has only one entry point and one exit point
    Coroutine: is the block of the code that can be stopped and then resumes its execution and maintain it's status, it can have multiple entry and exit points and pathways. 

The idea here is, if we have a task that have to wait for a resource, for example IO operation, or database queries Coroutines comes into picture; we can use the wait time to execute another task until the needed resource is available for that task to use it! 

Coroutine makes the Asynchronous programming possible, and here where python asyncio library comes to serve the goal of writing  asynchronous code using async/await syntax.

async keyword makes a coroutine
