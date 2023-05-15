from models.constants import QUESTION
from restServer.tests import GAME_DETAIL, GUESS_LIST, PARTICIPANT_LIST
from restServer.tests import RestTests
from rest_framework import status
from rest_framework.reverse import reverse
import uuid
import json

GAME_NOT_EXIST = "Game does not exist"


class AdditionalTestAPI(RestTests):
    '''
    Tests for 100% coverage.
    '''

    def test001_testParticipantCreate(self):
        '''
        Test that the ParticipantCreateView is working correctly.
        @author: Bhavuk Sikka
        '''
        url = reverse(PARTICIPANT_LIST)
        # let us add another participants with the same alias
        data = {'game': self.gameDict['publicId']+1,
                'alias': "luis"}
        response = self.client.post(url, data, format='json')
        responseJson = json.loads(self.decode(response.content))
        # convert response from bytes to json
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(responseJson['error'], GAME_NOT_EXIST)

        # game already started
        # start game
        self.game.state = 2
        self.game.save()
        data = {'game': self.gameDict['publicId'],
                'alias': "luis"}
        response = self.client.post(url, data, format='json')
        responseJson = json.loads(self.decode(response.content))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test002_testParticipantList(self):
        '''
        Test that the ParticipantListView is forbidden
        @author: Bhavuk Sikka
        '''
        url = reverse(PARTICIPANT_LIST)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test003_testGuessCreate(self):
        '''
        Test that the GuessCreateView is working correctly upon recreation of
        the same guess by the same participant.
        @Author: Bhavuk Sikka
        '''
        url = reverse(GUESS_LIST)
        self.game.questionNo = self.game.questionNo + 1
        self.game.save()
        # create a guess with a participant that does not exist
        data = {
            'uuidp': uuid.uuid1(),
            'game': self.gameDict['publicId'],
            'answer': 0,
        }
        self.game.state = QUESTION
        self.game.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # create a guess with an answer that does not exist
        data = {
            'uuidp': self.participant.uuidP,
            'game': self.gameDict['publicId'],
            'answer': 4,
        }
        self.game.state = QUESTION
        self.game.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test004_testGuessList(self):
        '''
        Test that the GuessListView is forbidden
        @author: Bhavuk Sikka
        '''
        url = reverse(GUESS_LIST)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test005_testGameAnswerCount(self):
        '''
        Test that the answer count is working correctly on edge cases.
        @author: Bhavuk Sikka
        '''
        url = reverse(GAME_DETAIL, args=[self.gameDict['publicId']])
        self.game.questionNo = self.game.questionNo + 100  # not existant
        self.game.save()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['answerCount'], 0)
