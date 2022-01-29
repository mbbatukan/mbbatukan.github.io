##
using CSV, DataFrames

df_airbnb = DataFrame(CSV.File("airbnb.csv"))

describe(df_airbnb)
