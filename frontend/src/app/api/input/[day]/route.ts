import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET(
  request: Request,
  { params }: { params: { day: string } }
) {
  const day = await params.day;
  
  try {
    const filePath = path.join(process.cwd(), 'src', 'utils', 'solutions', `day${day}`, 'input.txt');
    const input = fs.readFileSync(filePath, 'utf8');
    return NextResponse.json({ input, success: true });
  } catch (error) {
    console.error('Error reading input file:', error);
    return NextResponse.json({ error: 'Failed to read input file', success: false }, { status: 500 });
  }
} 