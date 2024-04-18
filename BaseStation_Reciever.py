import cv2
import requests
import numpy as np

def receive_stream(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        bytes_data = bytes()
        for chunk in r.iter_content(chunk_size=1024):
            bytes_data += chunk
            a = bytes_data.find(b'\xff\xd8')
            b = bytes_data.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_data[a:b+2]
                bytes_data = bytes_data[b+2:]
                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                if frame is not None:
                    cv2.imshow('Video Stream', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_url = 'http://localhost:5000/video'
    receive_stream(video_url)