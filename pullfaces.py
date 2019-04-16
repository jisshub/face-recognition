# import image from PILLOW library
from PIL import Image
import face_recognition
# next load the image and get the location of each face

image=face_recognition.load_image_file('./img/groups/hotel.jpg')

face_location=face_recognition.face_locations(image)

for each_loc in face_location:
    top,right,bottom,left=each_loc
    face_image=image[top:right, bottom:left]
    # this will give us the face image in the form of an array
    # and thus using this array we can get the actual face using pillow library.
    # Image module has fromarray() where v pass array,so pass face_image as arg.
    pil_image=Image.fromarray(face_image)
    # show the image using show()
    # pil_image.show()

    # to save the images in seperate jpg files use save() 
    pil_image.save(f"{bottom}.jpg")
    







