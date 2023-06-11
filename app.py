from flask import Flask, jsonify
from flask import render_template
from urllib.request import urlopen
import json
import requests
from datetime import timezone, datetime, timedelta

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://statsapi.web.nhl.com/api/v1/schedule'
    today = datetime.now().strftime('%Y-%m-%d')

    end_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    params = {'startDate': today, 'endDate': end_date}
    response = requests.get(url, params=params)
    data = response.json()

    team_chars = {
        'Anaheim Ducks': 'https://static.wixstatic.com/media/3d7fb3_769a41303c154bd0aa654c62a7cd2754~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_769a41303c154bd0aa654c62a7cd2754~mv2.png',
        'Boston Bruins': 'https://static.wixstatic.com/media/3d7fb3_f08c6d14ba664c94a04d55d8a15af472~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_f08c6d14ba664c94a04d55d8a15af472~mv2.png',
        'Buffalo Sabres': 'https://static.wixstatic.com/media/3d7fb3_20aa5d7fbd6440e397a6ec98940193e5~mv2.png/v1/fill/w_703,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_20aa5d7fbd6440e397a6ec98940193e5~mv2.png',
        'Calgary Flames': 'https://static.wixstatic.com/media/3d7fb3_b901b23a600f41fc88b0f42fd38deaf5~mv2.png/v1/fill/w_703,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_b901b23a600f41fc88b0f42fd38deaf5~mv2.png',
        'Carolina Hurricanes': 'https://static.wixstatic.com/media/3d7fb3_aff9216f99ff4cceb61caba45a2e8b9c~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_aff9216f99ff4cceb61caba45a2e8b9c~mv2.png',
        'Chicago Blackhawks': 'https://static.wixstatic.com/media/3d7fb3_040659cb7db94b39b8560276a35fc8e3~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_040659cb7db94b39b8560276a35fc8e3~mv2.png',
        'Colorado Avalanche': 'https://static.wixstatic.com/media/3d7fb3_3100c4beeab64400872ef2c43be9ffa3~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_3100c4beeab64400872ef2c43be9ffa3~mv2.png',
        'Columbus Blue Jackets': 'https://static.wixstatic.com/media/3d7fb3_546a74b41863469583ed937d08635e73~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_546a74b41863469583ed937d08635e73~mv2.png',
        'Dallas Stars': 'https://static.wixstatic.com/media/3d7fb3_dd8b454505b34a5d940a030cab1fe0cd~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_dd8b454505b34a5d940a030cab1fe0cd~mv2.png',
        'Detroit Red Wings': 'https://static.wixstatic.com/media/3d7fb3_df0dfc38cfe54c32a7d963b6d7180802~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_df0dfc38cfe54c32a7d963b6d7180802~mv2.png',
        'Edmonton Oilers': 'https://static.wixstatic.com/media/3d7fb3_934d2213949c49aca9d509aa4c68531a~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_934d2213949c49aca9d509aa4c68531a~mv2.png',
        'Florida Panthers': 'https://static.wixstatic.com/media/3d7fb3_5cf413a02d734d54a082b62ec8255b83~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_5cf413a02d734d54a082b62ec8255b83~mv2.png',
        'Los Angeles Kings': 'https://static.wixstatic.com/media/3d7fb3_70808b1d5b6948c7a656fde76e2abac5~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_70808b1d5b6948c7a656fde76e2abac5~mv2.png',
        'Minnesota Wild': 'https://static.wixstatic.com/media/3d7fb3_49f5c78c5b7e4d999e62514d7e4a73fc~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_49f5c78c5b7e4d999e62514d7e4a73fc~mv2.png',
        'Montréal Canadiens': 'https://static.wixstatic.com/media/3d7fb3_85b92c6f6a894b3fbf445f14de9f332b~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_85b92c6f6a894b3fbf445f14de9f332b~mv2.png',
        'Nashville Predators': 'https://static.wixstatic.com/media/3d7fb3_1eda07a599f64197b183da45d93600eb~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_1eda07a599f64197b183da45d93600eb~mv2.png',
        'New Jersey Devils': 'https://static.wixstatic.com/media/3d7fb3_e5bc8a140c0b43068fdaccf1a5452a05~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_e5bc8a140c0b43068fdaccf1a5452a05~mv2.png',
        'New York Islanders': 'https://static.wixstatic.com/media/3d7fb3_96602e965394421cacdcf9222d04601b~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_96602e965394421cacdcf9222d04601b~mv2.png',
        'New York Rangers': 'https://static.wixstatic.com/media/3d7fb3_9cbfc2c0b9a84f31a97db8fa905e124c~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_9cbfc2c0b9a84f31a97db8fa905e124c~mv2.png',
        'Ottawa Senators': 'https://static.wixstatic.com/media/3d7fb3_94badec8d3eb440c98c4a5558081eda1~mv2.png/v1/fill/w_703,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_94badec8d3eb440c98c4a5558081eda1~mv2.png',
        'Philadelphia Flyers': 'https://static.wixstatic.com/media/3d7fb3_65e8e6efb9b04b61b7d5bf5ed6674831~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_65e8e6efb9b04b61b7d5bf5ed6674831~mv2.png',
        'Arizona Coyotes': 'https://static.wixstatic.com/media/3d7fb3_59883f0a0976478387482b3abd7450db~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_59883f0a0976478387482b3abd7450db~mv2.png',
        'Pittsburgh Penguins': 'https://static.wixstatic.com/media/3d7fb3_d6f44625497b4c1384e059510e51422e~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_d6f44625497b4c1384e059510e51422e~mv2.png',
        'San Jose Sharks': 'https://static.wixstatic.com/media/3d7fb3_be8ff4f73ed343d6b6237e92df93d1f4~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_be8ff4f73ed343d6b6237e92df93d1f4~mv2.png',
        'St. Louis Blues': 'https://static.wixstatic.com/media/3d7fb3_1f890d2dd7614ae8842c27d8f8fd3d56~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_1f890d2dd7614ae8842c27d8f8fd3d56~mv2.png',
        'Seattle Kraken': 'https://static.wixstatic.com/media/3d7fb3_effbb7bc858643bc99805af05b4104cf~mv2.png/v1/fill/w_703,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_effbb7bc858643bc99805af05b4104cf~mv2.png',
        'Tampa Bay Lightning': 'https://static.wixstatic.com/media/3d7fb3_b71731f53f974b99a5f94dc9ae01b01d~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_b71731f53f974b99a5f94dc9ae01b01d~mv2.png',
        'Toronto Maple Leafs': 'https://static.wixstatic.com/media/3d7fb3_7ce0b4815c3e4b0e8c1bb2243c71aa2c~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_7ce0b4815c3e4b0e8c1bb2243c71aa2c~mv2.png',
        'Vancouver Canucks': 'https://static.wixstatic.com/media/3d7fb3_8f986c9f35e44805ae9de5499457a741~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_8f986c9f35e44805ae9de5499457a741~mv2.png',
        'Washington Capitals': 'https://static.wixstatic.com/media/3d7fb3_2ba590c8eeb54c8a96ffdb6319107613~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_2ba590c8eeb54c8a96ffdb6319107613~mv2.png',
        'Winnipeg Jets': 'https://static.wixstatic.com/media/3d7fb3_77155ceb5ad24651a45e61ff69481757~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_77155ceb5ad24651a45e61ff69481757~mv2.png',
        'Vegas Golden Knights': 'https://static.wixstatic.com/media/3d7fb3_59f4b51de03345448bd27988625ef40a~mv2.png/v1/fill/w_777,h_703,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/3d7fb3_59f4b51de03345448bd27988625ef40a~mv2.png'
    }

    games = []
    for date in data['dates']:
        for game in date['games']:
            game_info = {
                'game_id': game['gamePk'],
                'away_team': game['teams']['away']['team']['name'],
                'away_team_char': team_chars.get(game['teams']['away']['team']['name'], '0'),
                'home_team': game['teams']['home']['team']['name'],
                'home_team_char': team_chars.get(game['teams']['home']['team']['name'], '0')
            }
            if game['status']['abstractGameState'] == 'Live':
                game_info['status'] = 'LIVE'
                game_info['away_score'] = game['teams']['away']['score']
                game_info['home_score'] = game['teams']['home']['score']
            else:
                game_info['status'] = 'Scheduled'
                time_format = '%Y-%m-%dT%H:%M:%SZ'
                start_time_utc_str = game['gameDate']
                start_time_utc_dt_obj = datetime.strptime(
                    start_time_utc_str, time_format)
                start_time_local_dt_obj = start_time_utc_dt_obj.replace(
                    tzinfo=timezone.utc).astimezone(tz=None)

                formatted_start_time_local_str = start_time_local_dt_obj.strftime(
                    '%Y-%m-%d %H:%M')

                game_info["start_time"] = formatted_start_time_local_str

            games.append(game_info)
    return render_template('index.html', games=games)


