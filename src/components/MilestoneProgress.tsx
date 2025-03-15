import { MilestoneGoal } from '../types';

interface MilestoneProgressProps {
  milestone: MilestoneGoal;
}

export const MilestoneProgress = ({ milestone }: MilestoneProgressProps) => {
  const progress = (milestone.current / milestone.target) * 100;

  return (
    <div className="bg-surface rounded-2xl shadow-xl p-8 transform hover:scale-[1.02] transition-all hover:bg-surface-light">
      <h2 className="text-3xl font-bold text-white mb-6">{milestone.title}</h2>
      <div className="relative pt-1">
        <div className="flex items-center justify-between mb-2">
          <div>
            <span className="text-4xl font-bold text-primary">
              {milestone.current.toFixed(1)}
            </span>
            <span className="ml-2 text-xl text-gray-400">km</span>
          </div>
          <div className="text-right">
            <span className="text-xl text-gray-400">Goal: </span>
            <span className="text-xl font-semibold text-white">
              {milestone.target} km
            </span>
          </div>
        </div>
        <div className="overflow-hidden h-6 mb-4 text-xs flex rounded-full bg-surface-light">
          <div
            style={{ width: `${Math.min(progress, 100)}%` }}
            className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-primary transition-all duration-500"
          />
        </div>
        <div className="text-center text-gray-400">
          {progress.toFixed(1)}% Complete
        </div>
      </div>
    </div>
  );
}; 