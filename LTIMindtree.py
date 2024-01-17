from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import abs, avg


class FaultyVehiclesDetection:

    def init_spark_session(self) -> SparkSession:
        spark = SparkSession.builder.appName("Faulty Vehicles Detection").master("local").getOrCreate()
        return spark

    def read_csv(self, input_path: str) -> DataFrame:
        spark = self.init_spark_session()
        schema = "vehicleld INT, fuelEfficiency FLOAT"
        df = spark.read.schema(schema).option("header", True).csv(input_path)
        return df

    def calc_average_efficiency(self, observed: DataFrame) -> DataFrame:
        df = observed.groupBy("vehicleld").agg(avg("fuelEfficiency").alias("averageFuelEfficiency"))
        return df

    def find_faulty_vehicles(self, avg_observed: DataFrame, required: DataFrame) -> DataFrame:
        df = avg_observed.join(required, "vehicleld")
        df = df.withColumn("diff", abs(df.averageFuelEfficiency - df.fuelEfficiency))
        df = df.filter(df["diff"] >= 5)
        df = df.select("vehicleld", "averageFuelEfficiency")
        df = df.withColumnRenamed("averageFuelEfficiency", "fuelEfficiency")
        return df

    def save_as(self, data: DataFrame, output_path: str) -> None:
        data.write.option("header", False).csv(output_path)
