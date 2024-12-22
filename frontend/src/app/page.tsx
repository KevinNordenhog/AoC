import DayCard from "@/components/DayCard";

export default function Home() {
  return (
    <div className="min-h-screen p-8">
      <main className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">Advent of Code Solutions</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <DayCard
            day={1}
            title="Day 1: Historian Hysteria"
            completed={true}
          />
          <DayCard day={2} title="Day 2: Red-Nosed Reports" completed={false} />
        </div>
      </main>
    </div>
  );
}
