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

void parseFriends(int& num_friends, int& num_pairs, std::vector<std::vector<bool>>& friends, std::vector<bool>& taken)
{
    std::string line;

    std::getline(std::cin, line);

    auto v = intSplit(line);
    num_friends = v[0];
    num_pairs   = v[1];

    std::vector<bool> false_vector(num_friends, false);
    friends = std::vector<std::vector<bool>>(num_friends, false_vector);
    taken = false_vector;

    std::getline(std::cin, line);

    v = intSplit(line);
    for (int i = 0; i < num_pairs; i++) {
        int x = v[2 * i], y = v[2 * i + 1];
        friends[x][y] = friends[y][x] = true;
    }
}

int recursivelyCount(int num_friends, int num_pairs, const std::vector<std::vector<bool>>& friends, std::vector<bool> taken)
{
    int first, second;
    int count = 0;

    bool done = true;
    for (int i = 0; i < num_friends; i++)
        if (!taken[i]) {
            done = false;
            first = i;
            break;
        }

    if (done) return 1;

    for (int i = first + 1; i < num_friends; i++)
        if (!taken[i] && friends[first][i]) {
            taken[first] = taken[i] = true;
            count += recursivelyCount(num_friends, num_pairs, friends, taken);
            taken[first] = taken[i] = false;
        }

    return count;
}

int numPairs()
{
    int num_friends, num_pairs;
    std::vector<std::vector<bool>> friends;
    std::vector<bool> taken;
    parseFriends(num_friends, num_pairs, friends, taken);

    return recursivelyCount(num_friends, num_pairs, friends, taken);
}


int main(int argc, const char* argv[])
{
    std::string line;
    std::getline(std::cin, line);
    int num_cases = std::stoi(line);

    for (int i = 0; i < num_cases; i++) {
        int n = numPairs();
        std::cout << n << std::endl;
    }

    return 0;
}