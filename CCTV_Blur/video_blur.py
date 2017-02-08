import numpy as np
import cv2
import sys
debug = 1
def print_progress(count, total, suffix='Processing Frame'):
    sys.stdout.write('%s [%s of %s]\r' % (suffix, count, total))
    sys.stdout.flush()
def Init():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture('test.mp4')

    fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
    vout = cv2.VideoWriter()
    frame_size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), \
                  int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    print "Frame size: {0}\nFPS: {1}\nFrame Count: {2}".format(frame_size, fps, length)
    success = vout.open('output.mov', fourcc, fps, frame_size, True)
    return cap, vout, face_cascade, length
def BlurVideo(cap, vout, face_cascade, length):
    i = 0
    print_progress(i, length)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        result_image = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for(x, y, w, h) in faces:
            sub_face = frame[y:y+h, x:x+w]
            sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
            result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
        vout.write(result_image)
        i+=1
        print_progress(i, length)
        if debug is 1:
            cv2.imshow('Video', result_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print "Error..."

def Cleanup(cap, vout):
    cap.release()
    vout.release()
    vout = None
    cv2.destroyAllWindows()
def main():
    if debug is 1:
        print "Debug mode is on"
    cap, vout, face_cascade, length = Init()
    BlurVideo(cap, vout, face_cascade, length)
    Cleanup(cap, vout)
main()
