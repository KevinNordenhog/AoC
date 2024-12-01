interface InputOptions {
    day: number;
    useCustomInput?: boolean;
    customInput?: string;
    separator?: string;
  }
  
  export const getInput = async ({ day, useCustomInput = false, customInput = '', separator = '\n' }: InputOptions): Promise<string[]> => {
    let input: string;
  
    if (useCustomInput && customInput) {
      input = customInput;
    } else {
      const response = await fetch(`/api/input/${day}`);
      const data = await response.json();
      input = data.input;
    }
  
    return input
      .split(separator)
      .map(line => line.replace(/\r$/, ''))
      .filter(line => line.length > 0);
  };