import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import Link from 'next/link';
import { getPollResults } from '../../lib/api';

export default function PollResults() {
  const router = useRouter();
  const { id } = router.query;
  const [poll, setPoll] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!id) return;
    getPollResults(id)
      .then(data => {
        setPoll(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div>Cargando resultados...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!poll) return <div>No se encontró la encuesta</div>;

  // Calcular porcentajes
  const total = poll.total_votes;
  const choicesWithPercent = poll.choices.map(choice => ({
    ...choice,
    percent: total === 0 ? 0 : (choice.votes / total) * 100,
  }));

  return (
    <div style={{ padding: '2rem' }}>
      <Link href="/">← Volver a encuestas</Link>
      <h1>{poll.question}</h1>
      <p><strong>Total de votos:</strong> {total}</p>
      <ul>
        {choicesWithPercent.map(choice => (
          <li key={choice.question} style={{ margin: '1rem 0' }}>
            <span>{choice.question}</span>
            <span> – {choice.votes} votos ({choice.percent.toFixed(1)}%)</span>
            <div style={{
              backgroundColor: '#4caf50',
              width: `${choice.percent}%`,
              height: '8px',
              marginTop: '4px',
              borderRadius: '4px',
            }} />
          </li>
        ))}
      </ul>
    </div>
  );
}
