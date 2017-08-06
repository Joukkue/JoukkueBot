from main import handle
import unittest
import telepot
from tests.testMessages import *
from code.help import getHelp
from resources.archive import *
from code.compare import *
from code.uptime import *

bot = telepot.Bot(joukkueBot)

class BotTests(unittest.TestCase):
    def testHelp(self):
        asd = handle(msg1)
        self.assertEqual(asd, getHelp(bot, msg1))

    def testTuli1(self):
        value = Comparing(msg2['text']).is_tuli()
        self.assertEqual(value, True)

    def testTuli2(self):
        value = Comparing(msg3['text']).is_tuli()
        self.assertEqual(value, False)

    def testKalja1(self):
        value = Comparing(msg3['text']).is_kalja()
        self.assertEqual(value, True)

    def testKalja2(self):
        value = Comparing(msg2['text']).is_kalja()
        self.assertEqual(value, False)

    def testTissit1(self):
        value = Comparing(msg4['text']).is_tissit()
        self.assertEqual(value, True)

    def testTissit2(self):
        value = Comparing(msg3['text']).is_tissit()
        self.assertEqual(value, False)

    #def testUptime(self):
        #self.assertEqual(handle(msg5), upTime(bot, msg5))