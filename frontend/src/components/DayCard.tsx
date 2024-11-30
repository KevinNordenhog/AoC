interface DayCardProps {
  day: number;
  title: string;
  completed: boolean;
}

export default function DayCard({ day, title, completed }: DayCardProps) {
  return (
    <a 
      href={`/day/${day}`}
      className="block p-6 border rounded-lg hover:border-blue-500 transition-colors"
    >
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm text-gray-500">Day {day}</span>
        {completed && (
          <span className="text-green-500">✓</span>
        )}
      </div>
      <h2 className="text-lg font-semibold">{title}</h2>
    </a>
  );
}
