@def title = "Projects"

### Data Wrangling with Julia

Data wrangling is a very important step in machine learning, and raw (scraped/downloaded from the internet) data should be cleaned out before training the models. Pandas is incredibly powerful and well-developed module in Python to analyze and manipulate the data, so I have gained some basic experience in the last few years. However, Julia, high-level programming language, has been increasingly getting popular in data science. While I try to learn syntax of Julia to add to my skill set, I prepared this post to show similarities in between Julia/DataFrames and Python/Pandas. I hope this will encourage people to see how easy to code in Julia.

Recently, there was an online event to learn basics of machine learning (Luckily, I attended). In the first part, data wrangling was explained well in detail using Python/Pandas. Those who are interested in seeing the original repository by Shadi Khalifa and accessing to the source files can refer to [the repository](https://github.com/skhalifa/CAC_S20).

Basically, I repeated what it was done in Python/Julia to gain confidence in Julia/DataFrames. This first block of code is the Python code and following codes are Julia code and output from Julia REPL, respectively. I didn't explicitly show Python output, but it can be found in [Jupyter Notebook](https://github.com/skhalifa/CAC_S20/blob/master/DataPrepHandsOn.ipynb).

There will be no separate reference for each block of code, and well-written documentation of the both modules can be accessed using the links below.

* [Python/Pandas](https://pandas.pydata.org/docs/)
* [Julia/DataFrames](https://dataframes.juliadata.org/stable/)

Since both modules and programming languages are getting updates frequently, some of codes may not properly run in the most recent version. Therefore, I listed the versions that I used to create outputs.

* Python: 3.9.7
   * Pandas (conda): 1.3.5

* Julia: 1.7.1
   * CSV: 0.9.11
   * DataFrames: 1.3.1
   * DataFramesMeta: 0.10.0

If you are new to Julia, you can refer to [Julia documentation](https://docs.julialang.org/en/v1/) and watch [julia for talented ameteurs](https://www.youtube.com/c/juliafortalentedamateurs) channel in YouTube to gain basic knowledge.

First of all, we need to import modules and CSV (data) file.

```python
# Python
import Pandas as pd

df_airbnb = pd.read_csv("airbnb.csv")
```

```julia
# Julia
using CSV, DataFrames

df_airbnb = DataFrame(CSV.File("airbnb.csv"))
```

The first/last 5 rows of the dataframe can be printed with following commands:
* Python: `df_airbnb.head(5)` and `df_airbnb.tail(5)`
* Julia: `first(df_airbnb, 5)` and `last(df_airbnb, 5)`

If you are using [vscode](https://code.visualstudio.com) and [Julia extension](https://code.visualstudio.com/docs/languages/julia) is installed. Dataframe can be visualized by `vscodedisplay(df_airbnb)`.

Let's see how many rows and columns we have in the dataset.

```python
# Python
df_airbnb.shape
```
```julia
# Julia
@show size(df_airbnb)
```
~~~
<pre><code class="plaintext code-output"># Julia REPL output
size(df_airbnb) = (7072, 96)</code></pre>
~~~

Also, `df_airbnb.info()` method and `describe(df_airbnb)` function can be used to get detailed information about dataset in Python/Pandas and Julia/DataFrames, respectively.

There are 96 columns and 7072 rows as you can see from the output. Since not all of these columns is necessary to train model, we select some of the columns from the main dataframe.

```julia
# The same array in Python and Julia
columns_needed = [
   "host_is_superhost",
   "cancellation_policy",
   "instant_bookable",
   "host_total_listings_count",
   "neighbourhood_cleansed",
   "zipcode",
   "latitude",
   "longitude",
   "property_type",
   "room_type",
   "accommodates",
   "bathrooms",
   "bedrooms",
   "beds",
   "bed_type",
   "minimum_nights",
   "number_of_reviews",
   "review_scores_rating",
   "review_scores_accuracy",
   "review_scores_cleanliness",
   "review_scores_checkin",
   "review_scores_communication",
   "review_scores_location",
   "review_scores_value",
   "price"]
```

```python
# Python
df_cleaned = df_airbnb[columns_needed]
```

```julia
# Julia
df_cleaned = df_airbnb[!, columns_needed]
```

To see what type of elements we have in each column, you can use:
* Python: `df_cleaned.dtypes`
* Julia: `[names(df_cleaned) eltype.(eachcol(df_cleaned))]`

~~~
<pre><code class="plaintext code-output"># Julia REPL output
25×2 Matrix{Any}:
 "host_is_superhost"            Union{Missing, String1}
 "cancellation_policy"          Union{Missing, String31}
 "instant_bookable"             Union{Missing, String1}
 "host_total_listings_count"    Union{Missing, Int64}
 "neighbourhood_cleansed"       Union{Missing, String31}
 "zipcode"                      Union{Missing, Int64}
 "latitude"                     Union{Missing, Float64}
 "longitude"                    Union{Missing, Float64}
 "property_type"                Union{Missing, String31}
 "room_type"                    Union{Missing, String15}
 "accommodates"                 Union{Missing, Int64}
 "bathrooms"                    Union{Missing, Float64}
 "bedrooms"                     Union{Missing, Int64}
 "beds"                         Union{Missing, Int64}
 "bed_type"                     Union{Missing, String15}
 "minimum_nights"               Union{Missing, Int64}
 "number_of_reviews"            Union{Missing, Int64}
 "review_scores_rating"         Union{Missing, Int64}
 "review_scores_accuracy"       Union{Missing, Int64}
 "review_scores_cleanliness"    Union{Missing, Int64}
 "review_scores_checkin"        Union{Missing, Int64}
 "review_scores_communication"  Union{Missing, Int64}
 "review_scores_location"       Union{Missing, Int64}
 "review_scores_value"          Union{Missing, Int64}
 "price"                        Union{Missing, String15}
</code></pre>
~~~

As can be seen above, Julia gives you Union type which consists of Missing and other data types (`Int`, `String`, and `Float`) meaning that we have missing data in each column. Also, missing data (`NaN`) can easily be observed with `df_cleaned.info()` method in Python as well.

```python
df_cleaned = df_cleaned.replace({"price": r"[\$,]"}, {"price": ""}, regex=True)
df_cleaned['price'] = df_cleaned["price"].astype("float64")  
```
```julia
df_cleaned.price .= passmissing(x -> replace(x, (r"[\$,]" => ""))).(df_cleaned.price)
df_cleaned.price = passmissing(parse).(Float64, df_cleaned.price)
```

```python
df_cleaned[["host_is_superhost", "host_total_listings_count", "zipcode"]].describe() 
```
~~~
<pre><code class="plaintext code-output"># Python output
host_total_listings_count	zipcode
count	5165.000000	5101.000000
mean	42.044530	94114.965105
std	199.120312	15.394828
min	0.000000	94014.000000
25%	1.000000	94109.000000
50%	2.000000	94114.000000
75%	5.000000	94118.000000
max	1475.000000	94965.000000
</code></pre>
~~~

```julia
describe(df_cleaned[!, ["host_is_superhost", "host_total_listings_count", "zipcode"]])
```
~~~
<pre><code class="plaintext code-output"># Julia REPL output
3×7 DataFrame
 Row │ variable                   mean     min    median   max    nmissing  eltype                  
     │ Symbol                     Union…   Any    Union…   Any    Int64     Union                   
─────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1 │ host_is_superhost                   f               t          1907  Union{Missing, String1}
   2 │ host_total_listings_count  42.0445  0      2.0      1475       1907  Union{Missing, Int64}
   3 │ zipcode                    94115.0  94014  94114.0  94965      1971  Union{Missing, Int64}
</code></pre>
~~~

```python
df_cleaned_NaN_zip = df_cleaned.dropna(subset=["zipcode"])
df_cleaned_NaN_zip.info() 
```

```julia
df_cleaned_NaN_zip = dropmissing(df_cleaned, "zipcode")
[names(df_cleaned_NaN_zip) eltype.(eachcol(df_cleaned_NaN_zip))]
```

```julia
# The same array in Python and Julia
impute_cols = [
  "bedrooms",
  "bathrooms",
  "beds",
  "review_scores_rating",
  "review_scores_accuracy",
  "review_scores_cleanliness",
  "review_scores_checkin",
  "review_scores_communication",
  "review_scores_location",
  "review_scores_value"
]
```

```python
df_imputed = df_cleaned_NaN_zip.fillna(df_cleaned_NaN_zip.median()[impute_cols])
```

~~~
<pre><code class="plaintext code-output"># Python output

host_total_listings_count	zipcode	latitude	longitude	accommodates	bathrooms	bedrooms	beds	minimum_nights	number_of_reviews	review_scores_rating	review_scores_accuracy	review_scores_cleanliness	review_scores_checkin	review_scores_communication	review_scores_location	review_scores_value	price
count	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000	5101.00000	5101.000000	5101.000000	5.101000e+03	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000	5101.000000
mean	37.652421	94114.965105	37.765107	-122.431748	3.215056	1.31435	1.372672	1.768085	1.961955e+04	57.894334	95.616742	9.784552	9.650853	9.885709	9.857283	9.651833	9.458734	208.301510
std	194.230240	15.394828	0.022179	0.026419	1.932137	0.70748	0.922757	1.193006	1.400143e+06	78.761133	6.259013	0.607183	0.699743	0.448607	0.538717	0.673541	0.748405	292.403995
min	0.000000	94014.000000	37.706149	-122.513065	1.000000	0.00000	0.000000	0.000000	1.000000e+00	0.000000	20.000000	2.000000	2.000000	2.000000	2.000000	2.000000	2.000000	0.000000
25%	1.000000	94109.000000	37.750436	-122.443752	2.000000	1.00000	1.000000	1.000000	2.000000e+00	5.000000	95.000000	10.000000	9.000000	10.000000	10.000000	9.000000	9.000000	99.000000
50%	2.000000	94114.000000	37.764713	-122.426608	2.000000	1.00000	1.000000	1.000000	3.000000e+00	26.000000	97.000000	10.000000	10.000000	10.000000	10.000000	10.000000	10.000000	149.000000
75%	4.000000	94118.000000	37.783214	-122.412679	4.000000	1.50000	2.000000	2.000000	3.000000e+01	81.000000	99.000000	10.000000	10.000000	10.000000	10.000000	10.000000	10.000000	233.000000
max	1475.000000	94965.000000	37.810306	-122.370428	16.000000	8.00000	7.000000	14.000000	1.000000e+08	649.000000	100.000000	10.000000	10.000000	10.000000	10.000000	10.000000	10.000000	9000.000000
</code></pre>
~~~

```julia
using Statistics; using Impute

df_imputed = copy(df_cleaned_NaN_zip)
df_imputed[!, impute_cols] = Impute.substitute(df_cleaned_NaN_zip[!, impute_cols], statistic=median)
describe(df_imputed)
disallowmissing!(df_imputed)
```
~~~
<pre><code class="plaintext code-output"># Julia REPL output
25×7 DataFrame
 Row │ variable                     mean      min              median    max               nmissing  eltype                   ⋯
     │ Symbol                       Union…    Any              Union…    Any               Int64     Type                     ⋯
─────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1 │ host_is_superhost                      f                          t                        0  Union{Missing, String1}  ⋯
   2 │ cancellation_policy                    flexible                   super_strict_60          0  Union{Missing, String31}
   3 │ instant_bookable                       f                          t                        0  Union{Missing, String1}
   4 │ host_total_listings_count    37.6524   0                2.0       1475                     0  Union{Missing, Int64}
   5 │ neighbourhood_cleansed                 Bayview                    Western Addition         0  Union{Missing, String31} ⋯
   6 │ zipcode                      94115.0   94014            94114.0   94965                    0  Int64
   7 │ latitude                     37.7651   37.7061          37.7647   37.8103                  0  Union{Missing, Float64}
   8 │ longitude                    -122.432  -122.513         -122.427  -122.37                  0  Union{Missing, Float64}
   9 │ property_type                          Aparthotel                 Villa                    0  Union{Missing, String31} ⋯
  10 │ room_type                              Entire home/apt            Shared room              0  Union{Missing, String15}
  11 │ accommodates                 3.21506   1                2.0       16                       0  Union{Missing, Int64}
  12 │ bathrooms                    1.31435   0.0              1.0       8.0                      0  Union{Missing, Float64}
  13 │ bedrooms                     1.37267   0                1.0       7                        0  Union{Missing, Int64}    ⋯
  14 │ beds                         1.76808   0                1.0       14                       0  Union{Missing, Int64}
  15 │ bed_type                               Airbed                     Real Bed                 0  Union{Missing, String15}
  16 │ minimum_nights               19619.6   1                3.0       100000000                0  Union{Missing, Int64}
  17 │ number_of_reviews            57.8943   0                26.0      649                      0  Union{Missing, Int64}    ⋯
  18 │ review_scores_rating         95.6167   20               97.0      100                      0  Union{Missing, Int64}
  19 │ review_scores_accuracy       9.78455   2                10.0      10                       0  Union{Missing, Int64}
  20 │ review_scores_cleanliness    9.65085   2                10.0      10                       0  Union{Missing, Int64}
  21 │ review_scores_checkin        9.88571   2                10.0      10                       0  Union{Missing, Int64}    ⋯
  22 │ review_scores_communication  9.85728   2                10.0      10                       0  Union{Missing, Int64}
  23 │ review_scores_location       9.65183   2                10.0      10                       0  Union{Missing, Int64}
  24 │ review_scores_value          9.45873   2                10.0      10                       0  Union{Missing, Int64}
  25 │ price                        208.302   0.0              149.0     9000.0                   0  Union{Missing, Float64}  ⋯

</code></pre>
~~~


