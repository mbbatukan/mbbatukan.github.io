@def title = "Projects"

### Data Wrangling with Julia

Data wrangling is a very important step in machine learning, and raw (scraped/downloaded from the internet) data should be cleaned out before training the models. Pandas is incredibly powerful and well-developed module in Python to analyze and manipulate the data, so I have gained some basic experience in the last few years. However, Julia, high-level programming language, has been increasingly getting popular in data science. While I try to learn syntax of Julia to add to my skill set, I prepared this post to show similarities in between Julia/DataFrames and Python/Pandas. I hope this will encourage people to see how easy to code in Julia.

Recently, there was an online event to learn basics of machine learning (Luckily, I attended). In the first part, data wrangling explained well in detail using Python/Pandas. Those who are interested in seeing the original repository by Shadi Khalifa and accessing to the source files can refer to [the repository](https://github.com/skhalifa/CAC_S20).

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

The first 5 rows of the dataframe can be seen with following commands:
* Python: `df_airbnb.head(5)`
* Julia: `first(df_airbnb, 5)`

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

There are 96 columns as you can see from the output. Since, not all of these columns is necessary to train model. We have to get rid of some of the columns.

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
* Julia: `eltype.(eachcol(df_cleaned))`

~~~
<pre><code class="plaintext code-output"># Julia REPL output
25-element Vector{Union}:
 Union{Missing, String1}
 Union{Missing, String31}
 Union{Missing, String1}
 Union{Missing, Int64}
 Union{Missing, String31}
 Union{Missing, Int64}
 Union{Missing, Float64}
 Union{Missing, Float64}
 Union{Missing, String31}
 Union{Missing, String15}
 Union{Missing, Int64}
 Union{Missing, Float64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, String15}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, Int64}
 Union{Missing, String15}
</code></pre>
~~~

As can be seen above, Julia gives you Union type which consist of Missing and other data types (Int or String) meaning that we have missing data in each column. Missing data can easily be observed with `df_cleaned.info()` method in Python as well.