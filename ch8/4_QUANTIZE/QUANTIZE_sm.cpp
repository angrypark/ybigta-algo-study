#ifdef __linux__
#include <bits/stdc++.h>
#else
#include <algorithm>
#include <cmath>
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
    std::string s;
    std::vector<int> ret;
    while (std::getline(ss, s, ' '))
        ret.push_back(std::stoi(s));
    return ret;
}

class Solution
{
private:
    int BIG_INT = 987654321;
    std::vector<int> seq;

public:
    int N, max_bins;
    Solution()
    {
        std::vector<int> meta = getIntVec();
        N = meta[0];
        max_bins = meta[1];
        seq = getIntVec();
        std::sort(seq.begin(), seq.end()); // O(nlogn)
    }

    int minLoss(int from, int to)
    {
        int avg = 0;
        for (int i = from; i < to; i++)
            avg += seq[i];
        avg /= (to - from);

        int ret = 0;
        for (int i = from; i < to; i++)
            ret += pow(seq[i] - avg, 2);
        // std::cout << "from: " << from << ", to: " << to << ", L = " << ret << std::endl;
        return ret;
    }

    int solve(int start, int bins)
    {
        if (start == seq.size())
            return 0;
        if (bins == 0)
            return BIG_INT;

        int min = BIG_INT;
        for (int size = 1; start + size <= seq.size(); size++) {
            min = std::min(min, minLoss(start, start + size) + solve(start + size, bins - 1));
        }
        return min;
    }
};

int main(int argc, const char* argv[])
{
    int num_cases = getInt();
    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        int answer = sol.solve(0, sol.max_bins);
        std::cout << answer << std::endl;
    }
}