#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<int> intSplit(const std::string& str, char delim = ' ')
{
    std::string s;
    std::vector<int> result;
    std::stringstream ss(str);
    while (std::getline(ss, s, delim))
        result.push_back(std::stoi(s));
    return result;
}

class Solution
{
private:
    int n;
    std::vector<int> heights;
public:
    Solution()
    {
        std::string line;
        std::getline(std::cin, line);

        n = std::stoi(line);

        std::getline(std::cin, line);
        heights = intSplit(line);
    }

    int solve(int from = 0, int to = -1)
    {
        if (to == -1) to = n;
        if (from >= to - 1) return heights[from];

        int mid = from + (to - from) / 2;

        int max = std::max(solve(from, mid), solve(mid, to));

        int left = mid - 1, right = mid;
        int h = std::min(heights[left], heights[right]);

        int area = (right - left + 1) * h;
        if (area > max)
            max = area;

        while (left > from || right < to - 1) {
            if (right < to - 1 && ((left == from) || (heights[left - 1] < heights[right + 1]))) {
                h = std::min(h, heights[++right]);
            } else {
                h = std::min(h, heights[--left]);
            }

            area = (right - left + 1) * h;
            if (area > max)
                max = area;
        }

        return max;
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