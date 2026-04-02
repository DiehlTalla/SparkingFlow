from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWorldCount").getOrCreate()

text = "hello spark Hello Python Hello Docker and  Hello Deffo"

words = spark.sparkContext.parallelize(text.split(" "))

wordsCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for wc in wordsCounts.collect():
    print(wc[0], wc[1])
    spark.stop()
