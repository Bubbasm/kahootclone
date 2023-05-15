from models.test_models import ModelTests
from models.test_authentication import ServiceBaseTest
from models.models import User
from django.urls import reverse


NUMBERUSERS = 5
SIGNUP_SERVICE = "signup"


class AdditionalTestModels(ModelTests):
    '''
    Tests for 100% coverage.
    '''
    def test001_questionnaire_url(self):
        '''
        Test that the url of a questionnaire is correct.
        @author: Bhavuk Sikkas
        '''
        questionnaire = self.createQuestionnaire(check=True)

        self.assertEqual(questionnaire.get_absolute_url(),
                         '/services/questionnaire/'+str(questionnaire.id))


class AdditionalTestAuthentication(ServiceBaseTest):
    '''
    Tests for 100% coverage.
    '''

    def test001_signup_fail(self):
        '''
        Check signup with wrong password confirmation
        @author: Bhavuk Sikka
        '''
        # check signup with wrong password2
        i = NUMBERUSERS
        user = {"username": "user_%d" % i,
                "first_name": "name_%d" % i,
                "last_name": "last_%d" % i,
                "email": "email_%d@gmail.com" % i,
                "password": 'trekingff0',
                "password1": 'trekingff1',
                "password2": 'trekingff2'}
        self.assertFalse(
            User.objects.filter(username=user["username"]).exists())
        # send signup request
        self.client1.post(reverse(SIGNUP_SERVICE), user, follow=True)
        # check the user has not been created
        self.assertFalse(
            User.objects.filter(username=user["username"]).exists())

    def test002_signup_page(self):
        '''
        Check get method in the signup page
        @author: Bhavuk Sikka
        '''
        # test get method in the signup page
        response = self.client1.get(reverse(SIGNUP_SERVICE), follow=True)
        self.assertEqual(response.status_code, 200)
