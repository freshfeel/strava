import time
import schedule
from update_strava_data import update_mock_data

def job():
    print(f"\nRunning update at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        update_mock_data()
    except Exception as e:
        print(f"Error during update: {str(e)}")

def main():
    # Schedule the job to run every hour
    schedule.every().hour.do(job)
    
    # Run once immediately
    job()
    
    print("\nUpdate scheduler is running. Press Ctrl+C to stop.")
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\nStopping scheduler...")
            break
        except Exception as e:
            print(f"Error in scheduler: {str(e)}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main() 