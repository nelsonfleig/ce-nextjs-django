"use client";
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export default function Home() {
  const { data, error, isLoading } = useSWR(
    "http://localhost:8001/api/hello",
    fetcher,
  );

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      <button>Lookup Data</button>
      <p>Data: {data.message}</p>
    </div>
  );
}
