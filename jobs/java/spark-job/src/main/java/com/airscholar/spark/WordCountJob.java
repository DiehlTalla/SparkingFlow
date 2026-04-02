package com.airscholar.spark;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.JavaPairRDD;
import scala.Tuple2;

import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

public class WordCountJob {

    private static final Pattern SPACE = Pattern.compile(" ");

    public static void main(String[] args) {

        SparkConf conf = new SparkConf()
                .setAppName("Word Count Job")
                .setMaster("local");

        JavaSparkContext sc = new JavaSparkContext(conf);

        String text = "hello world hello spark hello docker hello yusuf hello java";

        List<String> data = Arrays.asList(text.split(" "));
        JavaRDD<String> lines = sc.parallelize(data);

        JavaPairRDD<String, Integer> counts = lines
                .flatMap(s -> Arrays.asList(SPACE.split(s)).iterator())
                .mapToPair(word -> new Tuple2<>(word, 1))
                .reduceByKey(Integer::sum);

        List<Tuple2<String, Integer>> output = counts.collect();

        for (Tuple2<String, Integer> tuple : output) {
            System.out.println(tuple._1() + ": " + tuple._2());
        }

        sc.close();
    }
}