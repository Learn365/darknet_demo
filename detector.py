# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb
import cv2

cfg_file = b'./cfg/nlut.cfg'
obj_file = b'cfg/nlut.data'
weights = b'./backup/nlut_10000.weights'
# folder = '/home/peter/Pictures'
test_file=b'./nlut_test.jpg'
result_file=b'./result_nlut_test.jpg'
thresh  = 0.25

dn.set_gpu(0)
net = dn.load_net(cfg_file, weights, 0)
meta = dn.load_meta(obj_file)
try:
    r = dn.detect(net, meta, test_file)
    print (r) #list of name, probability, bounding box center x, center y, width, height

    img = cv2.imread(test_file,cv2.IMREAD_COLOR) #load image in cv2
    new_path=result_file
    while i<len(res):
        res_type=r[i][0]
        if "1" in res_type:
            #copy file to person directory
            # new_path = '/home/peter/Pictures/person/'+f
            #set the color for the person bounding box
            box_color = (0,255,0)
        elif "2" in res_type:
            # new_path = '/home/peter/Pictures/cat/'+f
            box_color = (0,255,255)
        elif "3" in res_type:
            # new_path = '/home/peter/Pictures/bird/'+f
            box_color = (255,0,0)
        elif "4" in res_type:
            # new_path = '/home/peter/Pictures/squirrel/'+f
            box_color = (0,0,255)
        elif "5":
            box_color = (255,255,0)

        #get bounding box
        center_x=int(r[i][2][0])
        center_y=int(r[i][2][1])
        width=int(r[i][2][2])
        height=int(r[i][2][3])

        UL_x=int(center_x-width/2)  #Upper left corner X coord
        UL_y=int(center_y+height/2) #Upper left y
        LR_x=int(center_x+width/2)
        LR_y=int(center_y-height/2)

        #write bounding box to image
        cv2.rectangle(img, (UL_x,UL_y),(LR_x,LR_y),box_color,1)
        #put label on bounding box
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,res_type,(center_x,center_y),font,2,box_color,2,cv2.LINE_AA)
        i=i+1
    cv2.imwrite(new_path,img) #wait until all the objects are marked and then write out.
#todo. This will end up being put in the last path that was found if there were multiple
#it would be good to put it all the paths.
except ValueError as err:
    print (err)

# And then down here you could detect a lot more images like:
# r = dn.detect(net, meta, "data/eagle.jpg")
# print r
# r = dn.detect(net, meta, "data/giraffe.jpg")
# print r
# r = dn.detect(net, meta, "data/horses.jpg")
# print r
# r = dn.detect(net, meta, "data/person.jpg")
# print r

