#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import os


# Download or create a CSV file called sales_data.csv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "owid-covid-data.csv")

#Load the CSV file using pandas.
covid_data = pd.read_csv(file_path)


# Display the first few rows of the DataFrame
print(covid_data.head())
# Display the columns of the DataFrame
print(covid_data.columns)

#Key columns:
#date, location, total_cases, total_deaths, new_cases, new_deaths, total_vaccinations, etc.

#Identify missing values:
covid_data.isnull().sum()

# Filter countries of interest (e.g., Kenya, USA, India).
countries_of_interest = [
    'Kenya', 'Zimbabwe', 'Botswana', 'South Africa', 'Mozambique', 'Zambia', 'Tanzania', 'Uganda',
    'Rwanda', 'Burundi', 'South Sudan', 'Ethiopia', 'Somalia', 'Sudan', 'Central African Republic',
    'Cameroon', 'Nigeria', 'Ghana', 'Senegal', 'Mali'
]
filtered_data = covid_data[covid_data['location'].isin(countries_of_interest)].copy()

# Display the filtered data
print(filtered_data.head())

# Drop rows with missing dates or critical values in 'date', 'total_cases', and 'total_deaths'.
critical_columns = ['date', 'location', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
filtered_data = filtered_data.dropna(subset=[col for col in critical_columns if col in filtered_data.columns]).copy()

# Convert the 'date' column to datetime format
if 'date' in filtered_data.columns:
    filtered_data['date'] = pd.to_datetime(filtered_data['date'])

# Handle missing numeric values in critical columns by filling with the mean
numeric_columns = [col for col in ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations'] if col in filtered_data.columns]
filtered_data[numeric_columns] = filtered_data[numeric_columns].fillna(filtered_data[numeric_columns].mean())


#Goal: Generate descriptive statistics & explore trends.

# Plot total cases over time for selected countries.
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
	country_data = filtered_data[filtered_data['location'] == country]
	plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total Cases Over Time for Selected Countries')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.show()


# Plot total deaths over time.
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

plt.title('Total Deaths Over Time for Selected Countries')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.show()

# Compare daily new cases between countries by plotting the daily new cases for each country
# TODO: Implement a plot to visualize daily new cases for each country to compare trends over time.
# to visualize the differences and trends over time.
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Daily New COVID-19 Cases for Selected Countries')
plt.xlabel('Date')
plt.ylabel('Daily New Cases')
#Calculate the death rate: total_deaths / total_cases.
if 'total_deaths' in filtered_data.columns and 'total_cases' in filtered_data.columns:
    filtered_data['death_rate'] = filtered_data['total_deaths'] / filtered_data['total_cases']
else:
    filtered_data['death_rate'] = None
plt.tight_layout()
plt.show()

#Calculate the death rate: total_deaths / total_cases.
filtered_data['death_rate'] = filtered_data['total_deaths'] / filtered_data['total_cases']

# Display average death rate for each country
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    avg_death_rate = country_data['death_rate'].mean()
    print(f"Average death rate for {country}: {avg_death_rate:.4f}")

# Bar chart: Top 10 countries by total cases (latest date in data)
latest_date = filtered_data['date'].max()
latest_data = filtered_data[filtered_data['date'] == latest_date]
top_countries = latest_data.sort_values('total_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_countries['location'], top_countries['total_cases'], color='skyblue')
plt.title('Top 10 Countries by Total COVID-19 Cases (Latest Date)')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot cumulative vaccinations over time for selected countries.
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    # Some countries may have missing vaccination data, so fillna(0) for plotting
    plt.plot(country_data['date'], country_data['total_vaccinations'].fillna(0), label=country)

plt.title('Cumulative COVID-19 Vaccinations Over Time for Selected Countries')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

'''
    Visualize cases or vaccination rates by country on a world map.

    ✅ Tools:

    Plotly Express
'''
import plotly.express as px

# Get the latest data for each country
world_latest = covid_data.sort_values('date').groupby('location').tail(1)

# Remove aggregate rows (like 'World', 'Africa', etc.) if present
# You can adjust this list as needed
aggregates = ['World', 'Africa', 'Asia', 'Europe', 'European Union', 'North America', 'Oceania', 'South America', 'International']
world_latest = world_latest[~world_latest['location'].isin(aggregates)]

# Plot total cases by country on a world map
fig = px.choropleth(
    world_latest,
    locations="location",
    locationmode="country names",
    color="total_cases",
    hover_name="location",
    color_continuous_scale="Reds",
    title="Total COVID-19 Cases by Country (Latest Data)"
)
fig.show()

#Prepare a dataframe with iso_code, total_cases for the latest date.
# Prepare a dataframe with iso_code and total_cases for the latest date
latest_date = covid_data['date'].max()
iso_cases_latest = covid_data[covid_data['date'] == latest_date][['iso_code', 'location', 'total_cases']]

print(iso_cases_latest.head())

#Plot a choropleth showing case density or vaccination rates.

# Example: Case density (cases per million)
if 'population' in covid_data.columns:
    covid_data['cases_per_million'] = covid_data['total_cases'] / covid_data['population'] * 1_000_000
    choropleth_df = covid_data[covid_data['date'] == latest_date][['iso_code', 'location', 'cases_per_million']]
    fig = px.choropleth(
        choropleth_df,
        locations="iso_code",
        color="cases_per_million",
        hover_name="location",
        color_continuous_scale="OrRd",
        title="COVID-19 Case Density (Cases per Million) by Country"
    )
    fig.show()
else:
    print("Population column not found. Cannot compute case density.")

# Example: Vaccination rates (total vaccinations per 100 people)
if 'total_vaccinations_per_hundred' in covid_data.columns:
    vacc_df = covid_data[covid_data['date'] == latest_date][['iso_code', 'location', 'total_vaccinations_per_hundred']]
    fig = px.choropleth(
        vacc_df,
        locations="iso_code",
        color="total_vaccinations_per_hundred",
        hover_name="location",
        color_continuous_scale="Blues",
        title="COVID-19 Vaccination Rates (per 100 people) by Country"
    )
    fig.show()
else:
    print("total_vaccinations_per_hundred column not found. Cannot plot vaccination rates.")
    
'''Key Insights from the COVID-19 Data:

South Africa consistently reported the highest total COVID-19 cases among the selected African countries, as seen in both the time series and the bar chart of top 10 countries by total cases.

Vaccination rollout varied greatly: Some countries, like South Africa and Botswana, achieved higher vaccination rates per 100 people, while others (such as Burundi and South Sudan) had very low vaccination coverage, as shown in the vaccination choropleth.

Death rates were not uniform: Countries like Zimbabwe and South Africa had higher average death rates compared to others in the region, possibly due to differences in healthcare infrastructure or reporting.

Case density anomalies: Small-population countries (e.g., Botswana) sometimes showed high case density (cases per million), even if their total case numbers were lower, highlighting the importance of normalizing by population.

Interesting pattern: Some countries experienced sharp spikes in daily new cases at different times, suggesting differences in outbreak waves or reporting practices. For example, Kenya and Uganda had noticeable surges that did not always align with neighboring countries.

Anomalies & Patterns:

Some countries reported very low or zero vaccination rates, which may indicate data gaps or logistical challenges.
A few countries had sudden jumps or drops in reported cases/deaths, likely due to reporting delays or data corrections.
The overall trend shows that wealthier or more urbanized countries tended to have both higher case numbers and higher vaccination rates.
This could be due to better healthcare access, more testing, and more efficient vaccination campaigns.
'''

# Save the plots as images
output_dir = os.path.join(script_dir, "plots")
os.makedirs(output_dir, exist_ok=True)

# Save the last plot as an image
latest_plot_path = os.path.join(output_dir, "latest_covid_cases.png")
fig.write_image(latest_plot_path)
print(f"Latest COVID-19 cases plot saved to {latest_plot_path}")

# Save the choropleth plot as an image  
choropleth_plot_path = os.path.join(output_dir, "covid_case_density.png")
fig.write_image(choropleth_plot_path)
print(f"COVID-19 case density plot saved to {choropleth_plot_path}")

# Save the vaccination rates plot as an image
vaccination_plot_path = os.path.join(output_dir, "covid_vaccination_rates.png")
fig.write_image(vaccination_plot_path)
print(f"COVID-19 vaccination rates plot saved to {vaccination_plot_path}")

# Save the bar chart of top 10 countries by total cases
bar_chart_path = os.path.join(output_dir, "top_10_countries_by_total_cases.png")
plt.figure(figsize=(12, 6))
plt.bar(top_countries['location'], top_countries['total_cases'], color='skyblue')

# Save the cleaned and processed data to a new CSV file
output_file_path = os.path.join(script_dir, "cleaned_covid_data.csv")
filtered_data.to_csv(output_file_path, index=False)
print(f"Cleaned data saved to {output_file_path}")

# Save the filtered data to a new CSV file
output_file_path = os.path.join(script_dir, "filtered_covid_data.csv")
filtered_data.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")