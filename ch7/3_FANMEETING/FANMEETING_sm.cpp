#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>


class Solution
{
private:
    std::string members, fans;
    int m, f;
public:
    Solution()
    {
        std::getline(std::cin, members);
        std::getline(std::cin, fans);
    }

    bool isAllHugging(const std::string& A, const std::string& B)
    {
        for (int i = 0; i < A.size(); i++)
            if (A[i] == 'M' && B[i] == 'M')
                return false;
        return true;
    }

    int solve()
    {
        if (members.size() > fans.size()) return 0;

        int count = 0;
        for (int i = 0; i < fans.size() - members.size() + 1; i++)
            count += isAllHugging(members, fans.substr(i, members.size()));
        return count;
    }
};


int main(int argc, const char* argv[])
{
    std::string line;
    std::getline(std::cin, line);
    int num_cases = std::stoi(line);

    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        auto answer = sol.solve();
        std::cout << answer << std::endl;
    }
    return 0;
}