import math
def heighestPointOnfinalBuildingListuilding(finalBuildingListuilding):
    heighestPoint = None
    maxX = float('-inf')
 
    for vertex in finalBuildingListuilding:
        if vertex[0] >= maxX:  
            maxX = vertex[0]
            heighestPoint = vertex
 
    return heighestPoint

def locationOfSun(heighestPoint, sun):
    if heighestPoint[1]<sun[1]:
        return "Up"
    elif heighestPoint[1]>sun[1]:
        return "Down"
 
def lengthOfLine(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
 
def intersectionPointOfTwoLines(line1, line2):

    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
 
    if x2 != x1 and x4 != x3:  
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
 
        if m1 == m2:
            return None  
 
        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3
 
        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1
 
    elif x2 == x1 and x4 == x3:  
        if x1 != x3:
            return None  
 
        y_min = min(y1, y2, y3, y4)
        y_max = max(y1, y2, y3, y4)
        y = (y_min + y_max) / 2
        x = x1
 
    else:  
        if x2 == x1:  
            m2 = (y4 - y3) / (x4 - x3)
            c2 = y3 - m2 * x3
            x = x1
            y = m2 * x1 + c2
        else: 
            m1 = (y2 - y1) / (x2 - x1)
            c1 = y1 - m1 * x1
            x = x3
            y = m1 * x3 + c1
 
    return x, y

def onVerticalEdge(line, point):
    if line[0][1] < line[1][1]:
        if line[0][1] < point[1] and line[1][1] > point[1]:
            return True
        return False
    else:
        if line[1][1] < point[1] and line[0][1] > point[1]:
            return True
        return False
 
 
def onHorizontalEdge(line, point):
    if line[0][0] < line[1][0]:
        if line[0][0] < point[0] and line[1][0] > point[0]:
            return True
        return False
    else:
        if line[1][0] < point[0] and line[0][0] > point[0]:
            return True
        return False

def lengthOfExposedWall(finalBuildingListuildings):
    totalLength = 0
    flag = 1
    count = 0
    for finalBuildingListuilding in finalBuildingListuildings:
 
        if locationOfSun(finalBuildingListuilding[0],sun)== "Up" and count==0:
            length = lengthOfLine(finalBuildingListuilding[1][0],finalBuildingListuilding[1][1])
            width = lengthOfLine(finalBuildingListuilding[1][1],finalBuildingListuilding[1][2])
            totalLength += length + width
            count+=1
 
        elif locationOfSun(finalBuildingListuilding[0],sun)== "Down" and  count==0:
            length = lengthOfLine(finalBuildingListuilding[1][0],finalBuildingListuilding[1][1])
            width = 0
            totalLength += length + width
            count+=1
 
        elif locationOfSun(finalBuildingListuilding[0],sun)== "Up" and flag==1 and count ==1 :
            previousfinalBuildingListuildingIndex = finalBuildingListuildings.index(finalBuildingListuilding)-1
            ray = [sun,finalBuildingListuildings[previousfinalBuildingListuildingIndex][1][0]]
            verticalEdge = [finalBuildingListuilding[1][2],finalBuildingListuilding[1][3]]
            HorizontalEdge = [finalBuildingListuilding[1][0],finalBuildingListuilding[1][3]]
 
            vertical = intersectionPointOfTwoLines(ray,verticalEdge)
            horizontal = intersectionPointOfTwoLines(ray,HorizontalEdge)
 
            if onVerticalEdge(verticalEdge,vertical):
                length =  afinalBuildingLists(lengthOfLine(verticalEdge[0],vertical))
                width = lengthOfLine(finalBuildingListuilding[1][1],finalBuildingListuilding[1][2])
                totalLength += length + width
            else:
                if verticalEdge[1][1] > vertical[1]:
                    length =  afinalBuildingLists(lengthOfLine(verticalEdge[0],verticalEdge[1]))
                    width = lengthOfLine(finalBuildingListuilding[1][1],finalBuildingListuilding[1][2])
                    totalLength += length + width
                else :
                    if onHorizontalEdge(HorizontalEdge,horizontal):
                        width = lengthOfLine(horizontal,HorizontalEdge[0])
                        totalLength += width
       
        elif locationOfSun(finalBuildingListuilding[0],sun)== "Down" and flag==1 and count ==1 :
            previousfinalBuildingListuildingIndex = finalBuildingListuildings.index(finalBuildingListuilding)-1
            ray = [sun,finalBuildingListuildings[previousfinalBuildingListuildingIndex][1][3]]
            verticalEdge = [finalBuildingListuilding[1][2],finalBuildingListuilding[1][3]]
            HorizontalEdge = [finalBuildingListuilding[1][0],finalBuildingListuilding[1][3]]
 
            vertical = intersectionPointOfTwoLines(ray,verticalEdge)
            horizontal = intersectionPointOfTwoLines(ray,HorizontalEdge)
 
            if onVerticalEdge(verticalEdge,vertical):
                length =  afinalBuildingLists(lengthOfLine(verticalEdge[0],vertical))
                width = 0
                totalLength += length + width
    return totalLength

if __name__ == "__main__":
    listOffinalBuildingListuilding =  [[[18,8],[18,0],[20,0],[20,8]],[[6,4],[6,0],[12,0],[12,4]],[[2,3],[2,0],[5,0],[5,3]]]
    finalBuildingList = []
    sun = [25,10]
    for finalBuildingListuilding in listOffinalBuildingListuilding:
        heighestPoint = heighestPointOnfinalBuildingListuilding(finalBuildingListuilding)
        finalBuildingList.append([heighestPoint,finalBuildingListuilding])
    totalLength = lengthOfExposedWall(finalBuildingList)
       
    print(totalLength)