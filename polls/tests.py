from django.test import TestCase
from .models import (
    Poll,
    Choice,
    Vote,
)
from .serializers import (
    QuestionCreateSerializer,
    VoteSerializer,
)


class QuestionCreateSerializerTest(TestCase):
    def test_valid_data_creates_poll_and_choices(self):
        data = {
            'question': '¿Cuál es tu color favorito?',
            'choices': ['Rojo', 'Azul', 'Verde']
        }
        serializer = QuestionCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        poll = serializer.save()
        
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(poll.question, data['question'])
        
        self.assertEqual(Choice.objects.count(), 3)
        choices_texts = Choice.objects.filter(poll=poll).values_list('text', flat=True)
        self.assertCountEqual(choices_texts, data['choices'])
    
    def test_choices_less_than_two_is_invalid(self):
        data = {
            'question': 'Pregunta con una opción',
            'choices': ['Solo una']
        }
        serializer = QuestionCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
        self.assertEqual(
            serializer.errors['non_field_errors'][0],
            "At least two choices are required."
        )
        self.assertEqual(Poll.objects.count(), 0)
        self.assertEqual(Choice.objects.count(), 0)


class VoteSerializerTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question="¿Color favorito?")
        self.choice = Choice.objects.create(poll=self.poll, text="Rojo")
        self.valid_data = {'choice_id': self.choice.id}
    
    def test_valid_choice_id_creates_vote(self):
        serializer = VoteSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        vote = serializer.save()
        self.assertIsInstance(vote, Vote)
        self.assertEqual(vote.choice_id, self.choice.id)
        self.assertEqual(Vote.objects.count(), 1)
    
    def test_invalid_choice_id_raises_validation_error(self):
        invalid_data = {'choice_id': 9999}
        serializer = VoteSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('choice_id', serializer.errors)
        expected_msg = f"Choice with id 9999 does not exist."
        self.assertEqual(serializer.errors['choice_id'][0], expected_msg)
        self.assertEqual(Vote.objects.count(), 0)
    
    def test_choice_id_must_be_integer(self):
        invalid_data = {'choice_id': 'not_an_int'}
        serializer = VoteSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('choice_id', serializer.errors)
        self.assertIn("integer", serializer.errors['choice_id'][0].lower())
    