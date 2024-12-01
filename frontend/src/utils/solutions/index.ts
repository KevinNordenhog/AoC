import * as day1 from './day1/day1';

export const solutions: Record<number, { 
  solvePart1: (useCustomInput?: boolean, customInput?: string) => Promise<number>;
  solvePart2: (useCustomInput?: boolean, customInput?: string) => Promise<number>;
}> = {
  1: day1,
};