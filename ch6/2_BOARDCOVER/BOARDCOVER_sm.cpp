#include <iostream>
#include <sstream>
#include <string>
#include <tuple>
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

class BoardCover
{
private:
    enum { COVER, UNCOVER };
    int width, height, free;
    std::vector<std::vector<int>> board;
    std::vector<std::vector<std::vector<int>>> pattern = {
        {{0,0},{0,1},{1,1}},
        {{0,0},{1,0},{1,-1}},
        {{0,0},{1,0},{1,1}},
        {{0,0},{0,1},{1,0}},
    };
public:
    BoardCover()
    {
        std::string line;

        std::getline(std::cin, line);

        auto v = intSplit(line);
        height = v[0];
        width  = v[1];
        free = width * height;

        board = std::vector<std::vector<int>>(height, std::vector<int>(width, 0));

        for (int i = 0; i < height; i++) {
            std::getline(std::cin, line);
            for (int j = 0; j < width; j++) {
                if (line[j] == '#') {
                    board[i][j] = 1;
                    free--;
                }
            }
        }
    }

    std::tuple<int, int> getFirstWhite()
    {
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                if (board[i][j] == 0)
                    return std::make_tuple(i, j);
        return std::make_tuple(-1,-1);
    }

    int countCoverings()
    {
        int result = 0;
        if (free % 3 != 0) return 0; // base case: can't cover the whole area, or the place is already covered.
        if (free == 0) return 1; // base case: if everything is already covered, we're done!

        int x, y;
        std::tie(y, x) = getFirstWhite();

        for (int r = 0; r < 4; r++) { // r for rotation
            if (isSafe(x, y, r)) {
                cover(x, y, r, COVER);
                result += countCoverings();
                cover(x, y, r, UNCOVER);
            }
        }
        return result;
    }

    void cover(int x, int y, int r, int mode)
    {
        int multiplier = (mode == COVER) ? 1 : -1;
        for (int i = 0; i < 3; i++) {
            int dy = pattern[r][i][0];
            int dx = pattern[r][i][1];
            board[y + dy][x + dx] += multiplier;
        }
        free -= multiplier * 3;
    }

    bool isSafe(int x, int y, int r)
    {
        for (int i = 0; i < 3; i++) {
            int target_y = y + pattern[r][i][0];
            int target_x = x + pattern[r][i][1];
            if ((target_x < 0) || (target_x >= width) || 
                (target_y < 0) || (target_y >= height)) return false;
            if (board[target_y][target_x] == 1) return false;
        }
        return true;
    }
    
};

int main(int argc, const char* argv[])
{
    std::string line;
    std::getline(std::cin, line);
    int num_cases = std::stoi(line);

    for (int i = 0; i < num_cases; i++) {
        BoardCover x;
        int answer = x.countCoverings();
        std::cout << answer << std::endl;
    }
    return 0;
}