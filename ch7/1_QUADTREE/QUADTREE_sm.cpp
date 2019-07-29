#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class Solution
{
private:
public:
    std::string text, answer;
    Solution()
    {
        std::getline(std::cin, text);
    }

    std::string solve(std::string str)
    {
        if (str.size() == 1) return str; 

        std::vector<std::string> buffer(4);

        int offset = (str[0] == 'x') ? 1 : 0;
        bool mixed = (str[0] == 'x') ? true : false;        

        for (int i = 0; i < 4; i++) {
            if (str[i + offset] != 'x')
                buffer[i] = str[i + offset];
            else {
                buffer[i] = solve(str.substr(i + offset));
                offset += buffer[i].size() - 1;
            }
        }
        std::string result = buffer[2] + buffer[3] + buffer[0] + buffer[1];
        return mixed ? 'x' + result : result;
    }
};


int main(int argc, const char* argv[])
{
    std::string line;
    std::getline(std::cin, line);
    int num_cases = std::stoi(line);

    for (int i = 0; i < num_cases; i++) {
        Solution sol;
        auto answer = sol.solve(sol.text);
        std::cout << answer << std::endl;
    }
    return 0;
}