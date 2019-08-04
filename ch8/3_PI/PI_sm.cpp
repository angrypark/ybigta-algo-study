#ifdef __linux__
#include <bits/stdc++.h>
#else
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#endif

std::string getStr()
{
    std::string s;
    std::getline(std::cin, s);
    return s;
}

int getInt()
{
    return std::stoi(getStr());
}

class Solution
{
private:
    const int BIG_INT = 99999;
    int cache[10000];
    std::string seq;

    bool isRepeating(int start, int len)
    {
        char c = seq[start];
        for (int i = 1; i < len; i++)
            if (seq[start + i] != c)
                return false;
        return true;
    }

    bool isStepFn(int start, int len, bool diffBy1)
    {
        int diff = seq[start + 1] - seq[start];
        if (diffBy1 && diff != 1 && diff != -1) return false;
        for (int i = 1; i < len - 1; i++) {
            if ((seq[start + i + 1] - seq[start + i]) != diff)
                return false;
        }
        return true;
    }

    bool twoNums(int start, int len)
    {
        char a = seq[start], b = seq[start + 1];
        for (int i = start + 2; i < start + len; i++) {
            char target = ((i - start) % 2 == 0) ? a : b;
            if (seq[i] != target)
                return false;
        }
        return true;
    }

    int level(int start, int len)
    {
        if (isRepeating(start, len))
            return 1;
        if (isStepFn(start, len, true)) 
            return 2;
        if (twoNums(start, len))
            return 4;
        if (isStepFn(start, len, false))
            return 5;
        return 10;
    }
public:
    Solution()
    {
        seq = getStr();
        memset(cache, -1, sizeof(cache));
    }

    int solve(int start)
    {
        int& ret = cache[start];
        if (ret != -1) return ret;

        int minSum = BIG_INT;
        for (int len = 3; len <= 5; len++) {
            int rem = seq.size() - (start + len);
            if (rem == 0) 
                minSum = std::min(minSum, level(start, len));
            else if (rem >= 3)
                minSum = std::min(minSum, level(start, len) + solve(start + len));
        }
        return ret = minSum;
    }
    
};

int main(int argc, const char* argv[])
{
    int num_cases = getInt();
    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        int answer = sol.solve(0);
        std::cout << answer << std::endl;
    }
}