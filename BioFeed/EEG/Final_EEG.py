''''
100 Errrors
Requuire Lot of Debugging
1st attempt
'''
import csv
import numpy as np
import scipy.spatial as ss
import scipy.stats as sst
import platform
import socket

import gevent
import threading
import statistics

from scipy.signal import butter, lfilter
from sklearn import preprocessing

sampling_rate = 128  #In hertz
number_of_channel = 14
realtime_eeg_in_second = 5 #Realtime each ... seconds
number_of_realtime_eeg = sampling_rate*realtime_eeg_in_second
socket_port = 8080

class RealtimeEmotion(object): 
    """
    Receives EEG data realtime, preprocessing and predict emotion.
    """

    # path is set to training data directory
    def __init__(self, path="../Training Data/"): 
            """
            Initializes training data and their classes.
            """
            self.train_arousal = self.get_csv(path + "train_arousal.csv")
            self.train_valence = self.get_csv(path + "train_valence.csv")
            self.class_arousal = self.get_csv(path + "class_arousal.csv")
            self.class_valence = self.get_csv(path + "class_valence.csv")
            self.data = self.get_csv(path+"databaseTest14.csv")

    def get_csv(self,path): 
            """
            Get data from csv and convert them to numpy python.
            Input: Path csv file.
            Output: Numpy array from csv data.
            """
            #Get csv data to list
            file_csv = open(path)
            data_csv = csv.reader(file_csv)
            data_training = np.array([each_line for each_line in data_csv])

            #Convert list to float
            data_training = data_training.astype(np.double)

            return data_training

    def butter_bandpass(self,lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def butter_bandpass_filter(self,data, lowcut, highcut, fs, order=5):
        b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y
    """

    def do_fft(self,all_channel_data): 
            data_fft = map(lambda x: np.fft.fft(x),all_channel_data)

            return data_fft
    """

    def get_frequency(self,all_channel_data): 
            """
            Get frequency from computed fft for all channels. 
            Input: Channel data with dimension N x M. N denotes number of channel and M denotes number of EEG data from each channel.
            Output: Frequency band from each channel: Delta, Theta, Alpha, Beta, and Gamma.
            """
            #Length data channel
            #all_channel_data = all_channel_data.T
            L = len(all_channel_data[0]) #L=14
            N=1023            
            Fs = 128
            X_raw= all_channel_data[:1023,:]
            X_raw = preprocessing.scale(X_raw)
            #X_raw1= butter_bandpass_filter(X_raw, 10,40, 128, 5);

            gamma= self.butter_bandpass_filter(X_raw, 30 ,60,128, 5);
            beta= self.butter_bandpass_filter(X_raw, 14, 30 ,128, 5);
            delta= self.butter_bandpass_filter(X_raw, 0.5, 4 ,128, 5);
            alpha= self.butter_bandpass_filter(X_raw, 8, 14 ,128, 5);
            theta= self.butter_bandpass_filter(X_raw, 4, 8 ,128, 5);


            """
            #Get fft data
            data_fft = self.do_fft(all_channel_data)

            #Compute frequency
            frequency = map(lambda x: abs(x/L),data_fft)


            frequency = map(lambda x: x[: (int)(L/2+1)]*2,frequency)
            #frequency = map(lambda x: x[: 4]*2,frequency)              
            """

            """
            #List frequency
            delta = map(lambda x: x[int(L*1/Fs-1): int(L*4/Fs)],frequency)
            theta = map(lambda x: x[int(L*4/Fs-1): int(L*8/Fs)],frequency)
            alpha = map(lambda x: x[int(L*5/Fs-1): int(L*13/Fs)],frequency)
            beta = map(lambda x: x[int(L*13/Fs-1): int(L*30/Fs)],frequency)
            gamma = map(lambda x: x[int(L*30/Fs-1): int(L*50/Fs)],frequency)
            delta=list(map(list, zip(*delta))) #to find transpose
            theta=list(map(list, zip(*theta)))
            alpha=list(map(list, zip(*alpha)))
            beta=list(map(list, zip(*beta)))
            gamma=list(map(list, zip(*gamma)))
            print("////////////////////////////////////////")
            print(np.shape(list(delta)))
            print("////////////////////////////////////////")

            """

            return delta,theta,alpha,beta,gamma

    def get_feature(self,all_channel_data): 
        (delta,theta,alpha,beta,gamma) = self.get_frequency(all_channel_data)
        #Compute feature std
        delta_std = np.std(delta,axis=1)
        theta_std = np.std(theta,axis=1)
        alpha_std = np.std(alpha,axis=1)
        beta_std = np.std(beta,axis=1)
        gamma_std = np.std(gamma,axis=1)

        #Compute feature mean
        delta_m = np.mean(delta,axis=1)
        theta_m = np.mean(theta,axis=1)
        alpha_m = np.mean(alpha,axis=1)
        beta_m = np.mean(beta,axis=1)
        gamma_m = np.mean(gamma,axis=1)


        #Concate feature
        feature = np.array([delta_std,delta_m,theta_std,theta_m,alpha_std,alpha_m,beta_std,beta_m,gamma_std,gamma_m])
        feature = feature.T
        feature = feature.ravel()

        return feature

    def predict_emotion(self,feature):
            """
            Get arousal and valence class from feature.
            Input: Feature (standard deviasion and mean) from all frequency bands and channels with dimesion 1 x M (number of feature).
            Output: Class of emotion between 1 to 3 from each arousal and valence. 1 denotes low category, 2 denotes normal category, and 3 denotes high category.
            """
            l=np.shape(feature)
            distance_ar=np.zeros(l)
            #Compute canberra with arousal training data
            distance_ar = map(lambda x:ss.distance.canberra(x,feature),self.train_arousal)

            distance_va=np.zeros(l)
            #Compute canberra with valence training data
            distance_va = map(lambda x:ss.distance.canberra(x,feature),self.train_valence)
            print("//////////////////////////////////////////////////////")
            print(np.shape(list(distance_va)))

            #Compute 3 nearest index and distance value from arousal
            idx_nearest_ar = np.array(np.argsort(distance_ar, axis= None)[:3])
            val_nearest_ar = np.array(np.sort(distance_ar, axis= None)[:3])

            #Compute 3 nearest index and distance value from arousal
            idx_nearest_va = np.array(np.argsort(distance_va, axis= None)[:3])
            val_nearest_va = np.array(np.sort(distance_va, axis= None)[:3])
            print("//////////////////////////////////////////////////////")
            print(np.shape(val_nearest_ar))

            #Compute comparation from first nearest and second nearest distance. If comparation less or equal than 0.7, then take class from the first nearest distance. Else take frequently class.
            #Arousal
            comp_ar = val_nearest_ar[0]/val_nearest_ar[1]
            if comp_ar<=0.97:
                    result_ar = self.class_arousal[0,idx_nearest_ar[0]]
            else:
                    result_ar = sst.mode(self.class_arousal[0,idx_nearest_ar])
                    result_ar = float(result_ar[0])

            #Valence
            comp_va = val_nearest_va[0]/val_nearest_va[1]
            if comp_va<=0.97:
                    result_va = self.class_valence[0,idx_nearest_va[0]]
            else:
                    result_va = sst.mode(self.class_valence[0,idx_nearest_va])
                    result_va = float(result_va[0])

            return result_ar,result_va

    def determine_emotion_class(self,feature):
            """
            Get emotion class from feature.
            Input: Feature (standard deviasion and mean) from all frequency bands and channels with dimesion 1 x M (number of feature).
            Output: Class of emotion between 1 to 5 according to Russel's Circumplex Model.
            """
            class_ar,class_va = self.predict_emotion(feature)

            if class_ar==2.0 or class_va==2.0:
                    emotion_class = 5
            elif class_ar==3.0 and class_va==1.0:
                    emotion_class = 1
            elif class_ar==3.0 and class_va==3.0:
                    emotion_class = 2
            elif class_ar==1.0 and class_va==3.0:
                    emotion_class = 3
            elif class_ar==1.0 and class_va==1.0:
                    emotion_class = 4

            return emotion_class

    def process_all_data(self,all_channel_data):
            """
            Process all data from EEG data to predict emotion class.
            Input: Channel data with dimension N x M. N denotes number of channel and M denotes number of EEG data from each channel.
            Output: Class of emotion between 1 to 5 according to Russel's Circumplex Model. And send it to web ap

            """
            print("ALLL channel")
            print(all_channel_data)
            #Get feature from EEG data
            feature = self.get_feature(all_channel_data)

            #Predict emotion class
            emotion_class = self.determine_emotion_class(feature)

            #send emotion_class to web app
            self.send_result_to_application(emotion_class)

    def send_result_to_application(self,emotion_class):
            """
            Send emotion predict to web app.
            Input: Class of emotion between 1 to 5 according to Russel's Circumplex Model.
            Output: Send emotion prediction to web app.
            """
            socket =  SocketIO('localhost', socket_port, LoggingNamespace)
            socket.emit('realtime emotion',emotion_class)

    def main_process(self):
            emotion_class_2 = self.process_all_data(self.data)
            print ("emotion_class")
            #print (emotion_class)

if __name__ == "__main__":
    rte = RealtimeEmotion()
    rte.main_process()
