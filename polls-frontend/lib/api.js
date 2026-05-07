// lib/api.js
const BASE_URL = 'http://localhost:8000/api';

async function handleResponse(response) {
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.message || `Error ${response.status}`);
  }
  return response.json();
}

export async function getPolls() {
  const response = await fetch(`${BASE_URL}/polls/`, {
    credentials: 'include', // envía cookie sessionid
  });
  return handleResponse(response);
}

export async function createPoll(question, choices) {
  const response = await fetch(`${BASE_URL}/polls/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, choices }),
    credentials: 'include',
  });
  return handleResponse(response);
}

export async function getPollResults(id) {
  const response = await fetch(`${BASE_URL}/polls/${id}/results/`, {
    credentials: 'include',
  });
  return handleResponse(response);
}

export async function vote(choiceId) {
  const response = await fetch(`${BASE_URL}/vote/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ choice_id: choiceId }),
    credentials: 'include',
  });
  return handleResponse(response);
}
