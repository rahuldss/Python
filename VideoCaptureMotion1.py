import cv2, time, pandas
from datetime import datetime

first_frame=None
df=pandas.DataFrame(columns=["Start","End"])
status_list=[None,None]
times=[]
i=0

video = cv2.VideoCapture(0)

while True:
    check, frame=video.read()
    status=0 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray,(21,21),0)

    #Ignoring the first black frame
    if first_frame is None:
        first_frame=gray
        continue

    #calculate the difference
    delta_frame=cv2.absdiff(first_frame,gray)
    #Provides the threshold value, convert the diff. value less than 30 to black. 
    # if diff. is greater that 30 then convert pixels to white.
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
    
    (cnts, _) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue

        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())

    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("frame",frame)
    cv2.imshow("Capturing...",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("thresh",thresh_frame)

    key=cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print(times)
for i in range(0,len(times),2):
    df=df.append({'Start': times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")

#show times to Graph
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=100, width=500,responsive=True,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=q.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("VideoCaptureGraph.html")
show(p)