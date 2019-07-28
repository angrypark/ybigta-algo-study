## 1. A vs B

`A = [1,7,3,5], B = [0,6,4,2]` 와 같은 정수 배열이 두개 있다.

배열의 순서는 마음대로 바꿔도 된다고 가정하고, `max count(B > A)` 가 몇인지 구하시오.



**Approach**

Note: 문제에 제시된 `A`,`B`로 보면 `count(B > A) == 0` 이다. 하지만 B의 순서를 바꿔 `A = [1,7,3,5]`, `B = [2,0,4,6]` 이렇게 만들게 되면, `count(B > A) == 3` 이고, 이것이 `max` 가 된다.



1. A,B에 대해 B > A를 행렬으로 표현하면 아래와 같이 나온다. 여기서 우리는 행과 열이 겹치지 않으면서 O를 최대한 많이 골라야 한다.

|       |   1   |   7   |   3   |   5   |
| :---: | :---: | :---: | :---: | :---: |
| **0** |   X   | **X** |   X   |   X   |
| **6** |   O   |   X   |   O   | **O** |
| **4** |   O   |   X   | **O** |   X   |
| **2** | **O** |   X   |   X   |   X   |

2. 생각해보니 칸을 고를때 O의 개수가 가장 작은 행부터 (= 자유도가 가장 낮은 행부터) 고르기 시작하면 될 것 같다. 그런데 한 행에 존재하는 O의 개수는 B 배열의 숫자가 클수록 많으므로, 그냥 배열을 sort 해서 보면 될 것 같다.

|       |   1   |   3   |   5   |   7   |
| :---: | :---: | :---: | :---: | :---: |
| **0** |   X   |   X   |   X   | **X** |
| **2** | **O** |   X   |   X   |   X   |
| **4** |   O   | **O** |   X   |   X   |
| **6** |   O   |   O   | **O** |   X   |

3. O가 없는 행은 무시해도 되고, 각 배열이 오름차순으로 정렬되어있기 때문에 `2 -> 4 -> 6`으로 갈수록 O의 개수가 많아진다. 따라서 순서대로 A의 가장 작은 숫자부터 매핑을 시켜주면 된다.



```cpp
#include <algorithm>
#include <string>
#include <vector>
#include <tuple>
#include <deque>

using D = std::deque<int>;

std::pair<D,D> sortedDeque(const std::vector<int>& a, const std::vector<int>& b)
{
    std::deque<int> A(a.begin(), a.end());
    std::deque<int> B(b.begin(), b.end());
    std::sort(A.begin(), A.end());
    std::sort(B.begin(), B.end());
    return {A, B};
}

int solution(std::vector<int> a, std::vector<int> b) {
    D A,B;
    std::tie(A, B) = sortedDeque(a, b);

    int answer = 0;
    for (int num : B) {
        if (num <= A[0]) {
            A.pop_back();
        } else {
            answer++;
            A.pop_front();
        }
    }
    return answer;
}
```







## 2. STF (Shortest Time First)

인풋으로 `[(t1, d1), (t2, d2), ...]` 와 같은 배열이 들어온다. 여기서 `t` 는 job이 들어온 시점을 의미하고, `d` 는 해당 job의 duration을 의미한다.

e.g., `[(0,3), (1,9), (2,6)]`.

이 때, job이 들어온 순서대로 (`1 -> 2 -> 3`) 일을 진행하게 되면 turnaround time per job은 $\frac{(3 - 0) + (12 - 1) + (18-2)}{3} = 10$ 이 된다. 하지만 만약 `1 -> 3 -> 2` 순으로 일을 진행한다면 turnaround time per job은 $\frac{3 + 7 + 17}{3} = 9$ 가 된다.

인풋이 주어졌을때, turnaround time per job의 최소값을 구하시오.



**Approach**

문제에 씌여있진 않지만 STF (shortest time first) 알고리즘 구현을 묻는 문제이다. 각 시점에 현재 큐에 들어와있는 태스크 중 가장 소요 시간이 작은 순서대로 일을 처리하면 된다.



```cpp
#include <algorithm>
#include <string>
#include <vector>
#include <queue>

class Eval
{
public:
    bool operator()(const std::vector<int> &lhs, const std::vector<int> &rhs) const
    {
        return lhs[1] > rhs[1];
    }
};

using Q = std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, Eval>;
using J = std::vector<std::vector<int>>;
using D = std::deque<std::vector<int>>;

void getBatch(int t, Q& queue, D& jobs)
{
    while (jobs.size() > 0 && jobs[0][0] <= t) {
        queue.push(jobs[0]);
        jobs.pop_front();
    }
}

int solution(J j) {
    D jobs(j.begin(), j.end());
    std::sort(jobs.begin(), jobs.end());

    Q queue;
    int answer = 0;

    int t = 0;
    int numJobs = jobs.size();
    while (jobs.size() > 0 || queue.size() > 0) {
        getBatch(t, queue, jobs);
        if (queue.empty()) {
            t++;
            continue;
        }

        auto work = queue.top();
        queue.pop();

        int start = work[0];
        int duration = work[1];

        answer += t + duration - start;
        t += duration;
    }

    return answer / numJobs;
}
```

