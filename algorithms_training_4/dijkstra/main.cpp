#include <iostream>
#include <fstream>
#include <vector>
#include <set>

unsigned int dijkstra(std::vector<std::vector<std::pair<int, int>>> graph, int start, int size) {
    std::vector<long long> values(size, 10000000000);
    values[start] = 0;

    std::set<std::pair<long long, int>> q;
    q.insert(std::make_pair(values[start], start));

    while (!q.empty()){
        int v = q.begin()->second;
        q.erase(q.begin());
        for (std::pair<long long, int> pair : graph[v]){
            int vert = pair.first;
            long long val = pair.second;
            if (values[vert] > values[v] + val){
                q.erase({values[vert], vert});
                values[vert] = values[v] + val;
                q.insert({values[vert], vert});
            }
        }
    }
    return values[size - 1];
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::ifstream inputFile("/Users/user/Documents/input.txt");
    std::ofstream outputFile("/Users/user/Documents/output.txt");
    int n, m;
    inputFile >> n >> m;
    std::vector<std::vector<std::pair<int, int>>> matrix(n);
    for (int i = 0; i < m; ++i) {
        int x, y, value;
        inputFile >> x >> y >> value;
        matrix[x - 1].push_back(std::make_pair(y - 1, value));
        matrix[y - 1].push_back(std::make_pair(x - 1, value));
    }
    outputFile << dijkstra(matrix, 0, n);
    return 0;
}
