import face_recognition
import cv2
import numpy as np
from test1 import *
import json
import pandas as pd

#known_face_names,known_face_encodings1=faceimg()
def test():
    name_data=open('name.json',)
    known_face_names=json.load(name_data)
    f = h5py.File('model.h5')
    known_face_encodings = f['person'][:]
    
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    # Grab a single frame of video
    #ret, frame = video_capture.read()
    img = cv2.imread("ss.jpeg", 1)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
                face_names.append(name)
                
                # time show
                import datetime
                now = datetime.datetime.now()
                print ("Current date and time : ")
                time=(now.strftime("%Y-%m-%d %H:%M:%S"))
                print(time)
                with open('attendance.txt','a') as f:
                    f.write(time+'\n') 
                    
                    f.write(name+'\n')
                    with open('display.txt','a') as f:
                        f.write(time+'\n') 
                        
                        f.write(name+'\n')
    account = pd.read_csv("display.txt",delimiter = '/')
    account.to_csv('display.csv',index = None)
            #time.sleep(10)

    process_this_frame = not process_this_frame


# Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        
        # Draw a label with a name below the face
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        print(name)
        
        # Display the resulting image
        cv2.imshow('img',img)
   

# Hit 'q' on the keyboard to quit!
