'use client';

import { use } from 'react';
import { useState } from 'react';
import * as solutions from '@/utils/solutions';

export default function DayPage({ params }: { params: Promise<{ day: string }> }) {
  const [input, setInput] = useState('');
  const [part1Result, setPart1Result] = useState<number | null>(null);
  const [part2Result, setPart2Result] = useState<number | null>(null);

  const resolvedParams = use(params);
  const day = parseInt(resolvedParams.day);
  const solution = solutions[day as keyof typeof solutions];

  const solvePart1 = () => {
    const result = solution.solvePart1(input);
    setPart1Result(result);
  };

  const solvePart2 = () => {
    const result = solution.solvePart2(input);
    setPart2Result(result);
  };

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-8">Day {day}</h1>
      
      <div className="space-y-8">
        <div>
          <h2 className="text-xl font-semibold mb-4">Input</h2>
          <textarea 
            className="w-full h-48 p-4 border rounded-lg font-mono"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Paste your puzzle input here..."
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h2 className="text-xl font-semibold mb-4">Part 1</h2>
            <button 
              onClick={solvePart1}
              className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
              Solve Part 1
            </button>
            {part1Result !== null && (
              <div className="mt-4 p-4 bg-gray-100 rounded-lg">
                <p className="font-mono">Result: {part1Result}</p>
              </div>
            )}
          </div>

          <div>
            <h2 className="text-xl font-semibold mb-4">Part 2</h2>
            <button 
              onClick={solvePart2}
              className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
              Solve Part 2
            </button>
            {part2Result !== null && (
              <div className="mt-4 p-4 bg-gray-100 rounded-lg">
                <p className="font-mono">Result: {part2Result}</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
} 