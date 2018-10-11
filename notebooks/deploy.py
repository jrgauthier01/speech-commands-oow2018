import numpy as np 
from json import loads, dumps
import pickle as pkl

import keras
from keras.models import load_model

import librosa

# Loading the Keras model from disk: 
model = load_model('./model1.hdf5')

# load the lookup dictionary: 
words_selected = pkl.load(open('./class_label_lookup.pkl','rb'))
# do a reverse lookup: 
words_selected = { value: key for key, value in words_selected.items() }

def predict(waveform): 
    """Given a waveform this function will predict the word that 
    was said. 
    
    Args: 
        - waveform (a json object) 
     
    Returns: 
        - prediction from the CNN model 
    
    """
    waveform = loads(waveform) 
    waveform = np.asarray(waveform) 
    max_size = 32
    mfcc = librosa.feature.mfcc(waveform, sr=16000, n_mfcc=20)
    mfcc = np.pad(mfcc, pad_width=((0, 0),(0, max_size-mfcc.shape[1])), mode='constant') 
    mfcc = mfcc.reshape(1,20,32,1)
    class_value = model.predict_classes(mfcc) 
    #print("what-you-said {}".format(words_selected[class_value[0]]))
    return {"what-you-said": words_selected[class_value[0]]}

        
if __name__ == "__main__":
    # cat, right, eight 
    files = ['../data/6b81fead_nohash_0.wav',\
             '../data/ff2b842e_nohash_2.wav',\
             '../data/ccb1266b_nohash_1.wav']
    for f in files:
        waveform, _ = librosa.load(f, mono=True, sr=None)
        predict(dumps(waveform.tolist())) 