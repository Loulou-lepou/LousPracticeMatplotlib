""" Comparing the rainfall in 2 cities """
import pandas as pd
import matplotlib.pyplot as plt


url = "https://assets.datacamp.com/production/repositories/3634/datasets/"
seattle_weather = pd.read_csv(url + "6fd451508ecce0d63354fad86704236592eed8ca/seattle_weather.csv")
austin_weather = pd.read_csv(url + "e76b460b41dc7ff286d78246daf3a8c324cb5587/austin_weather.csv")
# climate_data = pd.read_csv(url + "411add3f8570d5adf891127fd64095020210711b/climate_change.csv")

# seattle_weather.info() => seattle_weather["DATE"].dtype = int64 (integer col, not datetimeformat)
# "DATE" => months(1-12) w/o a specific yr
# only display "DATE" as abbreviated month names, w/o changing its actual values

seattle_weather["MONTH"] = pd.to_datetime(seattle_weather["DATE"], format="%m")\
                        .dt.strftime("%b")
austin_weather["MONTH"] = pd.to_datetime(austin_weather["DATE"], format="%m")\
                        .dt.strftime("%b")

# "MONTH" col -> formatted strings -> sorted alphabetically, not in chronological order
# Matplotlib doesn't automatically order month names correctly => messy plot

# soln: convert "MONTH" to a categorical type with an explicit order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# print(austin_weather["MONTH"][:20])
austin_weather["MONTH"] = pd.Categorical(austin_weather["MONTH"],
                                         categories=month_order, ordered=True)

seattle_weather["MONTH"] = pd.Categorical(seattle_weather["MONTH"],
                                          categories=month_order, ordered=True)
seattle_avg = seattle_weather.groupby("MONTH", observed=True)["MLY-PRCP-NORMAL"].mean().reset_index()
# print(austin_weather[["MONTH", "MLY-PRCP-NORMAL"]].head(20))
austin_weather = austin_weather.sort_values("MONTH")

# print(austin_weather[["MONTH", "MLY-PRCP-NORMAL"]].head(20))

plt.cla()
plt.clf()
plt.close("all")

fig, ax = plt.subplots()
ax.plot(seattle_avg["MONTH"], seattle_avg["MLY-PRCP-NORMAL"], 
        marker="o", linestyle="--", label="seattle")
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], 
        marker="v", linestyle="--", label="austin")
ax.legend()
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
ax.set_xticklabels(month_order, rotation=45)  # Rotate x-axis labels for readability
ax.set_title("Weather patterns in Austin and Seattle")
plt.tight_layout()
plt.show()
