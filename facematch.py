# comparing images and predicting the match.

import face_recognition
image_of_bill=face_recognition.load_image_file('./img/known/Bill Gates.jpg')
# now we need to get the facial feature of the image to compare with other images.
# so v use face_encodings().it wil give a list. so to convert this to an numpy array
# we set the index 0. since we cannot compare two list, bt can compare two arrays.
bill_face_encoding=face_recognition.face_encodings(image_of_bill)[0]

# now load an unknown image and get the facial fetaure of it
unknown_image=face_recognition.load_image_file('./img/unknown/keanu-reeves-2000.jpg')
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

# compare faces.to do it there is a meethod called compare_faces().
# two args: encoding of known face is passed in brackets ie bill_face_encoding.
# and second is unknown face encoding.
result=face_recognition.compare_faces([bill_face_encoding],unknown_face_encoding)
# gonna give a true or fale value in brackets.

if result[0]: 
    # result[0] removes the brackets from boolean values
    print('This is Bill Gates')
else:
    print('This is NOT Bill Gates')



    