@app.route('/teams')
def teams():
    link = "https://statsapi.web.nhl.com/api/v1/teams?expand=team.stats"
    response = urlopen(link)
    content = response.read()
    data = json.loads(content)
    teams = []

    for team in data["teams"]:
        name = team["name"]
        id = team["id"]
        wins = team["teamStats"][0]["splits"][0]["stat"]["wins"]
        losses = team["teamStats"][0]["splits"][0]["stat"]["losses"]
        ot = team["teamStats"][0]["splits"][0]["stat"]["ot"]
        pts = team["teamStats"][0]["splits"][0]["stat"]["pts"]
        teams.append({"name": name, "wins": wins,
                     "losses": losses, "ot": ot, "pts": pts})

    sorted_teams = sorted(teams, key=lambda d: d["pts"], reverse=True)

    for i, team in enumerate(sorted_teams):
        team["id"] = i + 1

    return render_template('teams.html', teams=sorted_teams)


@app.route('/players')
def players():

    url = 'https://statsapi.web.nhl.com/api/v1/teams'
    response = requests.get(url)
    data = response.json()
    teams = data['teams']
    players = []
    for team in teams:
        roster_url = f"{team['link']}/roster"
        roster_response = requests.get(
            f'https://statsapi.web.nhl.com{roster_url}')
        roster_data = roster_response.json()
        for player in roster_data['roster']:
            player_url = f"{player['person']['link']}/stats?stats=statsSingleSeason&season=20222023"
            player_response = requests.get(
                f'https://statsapi.web.nhl.com{player_url}')
            player_data = player_response.json()
            if 'stats' in player_data and len(player_data['stats']) > 0 and len(player_data['stats'][0]['splits']) > 0:
                stat = player_data['stats'][0]['splits'][0]['stat']
                if 'points' in stat:
                    goals = stat['goals']
                    assists = stat['assists']
                    plusminus = stat['plusMinus']
                    currentteam = team['name']
                    points = stat['points']
                    players.append(
                        {'name': player['person']['fullName'], 'currentteam': currentteam, 'goals': goals, 'assists': assists, 'plusminus': plusminus, 'points': points})

    sorted_players = sorted(players, key=lambda x: x['points'], reverse=True)

    return render_template('players.html', players=sorted_players)


if __name__ == '__main__':
    app.run(debug=True)
