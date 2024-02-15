from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        result_1 = emotion_detector('I love working with Python')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_2 = emotion_detector('I hate working with Python')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        result_3 = emotion_detector('I am really mad about this')
        self.assertEqual(result_3['dominant_emotion'], 'anger')

unittest.main()