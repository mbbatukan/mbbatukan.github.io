@def title = "Projects"

```python
import Pandas as pd

df_airbnb = pd.read_csv("airbnb.csv")
```

```julia
using CSV, DataFrames

df_airbnb = DataFrame(CSV.File("airbnb.csv"))
```

equivalent to head method in pandas `df_airbnb.head(5)` is `first(df_airbnb, 5)` in Julia.

```julia
a = 10
@show a
```
~~~
<pre><code class="plaintext code-output">a = 10</code></pre>
~~~

```julia
using DataFrames
df = DataFrame(A=1:4, B=["M", "F", "F", "M"])
@show df
```

~~~
<pre><code class="plaintext code-output">4×2 DataFrame
 Row │ A      B
     │ Int64  String
─────┼───────────────
   1 │     1  M
   2 │     2  F
   3 │     3  F
   4 │     4  M
</code></pre>
~~~