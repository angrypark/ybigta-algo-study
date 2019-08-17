#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

template<typename T>
using Matrix = std::vector<std::vector<T>>;


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

inline double vector_mult(const Matrix<double>& A, const Matrix<double>& B, int i, int j) {
    double output = 0;
    for (int k = 0; k < A[0].size(); k++)
        output += A[i][k] * B[k][j];
    return output;
}


Matrix<double> dot(const Matrix<double>& A, const Matrix<double>& B) {
    auto output = Matrix<double>(A.size(), std::vector<double>(B[0].size(), -1));
    for (int i = 0; i < A.size(); i++)
        for (int j = 0; j < B[0].size(); j++)
            output[i][j] = vector_mult(A, B, i, j);
    return output;
}


int main(int argc, const char* argv[]) {
    std::cout.precision(10);
    int num_test = getInt();
    for (int _ = 0; _ < num_test; _++) {
        auto args = getIntVec();
        int N = args[0];
        int D = args[1];
        int start = args[2];

        Matrix<int> l(N);
        Matrix<double> p(N);
        for (int i = 0; i < N; i++) {
            l[i] = getIntVec();
            double sum = std::accumulate(l[i].begin(), l[i].end(), 0.);
            std::vector<double> row;
            for (int j = 0; j < l[i].size(); j++)
                row.push_back(l[i][j] / sum);
            p[i] = row;
        }
        Matrix<double> m(N, std::vector<double>(N, 0));
        m[start][start] = 1;
        for (int i = 0; i < D; i++)
            m = dot(m, p);
        const auto& prob = m[start];
        getStr();
        auto idx = getIntVec();
        for (int i = 0; i < idx.size() - 1; i++)
            std::cout << prob[idx[i]] << ' ';
        std::cout << prob[idx[idx.size() - 1]] << std::endl;
    }
}
