from PIL import Image,ImageDraw
import face_recognition

# need to do face match so load the image of both from known folder .
bill_image=face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding=face_recognition.face_encodings(bill_image)[0]

steve_image=face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding=face_recognition.face_encodings(steve_image)[0]

# create an array of encodings and names.
known_face_encoding=[
    bill_face_encoding,
    steve_face_encoding
]
known_face_names=[
    "Bill Gates",
    "Steve Jobs"
]

# load test image to find the faces in it.
# test image contains both faces.
test_image=face_recognition.load_image_file("./img/groups/bill-steve-elon.jpg")

#find all the faces in the test images.
face_locations=face_recognition.face_locations(test_image)
# now v get the coordinates of all faces in test_image

# get the face encodings of test image and pass face_locations
test_image_encodings=face_recognition.face_encodings(test_image,face_locations)


# convert to PILLOW format.
pil_image=Image.fromarray(test_image)

# create an ImageDraw Instance to draw on top of the image.
draw=ImageDraw.Draw(pil_image)

# Loop thru each faces in the test_image.
for(top,right,bottom,left),test_image_encodings in zip(face_locations,test_image_encodings): 
    # for each iteration v have access to the coordinates and encodings of a face
     matches=face_recognition.compare_faces(known_face_encoding,test_image_encodings)

    # if there is no match,set
     name='Unknown Person'
    #  if match,ie if there is steve or bill in this image.
     if True in matches:
         first_match_index=matches.index(True)
         name=known_face_names[first_match_index]
    
    #  draw box around the face 
    # ins first box, use rectangle() method of imagedraw and pass two args, ie pair of cordinates 
    #  to draw boundarie and another is outline where v set rgb color.
     draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

    #  draw the label. ie a rectangle box and name inside it
    # use textsize() method  which return image size in pixels ie its width and height. 
     text_width, text_height = draw.textsize(name) 
     draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,255), 
     outline=(0,0,255))

    #  draw the text
     draw.text((left+6, bottom-text_height-5),name,fill=(255,255,255,255))

# delete the draw instance
del draw
# next show the final image
pil_image.show()
pil_image.save('final.jpg')




     

     
          