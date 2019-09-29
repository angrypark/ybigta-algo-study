# 2. 어린이날

#### 문제

어린이집을 경영하는 [원석이](https://algospot.com/wiki/read/일루)는 어린이날을 맞아 어린이집에 다니는 N 명의 아이들에게 장난감을 나눠 주기로 마음먹었습니다. 모든 아이들에게 같은 수의 장난감을 주려고 했지만, 그 중 M(0 <= M < N)명의 욕심쟁이 어린이들은 모두 같은 개수의 장난감을 받으면 삐져 버립니다. 따라서 이 욕심쟁이 어린이들에게는 남들보다 장난감을 한 개씩 더 주기로 했습니다. 종교적인 이유로 인해, 아이들에게 나누어 주는 장난감의 총 수 C는 십진수로 썼을 때 특정 숫자만으로 구성되어야 합니다.

예산이 빠듯한 관계로 장난감을 가능한 적게 사려고 합니다. 위와 같은 조건을 만족하는 최소의 C를 계산하는 프로그램을 작성하세요. 단 모든 어린이가 최소 한 개는 장난감을 받아야 합니다.



#### 입력

입력의 첫 줄에는 테스트 케이스의 수 T(T <= 50)가 주어집니다. 각 테스트 케이스는 C에 사용할 수 있는 자릿수의 목록 D와 N, M (0 <= M < N <= 10000) 으로 주어집니다. 자릿수 목록은 최소 한 개의 숫자는 포함하며, 자릿수 목록에 한 숫자가 두 번 주어지는 일은 없습니다.



#### 출력

각 테스트 케이스마다 필요한 최소 장난감의 수를 출력합니다. 만약 모든 조건을 만족하는 장난감의 개수를 찾을 수 없을 경우, IMPOSSIBLE을 출력합니다.



#### 예제 입력

```
5
1 7 0
1 10 1 
0 7 3
345 9997 3333
35 9 8
```



#### 예제 출력

```
111111
11
IMPOSSIBLE
35355353545
35
```
