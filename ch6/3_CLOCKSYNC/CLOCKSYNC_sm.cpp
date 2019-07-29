#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define BIG_INT 9999

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
    int min = BIG_INT;
public:
    ClockSync()
    {
        std::string line;
        std::getline(std::cin, line);
        clocks = intSplit(line);
        for (int& i : clocks)
            i = i % 12;
    }

    void solve(int start = 0, int count = 0)
    {
        if (allTwelve() && count < min) {
            min = count;
            return;
        }
        if (start > 9) return;

        for (int r = 0; r < 4; r++) {
            solve(start + 1, count + r);
            press(start);
        }
    }

    int answer()
    {
        return (min < BIG_INT) ? min : -1;
    }

    void press(int idx)
    {
        for (int i : switches[idx])
            clocks[i] = (clocks[i] + 3) % 12;
    }

    bool allTwelve()
    {
        for (int hour : clocks)
            if (hour != 0)
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