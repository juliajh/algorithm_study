import sys

direction=[(0,-1),(0,1),(-1,0),(1,0)]  #방향성

def calc(result, lst, m,n,x,y):
    if x ==m-1 and y ==n-1:             #오른쪽 맨아래(마지막지점) 근처 좌표라면
        result[x][y]=1                  #마지막 지점으로 가는 길은 1임.
        return
    if result[x][y]!=-1:                #계산한 적 있으면 다시 계산하지않게.
        return
    result[x][y] =0                     #계산한 적 없으면 지나갔다는 표시로 0(-1이 아닌 수)
    for dx,dy in direction:             #방향 확인 
        nx=x+dx                         #다음 x좌표구하기
        ny=y+dy                         #다음 y좌표구하기
        if 0<=nx<m and 0<=ny<n:         #다음 x,y좌표가 유효한지(m,n보다 큰 인덱스인지)
            if(lst[x][y]> lst[nx][ny]):  #현재 좌표와 다음 좌표 값비교 (현재보다 낮은 길일때만)
               calc(result, lst, m,n,nx,ny)   #다음 좌표도 똑같이 계산
               result[x][y] +=result[nx][ny]  #갈 수 있는 방향의 점이 가진 값(마지막지점으로 갈 수 있는 길 갯수)을 더해줌.
               


m, n = map(int, input().split())

lst=[]                              #원본 데이터 넣을 공간 
for i in range(m):                 #데이터 받기 
    put= list(map(int, input().split()))
    lst.append(put)


result = [[-1]*n for i in range(m)] #빈 배열 만들기(아직 방문하지 않았다는 뜻: -1)
calc(result, lst, m,n,0,0)          #(0,0)에 대한 계산
print(result[0][0])



#알고리즘
#마지막 지점근처부터 마지막지점으로 갈 수 있는 길의 수를 구한다.
#한 점의 4개의 방향의 숫자를 다 더해준다.
#첫번째 좌표 오른쪽과 아래 인덱스의 값을 더해준다. 

"""
피드백 코멘트 :
잘 푸셨습니다! 변수명이나 구조들이 제가 푸는 스타일하고 거의 똑같아서 신기하네요 ㅋㅋ
지금 calc 함수에 인자가 6개가 전달되고 있습니다. 몇 개는 줄여볼 수 있을 것 같네요.
인자가 많은 함수는 대체로 바람직하지 않으며, 풀이하는 본인조차도 가끔 사용할때 실수할 수 있습니다.
이 문제는 인자를 2개까지 줄여볼 수 있을 듯 하니 고민해보셔도 좋은 공부가 될 것 같네요.
"""