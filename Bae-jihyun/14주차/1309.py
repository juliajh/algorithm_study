'''
접근1 : 완전 탐색
N: 100,000
한 행에 사자가 최대 1마리 있을 수 있다.
한 행에는 사자가 없는 경우, 있는 경우로 2가지 경우가 있고 행의 갯수인 N입력이 들어왔을때 시간복잡도는 2^100,000이다. (탈락)
참고 ) 윗 행에 사자가 있을 시 현재 행의 사자 자리는 이미 정해져 있기 때문에 있다, 없다 2가지 경우이고
      윗 행에 사자가 없을 시 현재 행의 사자 자리는 없다, 왼쪽칸, 오른쪽칸으로 3가지 경우이다.
      사자의 위치가 2가지일때도 시간복잡도가 매우 크므로 3가지일때는 고려하지 않는다.


접근2 : DP
N번째 행이 추가되면 N-1번째 행까지의 값에 N번째 행이 추가되는 계산만 해주면 되므로 O(n), DP로 풀 수 있다.

dp[i][0] : 윗 행의 사자가 오른족에 있거나 없으면 가능. 오른족에 있거나 없을 경우를 더한 경우의 수
dp[i][1] : 윗 행의 사자가 왼쪽에 있거나 없으면 가능. 왼쪽에 있거나 없을 경우를 더한 경우의 수
dp[i][2] : 윗 행의 사자가 오른족에 있어도, 왼쪽에 있어도, 혹은 없어도 가능
'''

N = int(input())
dp = [[1]*3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2]) % 9901    # 사자가 왼쪽 칸에 있을 경우의 수
    dp[i][1] = (dp[i-1][0]+dp[i-1][2]) % 9901    # 사자가 오른쪽 칸에 있을 경우의 수
    dp[i][2] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]) % 9901    # 사자가 없을 경우의 수

print(max(dp[N]))


'''
배열을 N까지가 아니라 N+1번째의 max값을 구해야하는 이유를 몰랐는데 N을 1로 설정해보니 이해가 갔다.
N번째까지의 합을 구하기 위해 N+1에서 N번째 경우의 수들을 다 더해준다.
'''
