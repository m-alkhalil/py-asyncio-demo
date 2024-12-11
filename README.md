asyncio module (https://docs.python.org/3/library/asyncio.html) 
    is a python library used to write a concurrent code!


"time is the most valuable asset"
    Concurrency programming breifly refers to making a program to run multiple tasks at the same time; so time is saved, and resources are utilized effeciently.

The effecient use of the compute resources can be achived by:
    Concurrency: write the program code in a way that tasks can overlap in execution, that will reduce the execution time and keep the
                 resources busy so it's not sitting idle.
    Parallelsim*: generally split tasks to be executed at the same time. * Migh have multiple compute resources  

when writing a code, it can be written to run as synchronous or Asynchronous or both!
    Synchronous: means task execution is sequential as in the order it was recieved so once a task is finished the next task starts.
    Asynchronous: means different tasks can start and finish in overlaping periods of time. 

Both terms take us to the folwoing 2 terms Subroutin and Coroutin.
    Subroutin: is the block of the code which we call when needed and then resume the execution after it finishes execution and it can't be interrupted befor it finishes the execution. we can say it has only one entry point and one exit point
    Coroutin: is the block of the code that can be stopped and then resumes its execution and maintain it's status, it can have multiple entry and exit points and pathways. 

The idea here is, if we have a task that have to wait for a resource, for example IO opration, or database queries Coroutins comes into picture; we can use the wait time to execute another task until the needed resource is avalable for that task to use it! 

Coroutin makes the Asynchronous programming possible, and here where python asyncio librarry comes to surve the goal of writing  asynchronous code using async/await syntax.

async keyword makes a coroutin