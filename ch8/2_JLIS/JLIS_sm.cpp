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

std::vector<int> getIntVec()
{
    std::stringstream ss(getStr());
    std::vector<int> v;
    std::string s;
    while (std::getline(ss, s, ' '))
        v.push_back(std::stoi(s));
    return v;
}

class Solution
{
private:
    int cache[101][101];
    std::vector<int> A, B, sizes;
    long long NEG_INF = std::numeric_limits<long long>::min();

    int solveImpl(int idxA, int idxB)
    {
        int& ret = cache[idxA + 1][idxB + 1];
        if (ret != -1) return ret;

        long long elemA = (idxA == -1) ? NEG_INF : A[idxA];
        long long elemB = (idxB == -1) ? NEG_INF : B[idxB];
        long long maxElem = std::max(elemA, elemB);

        int maxLen = 2;
        for (int nextA = idxA + 1; nextA < A.size(); nextA++)
            if (maxElem < A[nextA])
                maxLen = std::max(maxLen, 1 + solveImpl(nextA, idxB));

        for (int nextB = idxB + 1; nextB < B.size(); nextB++)
            if (maxElem < B[nextB])
                maxLen = std::max(maxLen, 1 + solveImpl(idxA, nextB));
        return ret = maxLen;
    }
public:
    Solution()
    {
        sizes = getIntVec();
        A = getIntVec();
        B = getIntVec();
    }
    
    int solve()
    {
        memset(cache, -1, sizeof(cache));
        return solveImpl(-1, -1) - 2;
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