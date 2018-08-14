import numpy as np 
import geocoder


def process_df(df):
    """
    df: pd.DataFrame
    """
    
    df.dropna(subset=['lat', 'lon'], axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    # Add new column to hold the years
    df["year"] = [int(x.split("-")[0]) for x in df['date']]

    # Convert coordinates to decimal degrees ISO 6709 format i.e:(14.76º,
    # -23.2234º)
    lat_flip = np.logical_and(df["lat-dir"] == "S", df["lat"] >= 0)
    df.loc[lat_flip, "lat"] *= -1
    lon_flip = np.logical_and(df["lon-dir"] == "W", df["lon"] >= 0)
    df.loc[lon_flip, "lon"] *= -1

    legend = []
    print('Starting to pull data from Google Geolocation API')
    for i in range(len(df['impact-e'])):
        print(i+1, "of {}".format(len(df)+1))
        g = geocoder.google([df['lat'][i], df['lon'][i]], method='reverse')
        city = '{}'.format(g.city) if g.city else "N/A"
        country = '{}'.format(g.country) if g.country else "N/A"

        if city is not None and country is not None:
            location = "Location: {},{}<br>".format(city, country)
        
        if df['impact-e'][i] < 10:
            legend.append('{}<10 kt<br>{}'.format(location, str(df['date'][i])))
        else:
            legend.append('{}{} kt<br>{}'.format(location, df['impact-e'][i], str(df['date'][i])))

    df['legend'] = legend

    return df
