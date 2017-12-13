
from speech_recognition.voice_detection import voice_detection

def main():
    vi = voice_detection();
    while True:
        print (vi.get_text())

if __name__ == '__main__':
    main()
