import { useState } from 'react';
import { useRouter } from 'next/router';
import { createPoll } from '../lib/api';

export default function CreatePoll() {
  const router = useRouter();
  const [question, setQuestion] = useState('');
  const [choices, setChoices] = useState(['', '']); // mínimo 2 opciones
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const addChoice = () => setChoices([...choices, '']);
  const removeChoice = (index) => {
    if (choices.length <= 2) return;
    const newChoices = [...choices];
    newChoices.splice(index, 1);
    setChoices(newChoices);
  };
  const updateChoice = (index, value) => {
    const newChoices = [...choices];
    newChoices[index] = value;
    setChoices(newChoices);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    if (!question.trim()) return setError('La pregunta es requerida');
    const nonEmptyChoices = choices.filter(c => c.trim() !== '');
    if (nonEmptyChoices.length < 2) return setError('Debe haber al menos dos opciones válidas');

    setLoading(true);
    try {
      await createPoll(question, nonEmptyChoices);
      router.push('/');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Crear nueva encuesta</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Pregunta:</label><br />
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
            required
          />
        </div>
        <div>
          <label>Opciones de respuesta (mínimo 2):</label>
          {choices.map((choice, idx) => (
            <div key={idx} style={{ marginTop: '0.5rem' }}>
              <input
                type="text"
                value={choice}
                onChange={(e) => updateChoice(idx, e.target.value)}
                style={{ width: '80%', padding: '0.5rem' }}
                placeholder={`Opción ${idx + 1}`}
              />
              {choices.length > 2 && (
                <button type="button" onClick={() => removeChoice(idx)} style={{ marginLeft: '0.5rem' }}>
                  Eliminar
                </button>
              )}
            </div>
          ))}
          <button type="button" onClick={addChoice} style={{ marginTop: '0.5rem' }}>
            + Agregar opción
          </button>
        </div>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit" disabled={loading} style={{ marginTop: '1rem' }}>
          {loading ? 'Creando...' : 'Crear encuesta'}
        </button>
      </form>
    </div>
  );
}
