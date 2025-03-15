# 🏃‍♂️ Strava Weekly Progress

A beautiful React application that displays your weekly running progress and milestones from Strava. Built with React, Tailwind CSS, and the Strava API.

![Strava Weekly Progress Screenshot](screenshot.png)

## ✨ Features

- 📊 Track your weekly running distance
- 🎯 Set and monitor distance milestones
- 🔄 Auto-updates every hour with your latest Strava activities
- 🎨 Beautiful, responsive UI built with Tailwind CSS
- 🔒 Secure Strava OAuth integration

## 🚀 Live Demo

Check out the live demo at: https://freshfeel.github.io/strava/

## 🛠️ Tech Stack

- **Frontend:**
  - React
  - TypeScript
  - Tailwind CSS
  - Vite

- **Data Updates:**
  - Python
  - Strava API
  - GitHub Actions (automated updates)

## 🔧 Setup

### Prerequisites

- Node.js (v18 or higher)
- Python 3.x
- A Strava account and API application

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/freshfeel/strava.git
   cd strava
   ```

2. Install dependencies:
   ```bash
   npm install
   cd scripts
   pip install -r requirements.txt
   cd ..
   ```

3. Create a `.env` file in the `scripts` directory:
   ```env
   STRAVA_CLIENT_ID=your_client_id
   STRAVA_CLIENT_SECRET=your_client_secret
   STRAVA_ATHLETE_144790047_TOKEN=your_refresh_token
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

### Deployment

1. Fork this repository

2. In your forked repository's settings:
   - Go to "Settings" > "Pages"
   - Set the source to "GitHub Actions"

3. Add your Strava credentials as GitHub Secrets:
   - Go to "Settings" > "Secrets and variables" > "Actions"
   - Add the following secrets:
     - `STRAVA_CLIENT_ID`
     - `STRAVA_CLIENT_SECRET`
     - `STRAVA_ATHLETE_TOKEN`

4. Update the `auth.html` file:
   - Replace `YOUR_GITHUB_USERNAME` with your GitHub username

5. Push your changes:
   ```bash
   git push origin main
   ```

The GitHub Action will automatically:
- Update your Strava data every hour
- Build and deploy the site to GitHub Pages
- Keep your progress up to date

## 📝 Configuration

### Customizing the Weekly Target

Edit `scripts/update_strava_data.py` to change the weekly distance target:

```python
milestone_data = {
    'current': total_distance,
    'target': 200,  # Change this value (in kilometers)
    'title': 'Combined Weekly Distance'
}
```

### Styling

The app uses Tailwind CSS for styling. Customize the theme in `tailwind.config.cjs`:

```js
theme: {
  extend: {
    colors: {
      background: '#1a1a1a',
      primary: '#fc4c02',
      'primary-dark': '#e44400',
    },
  },
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- [Strava API](https://developers.strava.com/) for providing activity data
- [Tailwind CSS](https://tailwindcss.com/) for the styling system
- [React](https://reactjs.org/) for the UI framework
