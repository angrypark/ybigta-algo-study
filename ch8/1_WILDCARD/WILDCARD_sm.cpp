#ifdef __linux__
#include <bits/stdc++.h>
#else
#include <algorithm>
#include <iostream>
#include <sstream>
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
    std::string s;
    std::getline(std::cin, s);
    return std::stoi(s);
}

void simplify(std::string& str, char c = '*')
{
    bool flag = false;
    for (auto it = str.begin(); it != str.end(); ) {
        if (*it == c) {
            if (flag) { it = str.erase(it); continue; }
            else flag = true;
        }
        else flag = false;
        it++;
    }
}

class Solution
{
private:
    std::string regex, str;
    int cache[101][101];

    bool match(int s, int r)
    {
        int& ret = cache[s][r];
        if (ret != -1) return ret;

        if (regex.size() == r && str.size() > s)
            return ret = false;

        if (str.size() == s) {
            if (regex.size() == r)
                return ret = true;
            else if (regex[r] == '*')
                return match(s, r + 1);
            else
                return ret = false;
        }

        if (regex[r] == '?' || str[s] == regex[r])
            return match(s + 1, r + 1);
        if (regex[r] == '*')
            return match(s, r + 1) || match(s + 1, r);
        return ret = false;
    }

public:
    Solution()
    {
        std::getline(std::cin, regex);
        simplify(regex);
    }

    void solve()
    {
        std::vector<std::string> answer;

        int n = getInt();
        for (int i = 0; i < n; i++) {
            memset(cache, -1, sizeof(cache));
            str = getStr();
            if (match(0, 0))
                answer.push_back(str);
        }
        std::sort(answer.begin(), answer.end());
        for (auto& s : answer)
            std::cout << s << std::endl;
    }
};


int main(int argc, const char* argv[])
{
    int num_cases = getInt();

    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        sol.solve();
    }
    return 0;
}