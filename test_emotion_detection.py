import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    
    def test_joy(self):
        """Test that 'I am glad this happened' returns joy as dominant emotion"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        print(f"Joy test: {result}")
    
    def test_anger(self):
        """Test that 'I am really mad about this' returns anger as dominant emotion"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        print(f"Anger test: {result}")
    
    def test_disgust(self):
        """Test that 'I feel disgusted just hearing about this' returns disgust as dominant emotion"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        print(f"Disgust test: {result}")
    
    def test_sadness(self):
        """Test that 'I am so sad about this' returns sadness as dominant emotion"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        print(f"Sadness test: {result}")
    
    def test_fear(self):
        """Test that 'I am really afraid that this will happen' returns fear as dominant emotion"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
        print(f"Fear test: {result}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
