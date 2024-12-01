import { getInput } from '../utils/inputReader';

export const solvePart1 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 1, 
    useCustomInput, 
    customInput 
  });
  
  // Your solution logic here
  return input.length;
};

export const solvePart2 = async (useCustomInput = false, customInput = ''): Promise<number> => {
  const input = await getInput({ 
    day: 1, 
    useCustomInput, 
    customInput 
  });
  
  // Your solution logic here
  return input.length;
}; 