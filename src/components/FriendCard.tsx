import { Friend } from '../types';

interface FriendCardProps {
  friend: Friend;
}

export const FriendCard = ({ friend }: FriendCardProps) => {
  return (
    <div className="bg-surface rounded-xl shadow-lg overflow-hidden transform transition-all hover:scale-105 hover:bg-surface-light">
      <div className="p-6">
        <div className="flex items-center space-x-4">
          <img
            src={friend.avatar}
            alt={friend.name}
            className="w-16 h-16 rounded-full object-cover ring-2 ring-primary"
          />
          <div>
            <h3 className="text-xl font-semibold text-white">{friend.name}</h3>
            <div className="mt-1 flex items-center">
              <span className="text-3xl font-bold text-primary">
                {friend.distanceThisWeek}
              </span>
              <span className="ml-2 text-gray-400">km this week</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}; 