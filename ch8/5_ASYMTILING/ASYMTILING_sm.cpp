#ifdef __linux__
#include <bits/stdc++.h>
#else
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
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
    int N;
    int cache[101];
    static constexpr int MOD = 1000000007;

    int tiling(int n)
    {
        if (n <= 1) return 1;
        int& ret = cache[n];
        if (ret != -1) return ret;
        return ret = (tiling(n - 1) + tiling(n - 2)) % MOD;
    }

    int countSymmetric(int n)
    {
        if (n % 2 == 1)
            return tiling((n - 1) / 2) % MOD;
        return (tiling((n - 2) / 2) + tiling(n / 2)) % MOD;
    }

public:
    Solution()
    {
        N = getInt();
    }

    int solve()
    {
        memset(cache, -1, sizeof(cache));
        return (tiling(N) - countSymmetric(N) + MOD) % MOD;
    }
};

int main(int argc, const char* argv[])
{
    int num_cases = getInt();
    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        int answer = sol.solve();
        std::cout << answer << std::endl;
    }
}