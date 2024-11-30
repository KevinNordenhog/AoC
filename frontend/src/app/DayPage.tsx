interface PageProps {
    params: {
      day: string;
    };
  }
  
  export default function DayPage({ params }: PageProps) {
    const day = parseInt(params.day);
  
    return (
      <div className="min-h-screen p-8">
        <main className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold mb-8">Day {day}</h1>
          
          <div className="space-y-8">
            <section>
              <h2 className="text-xl font-semibold mb-4">Part 1</h2>
              <textarea 
                className="w-full h-32 p-2 border rounded"
                placeholder="Paste your input here..."
              />
              <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded">
                Solve Part 1
              </button>
            </section>
  
            <section>
              <h2 className="text-xl font-semibold mb-4">Part 2</h2>
              <textarea 
                className="w-full h-32 p-2 border rounded"
                placeholder="Paste your input here..."
              />
              <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded">
                Solve Part 2
              </button>
            </section>
          </div>
        </main>
      </div>
    );
  }