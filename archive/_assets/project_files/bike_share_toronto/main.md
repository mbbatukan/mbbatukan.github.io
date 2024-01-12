@def title = "Projects"

### Bike Share Toronto

#### Dataset visualization (Python)

```python
# python
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

%cd -q "../dataset/data/weather/"
years = ["2017", "2018", "2019", "2020", "2021"]

for year in years:
    files_weather = os.listdir()

    files_weather_selected = []
    for file in files_weather:
        if year in file:
            files_weather_selected.append(file)
    
    df_weather = pd.DataFrame()
    for file in files_weather_selected:
        df_weather = df_weather.append(pd.read_csv(file))

    plt.figure()
    palette = sns.diverging_palette(250, 15, s=100, l=50, n=9, center="light")
    ax = sns.boxplot(x="Month", y="Temp (°C)", data=df_weather, palette=palette)
    ax.grid(linewidth= 0.2)
    ax.set_axisbelow(True)
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", \
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.title(f"Monthly Weather in Toronto ({year})")
    plt.savefig(f"../../../project/weather_{year}.svg", dpi=1200, \
                format="svg", transparent=False, facecolor="white")
```

~~~
<details>
  <summary>Saved figures from Python</summary>
    <p align="center">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2017.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2018.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2019.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2020.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2021.svg">
    </p>
</details>
~~~

#### Dataset visualization (Julia)

```julia
# Julia
home_dir = homedir()

using Pkg; Pkg.activate(home_dir * ".julia/environments/DataFrames")
import DataFrames as DF
using CSV, Gadfly

years = ["2017", "2018", "2019", "2020", "2021"]

folder_weather = home_dir * "/github/BikeShareToronto/dataset/data/weather/"
files_weather = readdir(folder_weather)

for year in years
    files_weather_selected = []
    for file in files_weather
        if occursin(year, file)
            push!(files_weather_selected, file)
        end
    end

    df_all = DF.DataFrame()
    for file in files_weather_selected
        append!(df_all, DF.DataFrame(CSV.File(folder_weather * file));
                cols = :union)
    end

    DF.describe(df_all, :all)
    df_weather = df_all[:, ["Temp (°C)", "Month"]]
    DF.rename!(df_weather, "Temp (°C)" => :temp, "Month" => :month)
    DF.dropmissing!(df_weather)

    df_weather[!,:month] = string.(df_weather[!,:month])
    xticks = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for i in 1:12
        replace!(df_weather.month, string(i) => xticks[i])
    end

    set_default_plot_size(16cm, 9cm)

    p = plot(df_weather,
        x = :month,
        y = :temp,
        color = :month,
        Geom.boxplot,
        Guide.xlabel("Months"),
        Guide.ylabel("Temperature (°C)"),
        Guide.title("Monthly Weather in Toronto ($year)"),
        Guide.xticks(ticks=[0:13;]),
        Guide.colorkey(title = "Months"),
        Scale.y_continuous(format = :plain),
        Theme(background_color = "white")
    )

    img = SVG(home_dir * "/github/BikeShareToronto/project/weather_$(year)_julia.svg",
             16cm, 9cm)
    draw(img, p)
end
```

~~~
<details>
  <summary>Saved figures from Julia</summary>
    <p align="center">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2017_julia.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2018_julia.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2019_julia.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2020_julia.svg">
      <img src="https://raw.githubusercontent.com/mbbatukan/BikeShareToronto/main/project/weather_2021_julia.svg">
    </p>
</details>
~~~

---
<!-- ~~~
<p align="center">
  <i class="fas fa-circle-notch fa-spin fa-5x" style="font-size:250px;color:orange;"></i> 
</p>
~~~ -->