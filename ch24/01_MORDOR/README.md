# 1. 등산로

#### 문제

모르도르 지방의 [아름다운 경치](http://en.wikipedia.org/wiki/Mordor#Geography)를 한 눈에 볼 수 있는 명산 [오로드루인](http://en.wikipedia.org/wiki/Orodruin#Adaptations)에는 길기로 유명한 등산로가 있습니다. 이 등산로는 산등성이를 따라 오르락내리락하며 구성되어 있지요. 이 등산로는 너무 길기 때문에 특수 장비(예를 들면, [절대반지](http://en.wikipedia.org/wiki/One_Ring) 등)를 갖춘 사람이 아니라면 처음부터 끝까지 정복하기가 힘이 듭니다. 관광 자원 개척을 위해 이 등산로 중 몇 군데를 별도의 등산로로 개방하려고 합니다.

등산로에는 100미터 간격으로 표지판이 있는데, 각 표지판의 해발 고도를 측정한 자료가 있습니다. 이 때 등산로의 난이도는 등산로를 가다 만나는 표지판 중 최대 해발 고도와 최저 해발 고도의 차이입니다. 개방을 검토하고 있는 등산로의 일부가 주어질 때, 각 부분의 난이도를 계산하는 프로그램을 작성하세요.



#### 입력

입력의 첫 줄에는 테스트 케이스의 수 C (1 <= C <= 30) 가 주어집니다. 각 테스트 케이스의 첫 줄에는 원래 등산로에 있는 표지판의 수 N (1 <= N <= 100,000)과 개방을 고려하고 있는 등산로의 수 Q (1 <= Q <= 10,000)가 주어집니다. 그 다음 줄에 N 개의 정수로 각 표지판의 해발 고도 hi 가 순서대로 주어집니다. (0 <= hi <= 20,000) 각 표지판은 입력에 주어지는 순서대로 0 번부터 N-1 번까지 번호가 매겨져 있습니다. 그 다음 Q 줄에 각 2개의 정수로 개방을 고려하고 있는 등산로의 첫 번째 표지판과 마지막 표지판의 번호 a , b (0 <= a <= b < N) 가 주어집니다.

**입력 데이터의 양이 많으니 가능한 빠른 입출력 방법을 사용하시기 바랍니다.**



#### 출력

한 줄에 하나씩 개방을 고려하고 있는 각 등산로의 난이도를 출력합니다.



#### 예제 입력

```
2
3 1
1 2 3
0 2
10 4
3 9 5 6 10 8 7 1 2 4 
1 6
4 7
9 9
5 8
```



#### 예제 출력

```
2
5
9
0
7
```

