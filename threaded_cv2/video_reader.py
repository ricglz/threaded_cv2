'''Threaded cv2 VideoCapture'''
from queue import Queue
import os
import threading

import cv2

class VideoCapture:
    buffer = Queue(1024)
    end_frame = 0
    last_frame = 0
    stopped = False
    thread = None

    def __init__(self, video_path):
        if video_path is None:
            raise Exception("VideoReader:: Video reader needs a videoPath!")
        if not os.path.exists(video_path):
            raise Exception("VideoReader:: Provided video path does not exist")

        self.cap = cv2.VideoCapture(video_path)
        self.calc_fps()

    def __exit__(self, type, value, traceback):
        self.stop()

    def stop(self):
        '''Stops reading the video and realeases the VideoCapture'''
        self.thread.join()
        self.cap.release()

    def __enter__(self):
        self._fill_buffer()
        return self

    def start(self):
        '''Starts to fill up the buffer'''
        self._fill_buffer()

    def _fill_buffer(self):
        self.end_frame = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.thread = threading.Thread(target=self.read_frames, args=())
        self.thread.start()

    def read_frames(self):
        '''Reads video from start to finish'''
        while self.last_frame < self.end_frame:
            res, frame = self.cap.read()
            if res:
                self.buffer.put(frame)
            self.last_frame += 1

        self.stopped = True

    @property
    def video_ended(self):
        """Checks if there's no more frames to read"""
        return self.stopped and self.buffer.empty()

    def pop(self):
        '''Gets the next frame'''
        return self.buffer.get(block=True)

    def __iter__(self):
        while not self.video_ended:
            yield self.pop()

    def calc_fps(self):
        '''Calculates the fps of the video'''
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        return self.fps

    def get_fps(self):
        '''Gets the fps of the video'''
        if self.fps is None:
            self.calc_fps()
        return self.fps
