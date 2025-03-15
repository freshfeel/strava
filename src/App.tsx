import { useState } from 'react';
import { FriendCard } from './components/FriendCard';
import { MilestoneProgress } from './components/MilestoneProgress';
import { friends, milestone } from './stravaData';

function App() {
  return (
    <div className="min-h-screen bg-background text-white">
      <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-primary mb-2">
            Strava Weekly Progress
          </h1>
          <p className="text-xl text-gray-400 mb-6">
            Track your friends' activities and reach milestones together
          </p>
          <a
            href="/auth.html"
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primary-dark transition-colors duration-150 ease-in-out"
          >
            Connect with Strava
          </a>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {friends.map((friend) => (
            <FriendCard key={friend.id} friend={friend} />
          ))}
        </div>

        <div className="max-w-3xl mx-auto">
          <MilestoneProgress milestone={milestone} />
        </div>
      </div>
    </div>
  );
}

export default App;
