import { getInput } from '../../../utils/inputReader';

export const solvePart1 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 1, 
    useCustomInput, 
    customInput 
  });
  
  const [list1, list2] = parseInput(input);
  const distances: number[] = [];

  while (list1.length > 0 && list2.length > 0) {
    const smallest1 = findSmallest(list1);
    const smallest2 = findSmallest(list2);
    list1.splice(list1.indexOf(smallest1), 1);
    list2.splice(list2.indexOf(smallest2), 1);
    distances.push(Math.abs(smallest1 - smallest2));
  }
  return distances.reduce((acc, curr) => acc + curr, 0);
};

export const solvePart2 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 1, 
    useCustomInput, 
    customInput 
  });

  const [list1, list2] = parseInput(input);
  const distances: number[] = [];
  for (const number of list1) {
    distances.push(countOccurences(list2, number) * number);
  }
  
  return distances.reduce((acc, curr) => acc + curr, 0);
};

const parseInput = (input: string[]): [number[], number[]] => {
  const list1: number[] = [];
  const list2: number[] = [];
  for (const line of input) {
    const [a, b] = line.split('  ').map(Number);
    list1.push(a);
    list2.push(b);
  }
  return [list1, list2];
};

const findSmallest = (list: number[]): number => {
  return Math.min(...list);
};

const countOccurences = (list: number[], number: number): number => {
  return list.filter(n => n === number).length;
};

