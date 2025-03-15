import os
import requests
from datetime import datetime, timedelta
import json

class StravaDataFetcher:
    BASE_URL = "https://www.strava.com/api/v3"
    
    def __init__(self):
        self.client_id = os.getenv('STRAVA_CLIENT_ID')
        self.client_secret = os.getenv('STRAVA_CLIENT_SECRET')
        self.athlete_tokens = self._get_athlete_tokens()
        print(f"Found athlete tokens: {list(self.athlete_tokens.keys())}")
    
    def _get_athlete_tokens(self):
        """Get athlete tokens from environment variables.
        Format: STRAVA_ATHLETE_TOKENS=id1:token1,id2:token2,...
        """
        tokens = {}
        tokens_str = os.getenv('STRAVA_ATHLETE_TOKENS', '')
        if tokens_str:
            token_pairs = tokens_str.split(',')
            for pair in token_pairs:
                if ':' in pair:
                    athlete_id, token = pair.strip().split(':')
                    # Store athlete_id as integer
                    tokens[int(athlete_id)] = token
        return tokens
    
    def _refresh_access_token(self, refresh_token):
        """Refresh the access token using the refresh token."""
        print(f"Refreshing access token...")
        response = requests.post(
            f"{self.BASE_URL}/oauth/token",
            data={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }
        )
        data = response.json()
        print(f"Token refresh response: {data.get('token_type', 'unknown')}")
        return data['access_token']
    
    def get_athlete_activities(self, athlete_id, after_date):
        """Get activities for a specific athlete after a given date."""
        print(f"\nFetching activities for athlete {athlete_id}")
        # Convert athlete_id to int for dictionary lookup
        athlete_id = int(athlete_id)
        refresh_token = self.athlete_tokens.get(athlete_id)
        if not refresh_token:
            raise ValueError(f"No refresh token found for athlete {athlete_id}")
        
        access_token = self._refresh_access_token(refresh_token)
        
        response = requests.get(
            f"{self.BASE_URL}/athlete/activities",
            headers={'Authorization': f'Bearer {access_token}'},
            params={
                'after': int(after_date.timestamp()),
                'per_page': 100  # Maximum activities per page
            }
        )
        
        activities = response.json()
        print(f"Found {len(activities)} activities")
        for activity in activities:
            print(f"Activity on {activity['start_date']}: {activity['type']} - {activity['distance']/1000:.2f} km")
        return activities
    
    def get_athlete_profile(self, athlete_id):
        """Get athlete's profile data using their refresh token."""
        # Convert athlete_id to int for dictionary lookup
        athlete_id = int(athlete_id)
        refresh_token = self.athlete_tokens.get(athlete_id)
        if not refresh_token:
            return {
                'name': f"Athlete {athlete_id}",
                'avatar': "https://i.pravatar.cc/150?img=1"
            }
        
        access_token = self._refresh_access_token(refresh_token)
        
        response = requests.get(
            f"{self.BASE_URL}/athlete",
            headers={'Authorization': f'Bearer {access_token}'}
        )
        
        athlete_data = response.json()
        return {
            'name': f"{athlete_data['firstname']} {athlete_data['lastname']}",
            'avatar': athlete_data.get('profile', "https://i.pravatar.cc/150?img=1")
        }
    
    def get_weekly_running_distances(self, athlete_ids):
        """Get the running distances for the past week for multiple athletes."""
        one_week_ago = datetime.now() - timedelta(days=7)
        print(f"\nFetching activities since {one_week_ago}")
        athlete_distances = {}
        
        for athlete_id in athlete_ids:
            try:
                activities = self.get_athlete_activities(athlete_id, one_week_ago)
                profile = self.get_athlete_profile(athlete_id)
                
                # Sum up distances for running activities only (including virtual runs)
                total_distance = sum(
                    activity['distance'] / 1000  # Convert meters to kilometers
                    for activity in activities
                    if activity['type'] in ['Run', 'VirtualRun']
                )
                
                # Store with integer athlete_id
                athlete_distances[int(athlete_id)] = {
                    'distance': round(total_distance, 2),
                    'name': profile['name'],
                    'avatar': profile['avatar']
                }
            except Exception as e:
                print(f"Error fetching data for athlete {athlete_id}: {str(e)}")
                athlete_distances[int(athlete_id)] = {
                    'distance': 0,
                    'name': f"Athlete {athlete_id}",
                    'avatar': "https://i.pravatar.cc/150?img=1",
                    'error': str(e)
                }
        
        return athlete_distances

def main():
    # Example athlete IDs
    athlete_ids = [144790047]  # Replace with actual athlete IDs
    
    fetcher = StravaDataFetcher()
    weekly_distances = fetcher.get_weekly_running_distances(athlete_ids)
    
    # Save the results to a JSON file
    with open('weekly_distances.json', 'w') as f:
        json.dump(weekly_distances, f, indent=2)
    
    print("\nWeekly running distances:")
    for athlete_id, data in weekly_distances.items():
        print(f"{data['name']}: {data['distance']} km")

if __name__ == "__main__":
    main() 