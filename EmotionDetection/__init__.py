from .emotion_detection import emotion_detector

# Convenience function with faster defaults for testing
def quick_emotion_detector(text):
    return emotion_detector(text, timeout=3, retries=0, allow_offline=True)

__all__ = ["emotion_detector", "quick_emotion_detector"]