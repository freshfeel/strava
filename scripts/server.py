from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from update_strava_data import update_strava_data
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

def scheduled_update():
    """Run the Strava data update every hour"""
    try:
        update_strava_data()
    except Exception as e:
        print(f"Error updating Strava data: {e}")

# Create scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_update, trigger="interval", hours=1)
scheduler.start()

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/update', methods=['POST'])
def manual_update():
    try:
        update_strava_data()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run initial update
    scheduled_update()
    
    # Start server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 