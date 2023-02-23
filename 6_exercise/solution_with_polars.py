import polars as pl
from datetime import datetime

def format_date(dt):
  return datetime.strptime(dt, "%a %b %d %H:%M:%S IST %Y").strftime("%Y-%m")
  
def main(input_location, output_location):
    
    lazey_query = (
        pl.scan_csv(input_location).filter(
            pl.col('UserId') != -1 
        ).unique().select(
            pl.col('UserId').cast(pl.Int64, strict=False),
            date_obj = pl.col('TransactionTime').apply(format_date),
            amount = pl.col('NumberOfItemsPurchased') *	pl.col('CostPerItem'),
        )
    )

    # Build aggregation
    aggregated_table    = lazey_query.groupby(["UserId", "date_obj"]).agg(
        pl.col("amount").sum().alias("total_amount")
    ).sort(["UserId","date_obj"])

    # Create all possible combinations of users and months
    month_pool          = [month.strftime("%Y-%m") for month in pl.date_range(datetime(2018, 8, 1), datetime(2028, 6, 1), "1mo")]
    months              = pl.Series(name="date_obj", values=[month_pool])
    all_users           = aggregated_table.select("UserId").unique()
    all_users_month     = all_users.with_columns(months).explode("date_obj")


    # fill missing dates
    aggregated_table_filled_gaps = all_users_month.join(
        aggregated_table, on=["UserId", "date_obj"], how="left"
    ).with_columns([
        pl.col("total_amount").fill_null(0),
        pl.col("date_obj").apply(lambda x: datetime.strptime(x, "%Y-%m"))
    ])

    # Use shift instead of join to calculate future3mo_total_amount
    accounts_with_velocity = aggregated_table_filled_gaps.groupby_rolling(
        "date_obj", by="UserId", period="3mo",offset="-3mo",closed = "left", 
    ).agg([
        pl.col("total_amount").sum().alias("past3mo_total_amount"),
    ]).with_columns([
        pl.col("past3mo_total_amount").shift(-4).over("UserId").alias("future3mo_total_amount")
    ]).fill_null(0.0)
    
    final_results = accounts_with_velocity.select([
        pl.col("UserId"),
        pl.col("date_obj"), 
        pl.when(pl.col("past3mo_total_amount") == 0).then(0).otherwise(
            pl.when(pl.col("past3mo_total_amount") > 4 * pl.col("future3mo_total_amount")).then(1).otherwise(0)
        ).alias("soft_attrition")
    ])
    
    print("Now I start to do the Job!")

    final_results.collect().write_csv(
        output_location, 
        datetime_format="%Y-%m", 
        float_precision = 0)
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='data cleaning and computing soft attrition labels')
    parser.add_argument('--myinput', metavar='path', required=True,
                        help='the path to input')
    
    parser.add_argument('--myoutput', metavar='path', required=True,
                        help='the path to output')
    
    args = parser.parse_args()
    
    main(input_location=args.myinput, output_location=args.myoutput)
