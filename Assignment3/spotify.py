import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests


app = dash.Dash(__name__)


url = "https://spotify23.p.rapidapi.com/tracks/"
params = {
    "ids": "4WNcduiCmDNfmTEz7JvmLv"
}
headers = {
    "X-RapidAPI-Key": "29c4f831cfmsh52dc9590010758dp119888jsn6df53e96b996",
    "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}
response = requests.get(url, params=params, headers=headers)
data = response.json()

track = data['tracks'][0] 

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Spotify Track Information"),
    html.Div([
        html.P(f"Track Name: {track['name']}"),
        html.P(f"Artist(s): {', '.join(artist['name'] for artist in track['artists'])}"),
        html.P(f"Album: {track['album']['name']}"),
        html.P(f"Release Date: {track['album']['release_date']}"),
        html.Audio(src=track['preview_url'], controls=True) if track['preview_url'] else html.P("No preview available")
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)



