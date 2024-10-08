from pyspark.sql import SparkSession
from pyspark import SparkConf

# set shuffle partitions to 5
conf = (
    SparkConf()
    .setAppName("streaming application")
    .setMaster("local[*]")
    .set("spark.sql.shuffle.partitions", "3")
    .set("spark.streaming.stopGracefullyOnShutdown", "true")
    .set(
        "spark.sql.streaming.schemaInference", "true"
    )  # for json we have to infer the schema
)
# streaming stop gracefully on shutdown means that if we stop the streaming application it will stop gracefully
spark = SparkSession.builder.config(conf=conf).getOrCreate()
# set logger to error level only
spark.sparkContext.setLogLevel("ERROR")

# 1 read from the stream
ordersdf = (
    spark.readStream.format("json")
    .option("path", "input_files/streaming_files/")
    .load()
)
# 2 process all the orders that are completed
ordersdf.createOrReplaceTempView("orders")
completed_orders = spark.sql(
    "select count(*) from orders where order_status='COMPLETE'"
)


# 2 write it back to the sink
orders_query = (
    completed_orders.writeStream.format("console")
    .outputMode("complete")
    .option("path", "output_files/streaming_files/")
    .option("checkpointLocation", "checkpoint-location")
    .trigger(processingTime="15 seconds")
    .start()
)

orders_query.awaitTermination()
# means do not terminate the program until we terminate this

# open a terminal and run the following command
# nc -lk 12345
# type some text and see the output in the console
# to stop the program press ctrl+c

# we have other options also
# 1-in read stream we have options like maxFilesPerTrigger
# go to next file to see it
# checkpoint directory keeps a track of running total in state file
# it keeps a track of what all it has read in souce file

# Fault tolerance and exactly once processing
Ideally a spark streaming application can run forever
1-Exception
2-Maintaince activities
our application should be able to stop and restart gracefully

this means to maintain exactly once semantics
    do not miss any input records
    moreover do not create duplicate output records

spark structured streaming provides ample support for this
it maitains the state of the micro batch in the checkpoint location

checkpoint location helps us to achieve fault tolerance

checkpoint locaton mainly contains 2 things
 1- it contains the read positions example which all files are processed
 2- it keeps track of state information example running total

spark structred streaming all information it requires to restart the unfinised microbatch so that fault tolearance will be there

To gauarnetee exactlt once processing 4 reqirement should be met
 1-restart application with same checkpoint location
        lets say in 3rd microbatch we got an exception in checkpoint location in the commits we have got 2 commits
        since 3rd once failed 3rd commits we will not see
        so it know it has to start from 3rd microbatch

 2- use a replayable source
        consider in 3rd microbatch we got some error
        consider 100 records in 3rd microbatch
        after processing 30 records it gave records
        next time when we restart the application it should be able to read the same 30 records again
        so that it can process the remaining 70 records
        replayable means we can get the same data which we have processed agan
        when we are using socket source we cannot get older data
        so socket source is not replayable
        kafka source and s3 source are replayable

 3- use deterministic computation
        lets say 3rd microbatch has 100 records and consider while processing 30th records we got an error
        now whenver we start the application again it will start from the begining of 3rd microbatch
        these 30 records are also processed again
        so the output should remain same

 4- use an idempotent sink
        lets say 3rd microbatch has 100 records and consider while processing 30th records we got an error
        now whenver we start the application again it will start from the begining of 3rd microbatch
        these 30 records are also processed again
        dont you feel we are processing these 30 records 2 times so we will be writing to sink(output) 2 times
        2nd time when you are writing the same output it should not impact us
        either it should discard the 2nd output or it should override the first output with the second one

Stateful vs stateless transformations
======================================

stateless
    select
    filter
    map
    flatmap
    explode
t   hese transformation only works with the current microbatch and that we dont have to maintain any state

stateful
    last state is maintained in a state store
    grouping and aggreagation cannot work without history
    these kind of transformation rely on state information or history

Note:
when we talk about stateless transformation do not support complete output mode
for example
map,select
1000 input --->1000 output
can we store this in state store?No its not efficient so in stateless transformation we cannot define a complete mode
remebring the state of the query is not efficient as we have too much data to cater
it will fail

when we are using stateful transformation we are storing the state or history in state store
excessing state can cause out of memory error
state store is stored in memory of the executor.if it keeps on growing it will cause out of memory error
but we saw a folder that is created checkpoint directory is created to have state information
it maintains position of file and state
ideally it wil be stored in s3 or hdfs
that why are we talking out oo memory error
checkpoint and state information is stored in checkpoint directory to handle fault tolerance
but when we are executing something and want to read history it does not come to checkpoint files and check that is why
the same information state info present in this file is maintained in executor memory for quick lookups

we should be careful when we deal with stateful operations
becuase if history or state keeps on growing it can lead of out of memory error

spark offers us 2 kinds of stateful operations
1-managed stateful operations
    spark manages how to clean up state store.remember state store is in exector memory
2-unmanaged stateful operations
    where we as a developer decide on when to cleanup the state store
    we write our custom cleanup logics
    present in scala/java but not in python

Aggregations are 2 types
==============================
1- continous aggregations
    consider you purchased your grocey from big bajar
    on purchase of 100 rs we get one 1 reward point
    consider these reward point never expire
    it will keep on adding like unbounded
    now lets say 100 million customer and every month we are getting 1 million new customers
    so the data is unbounded
    so state store(history) will keep on growing
    spark will not be able to cleanup.
    in such cases there we have unbounded we can think of unmanaged stateful operations to do the cleanup
    we can write our custom cleanup logics
2- time bound aggregations also called window based aggregations
    consider we have a 1 month window and the reward points expire after 1 month
    so in this case we can go with managed stateful operations
    spark can help us to clean the state store
    any data before 1 month can be cleanup
    managed stateful operations spark will work on cleanup logic
    spark can clear the state for previous month and start again

for all the time bound aggregations we can go with managed stateful operations


There are 2 types of windows
    1-Tumbling time window
        a series of fixed-size, non-overlapping, contiguous time intervals
        each window will be of fixed size
        tumbling window of 15 mins
        10-10.15
        10.15-10.30
        10.30-10.45
        10.45-11
        if i say 10.14 its not overlapped

    2-sliding time window
        a series of fixed-size, overlapping, contiguous time intervals
        we can have a sliding winodw of 15 mins where it slides every 5 mins
        10-10.15
        10.05-10.20
        10.10-10.25
        10.15-10.30
        window size is 15 mins and the sliding interval is 5 mins

Aggregations windows are based on event time and not on trigger TimeoutError
consider big bazaar
{"order_id":57012,"order_date":"2021-06-01T10:00:00","order_status":"PROCESSING","amount":200}
event_time = order_date = 2021-06-01T10:00:00
this event might reach spark at 10.10
but we always deal with event_time
event time will be earlier
consider these type of transcation happening in big bazaar
find total amount of sales every 15 mins
we can go with a tumbling window of 15 mins
11.00-11.15 [event time] -window 1
11.15-11.30 [event time] -window 2
11.30-11.45 [event time] -window 3
11.45-12.00 [event time] -window 4
lets say event time is 11.14 (order was placed at 11.14) but this order late to spark at 11.20(lets say)
than what will happen to late records
go to 6_streaming.py






