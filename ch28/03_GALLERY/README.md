# 3. 감시 카메라 설치

#### 문제

전세계의 유명한 인물화들을 모아 두는 미술관에 괴도 [콩](http://ko.wikipedia.org/wiki/홍진호)의 도전장이 날아들었습니다. [2](http://ko.wikipedia.org/wiki/홍진호)0[2](http://ko.wikipedia.org/wiki/홍진호)[2](http://ko.wikipedia.org/wiki/홍진호)년 [2](http://ko.wikipedia.org/wiki/홍진호)월 [2](http://ko.wikipedia.org/wiki/홍진호)일을 기념하여, 미술관에 전시된 인물화 중 하나의 얼굴을 [모 프로게이머](http://ko.wikipedia.org/wiki/홍진호)의 얼굴로 합성하겠다는 것입니다. 미술관의 관장을 맡고 있는 재하는 이와 같은 사태를 방지하기 위해 감시 카메라를 설치하기로 마음먹었습니다. 미술관은 여러 개의 갤러리와 이들을 연결하는 복도로 구성되어 있으며, 한 갤러리에 감시 카메라를 설치하면 이 갤러리와, 복도로 직접 연결된 갤러리들을 감시할 수 있습니다. 모든 갤러리를 감시하기 위해 필요한 최소 감시 카메라의 수는 몇 개일까요?

미술관은 한 번 관람한 갤러리를 다시 가기 위해서는 이전에 지나왔던 복도를 반드시 한 번 지나야 하는 구조로 설계되어 있으며, 모든 갤러리가 서로 연결되어 있지 않을 수도 있습니다.



#### 입력

입력의 첫 줄에는 테스트 케이스의 수 C (C <= 50) 가 주어집니다. 각 테스트 케이스의 첫 줄에는 미술관에 포함된 갤러리의 수 G (1 <= G <= 1000) 와 갤러리들을 연결하는 복도의 수 H (0 <= H < G) 가 주어집니다. 각 갤러리에는 0번부터 G-1 번까지의 고유 번호가 있습니다. 그 후 H 줄에 각 2개의 정수로 각 복도가 연결하는 두 갤러리의 번호가 주어집니다.



#### 출력

각 테스트 케이스마다 한 줄에 필요한 카메라의 최소 개수를 출력합니다.



#### 예제 입력

```
3
6 5
0 1
1 2
1 3
2 5
0 4
4 2
0 1
2 3
1000 1
0 1
```



#### 예제 출력

```
3
2
999
```

