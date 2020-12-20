import unittest
from HTMLTestRunner import HTMLTestRunner
from api.user_manager import UserManager
from setting import TEST_REPOET_PATH,LOGIN_INFO


if __name__ == '__main__':

    UserManager().login(LOGIN_INFO.get('username'), LOGIN_INFO.get('password'))

    suite = unittest.TestLoader().discover('./cases','test*.py')


    with open(TEST_REPOET_PATH,'wb') as f:

        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)