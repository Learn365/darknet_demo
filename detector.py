# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb
import cv2

dn.set_gpu(0)
net = dn.load_net(b'cfg/demo.cfg', b'backup/demo_10000.weights', 0)
meta = dn.load_meta(b'cfg/demo.data')
r = dn.detect(net, meta, b'test.jpg')
print (r)
img = cv2.imread('./test.jpg',cv2.IMREAD_COLOR) #load image in cv2
new_path='./test_result.jpg'
center_x=int(r[0][2][0])
center_y=int(r[0][2][1])
width=int(r[0][2][2])
height=int(r[0][2][3])

UL_x=int(center_x-width/2)  #Upper left corner X coord
UL_y=int(center_y+height/2) #Upper left y
LR_x=int(center_x+width/2)
LR_y=int(center_y-height/2)
box_color=(0,255,0)
cv2.rectangle(img, (UL_x,UL_y),(LR_x,LR_y),box_color,1)
res_type=r[0][0]
cv2.imwrite(new_path,img)
# And then down here you could detect a lot more images like:
# r = dn.detect(net, meta, "data/eagle.jpg")
# print r
# r = dn.detect(net, meta, "data/giraffe.jpg")
# print r
# r = dn.detect(net, meta, "data/horses.jpg")
# print r
# r = dn.detect(net, meta, "data/person.jpg")
# print r

