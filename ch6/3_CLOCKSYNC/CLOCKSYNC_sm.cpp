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

class ClockSync
{
    std::vector<std::vector<int>> switches = {
        {0, 1, 2},
        {3, 7, 9, 11},
        {4, 10, 14, 15},
        {0, 4, 5, 6, 7},
        {6, 7, 8, 10, 12},
        {0, 2, 14, 15},
        {3, 14, 15},
        {4, 5, 7, 14, 15},
        {1, 2, 3, 4, 5},
        {3, 4, 5, 9, 13}
    };
    std::vector<int> clocks;
    int min = INT_MAX;
public:
    ClockSync()
    {
        std::string line;
        std::getline(std::cin, line);
        clocks = intSplit(line);
    }

    void solve(int start = 0, int count = 0)
    {
        if (start > 9) return;
        if (allTwelve() && count < min)
            min = count;

        for (int r = 0; r < 4; r++) {
            press(start, r);
            solve(start + 1, count + r);
            press(start, r, true);
        }
    }

    int answer()
    {
        return (min < INT_MAX) ? min : -1;
    }

    void press(int idx, int r, bool rewind = false)
    {
        int move = rewind ? -3 : 3;
        for (int i : switches[idx]) {
            clocks[i] += move * r;
            if (clocks[i] > 12) clocks[i] -= 12;
            else if (clocks[i] <= 0) clocks[i] += 12;
        }
    }

    bool allTwelve()
    {
        for (int hour : clocks)
            if (hour != 12)
                return false;
        return true;
    }
};

int main(int argc, const char* argv[])
{
    std::string line;
    std::getline(std::cin, line);
    int num_cases = std::stoi(line);

    for (int i = 0; i < num_cases; i++) {
        ClockSync solution;
        solution.solve();
        std::cout << solution.answer() << std::endl;
    }
    return 0;
}