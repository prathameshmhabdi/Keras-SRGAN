import cv2


for i in range(22):
	img=cv2.imread("high_res_result_image_"+str(i)+".png")
	frame.append(img)


out=cv2.VideoWriter(video.avi,cv2.VideoWriter_fourcc(*'DIVX'),1,(640,480))

for i in range(22)
	out.write(frame[i])

out.release()
