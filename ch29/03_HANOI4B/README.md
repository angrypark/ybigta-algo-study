# 3. 하노이의 탑

#### 문제

![Hanoi.jpg](http://algospot.com/media/judge-attachments/8cb6ad23fcf3eb42d978d8da99e9ace3/Hanoi.jpg)

하노이의 탑은 세 개의 기둥에 꽂혀 있는 N개의 원반을 가지고 하는 게임입니다. N개의 원반은 크기가 모두 다르며, 게임의 시작 때는 그림과 같이 맨 왼쪽의 기둥에 모두 크기 순서대로 꽂혀 있습니다. 게임의 목적은 모든 원반을 맨 오른쪽 기둥으로 옮기는 것입니다.

원반을 움직일 때는 다음과 같은 규칙을 따라야 합니다.

- 한 번에 한 개의 원반만을 움직일 수 있습니다. 원반을 기둥이 아닌 다른 곳에 내려놓거나, 원반을 하나 들고 있으면서 다른 원반을 움직일 수는 없습니다.
- 작은 원반 위에 큰 원반을 올려놓아서는 안 됩니다.

세 개의 기둥이 있을 때 하노이의 탑 문제에는 간단한 해법이 있음은 잘 알려진 사실입니다. 그러면 기둥이 네 개가 있으면 어떨까요? 네 개의 기둥에 원반들이 자유롭게 배치되어 있을 때, 모든 원반을 오른쪽 기둥으로 옮겨 놓기 위해 필요한 최소한의 움직임 수를 계산하는 프로그램을 작성하세요.



#### 입력

입력의 첫 줄에는 테스트 케이스의 수 C (C <= 50) 가 주어집니다. 각 테스트 케이스의 첫 줄에는 원반의 총 수 N (1 <= N <= 12) 이 주어집니다. 각 원반에는 작은 것부터 순서대로 1부터 N 까지 번호가 매겨져 있다고 합시다. 그 후 네 줄에는 맨 왼쪽 기둥부터 하나씩 기둥에 꽂힌 원반의 정보가 주어집니다. 각 줄의 첫 정수는 해당 기둥에 꽂혀 있는 원반의 개수를 나타내며, 그 후로는 각 원반의 번호가 맨 아래 꽂힌 원반부터 주어집니다.

입력에 주어진 원반의 배치에서 큰 원반이 작은 원반 위에 꽂혀 있는 경우는 없습니다.



#### 출력

각 테스트 케이스마다 모든 원반을 맨 오른쪽 기둥으로 옮겨 놓기 위한 최소 움직임의 수를 출력합니다. 항상 모든 원반을 맨 오른쪽 기둥으로 옮겨 놓을 수 있다고 가정해도 좋습니다.



#### 예제 입력

```
3
5
1 1
1 3
2 5 4
1 2
3
1 2
0
2 3 1
0
10
2 8 7
2 5 4
3 6 3 2
3 10 9 1 
```



#### 예제 출력

```
10
4
24
```

