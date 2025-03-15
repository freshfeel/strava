import os
import json
from dotenv import load_dotenv
from fetch_strava_data import StravaDataFetcher

def update_strava_data():
    # Load environment variables
    load_dotenv()
    
    # Initialize the data fetcher
    fetcher = StravaDataFetcher()
    
    # Get weekly distances for all athletes
    athlete_ids = [144790047]  # Add more athlete IDs here if needed
    weekly_distances = fetcher.get_weekly_running_distances(athlete_ids)
    
    # Calculate total distance for milestone
    total_distance = sum(data['distance'] for data in weekly_distances.values())
    
    # Format data for the TypeScript file
    friends_data = []
    for athlete_id, data in weekly_distances.items():
        friends_data.append({
            'id': int(athlete_id),
            'name': data['name'],
            'avatar': data['avatar'],
            'distanceThisWeek': data['distance']
        })
    
    milestone_data = {
        'current': total_distance,
        'target': 200,  # Weekly target in kilometers
        'title': 'Combined Weekly Distance'
    }
    
    # Generate TypeScript code
    ts_code = 'import { Friend, MilestoneGoal } from \'./types\';\n\n'
    ts_code += f'export const friends: Friend[] = {json.dumps(friends_data, indent=2)};\n\n'
    ts_code += f'export const milestone: MilestoneGoal = {json.dumps(milestone_data, indent=2)};\n'
    
    # Write to the TypeScript file
    strava_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'stravaData.ts')
    with open(strava_data_path, 'w') as f:
        f.write(ts_code)
    
    print(f"Updated {strava_data_path}")
    print(f"Total distance: {total_distance} km")

if __name__ == "__main__":
    update_strava_data() 