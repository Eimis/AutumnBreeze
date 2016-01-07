A demo project for http://defintel.com/

**Task description:**

> This goes into our anomaly detection area of tools. This is a basic anomaly detector.We have a dataset that looks like this:

> `location_id,client_id,timestamp`
> `4284,1004,2015-5-5 14:01:22`

> For the test task purposes you can make up a days worth of data with 20 different location IDs at various timestamps. So invent your own data.
we would then require you to organize the data in a way to establish a baseline of location_ids for the day
then introduce a new dataset to compare against the baseline of data you established for day one. Again, just make it up. This time have one location ID that is new and an increase by 20% of another location that was already in day one.
Then you would code a tool in python which highlights the anomalies, when a new location_id or a fluctuation of data (the 20% increase for one location ID) appears in the data as compared to the baseline
so let's say location 400 is present 20 times in day one. Then in day two it is present 24 times. This is anomalous as we established that 20 is what is expected for that particular location.
20% would be an adjustable condition, as would the number of days for a baseline. Ideally you would create a program where the variables can be changed easily
such as a baseline of 7 days versus one day or to look for 40% fluctuations of data versus 20%.

> Not all counts will be 20% more. Have counts of different variations. One or more should meet the 20% anomaly threshold for detection
And also one or more new location IDs in the second set of data. We also need to detect any brand new locations that come up that were not in the previous data set
Another condition is the entry of the non baseline data. In this case it is the second day of data
We should be able to upload a dataset into the database as a file, like a csv
and then we run your tool and it looks for the anomalies as compared to the baseline
and then it outputs the anomalies
make it so we are allowed to upload our own dataset and run the program
it can be all command line. bonus points for any graphical interface but not required
