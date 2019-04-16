# import face_recognition library
import face_recognition
# load_image_file() method loads image file as a numpy.ndarray.
image=face_recognition.load_image_file("./img/groups/team1.jpg")
# locations of each face. use face_locations() mthod and pass image as arg
face_location=face_recognition.face_locations(image)
# now v get list of coordinates of each face in image
# ie(top,right,bottom,left)
# print(face_location)
# to get no of people use,len()
print(f'there are {len(face_location)} people in the image')