import { useEffect, useState } from 'react';
import Link from 'next/link';
import { getPolls, vote } from '../lib/api';

export default function Home() {
  const [polls, setPolls] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    getPolls()
      .then(setPolls)
      .catch(err => setMessage('Error al cargar encuestas: ' + err.message));
  }, []);

  const handleVote = async (choiceId, pollId) => {
    try {
      await vote(choiceId);
      setMessage('¡Voto registrado correctamente!');
      // Opcional: redirigir a la página de resultados
      // router.push(`/results/${pollId}`);
    } catch (err) {
      setMessage('Error al votar: ' + err.message);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Encuestas</h1>
      <Link href="/create">
        <button>➕ Crear nueva encuesta</button>
      </Link>
      {message && <p style={{ color: 'blue' }}>{message}</p>}
      {polls.map(poll => (
        <div key={poll.id} style={{ border: '1px solid #ccc', margin: '1rem 0', padding: '1rem' }}>
          <h2>{poll.question}</h2>
          <ul>
            {poll.choices.map(choice => (
              <li key={choice.id}>
                {choice.text}
                <button onClick={() => handleVote(choice.id, poll.id)} style={{ marginLeft: '1rem' }}>
                  Votar
                </button>
              </li>
            ))}
          </ul>
          <Link href={`/results/${poll.id}`}>
            Ver resultados
          </Link>
        </div>
      ))}
    </div>
  );
}
