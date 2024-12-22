import { getInput } from '../../../utils/inputReader';

export const solvePart1 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 2, 
    useCustomInput, 
    customInput 
  });
  
  const reports = parseInput(input);

  let safeCount = 0;
  for (const report of reports) {
    const descending = isDescending(report);
    for (let i = 1;  i < report.length; i++ ) {
        if (isSafe(report[i], report[i-1], descending)) {
            safeCount++;
        }
    }
  }
  return safeCount;
};

export const solvePart2 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 2, 
    useCustomInput, 
    customInput 
  });
  
  // Your solution logic here
  return input.length;
};

const parseInput = (input: string[]): number[][] => {
    return input.map(x => x.split(' ').map(Number));
}

const isDescending = (input: number[]): boolean => {
    return input[0] > input[1]
}

const validSteps = new Set([1, 2, 3]);
const isSafe = (current: number, previous: number, descending: boolean): boolean => {
    const diff = descending ? previous - current : current - previous;
    return validSteps.has(diff);
}
