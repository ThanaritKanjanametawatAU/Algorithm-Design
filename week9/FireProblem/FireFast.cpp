#include <iostream>
#include <vector>
#include <queue>

int main() {
    // Read Input N
    int N;
    std::cin >> N;


    // Read Input House of N*N 2-D vector
    std::vector<std::vector<int>> House(N, std::vector<int>(N, 0));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cin >> House[i][j];
        }
    }

    // Solve Problem

    // Use Priority Queue and push the starting point (N-1, N-1)
    std::priority_queue<int> PQ;
    PQ.push(House[N-1][N-1]);

    // Declare p for the sum of the path
    int p = 0;

    // In Each Depth, pop the top of PQ and add it to p
    for (int i = 2*N-2; i > 0; --i) {

        // u = PQ.dequeue()
        int u = PQ.top();
        PQ.pop();

        // Add u to p
        p += u;

        // Push the elements in the next depth to PQ
        for (int j = 0; j < N; ++j) {
            if (0 <= i-1-j && i-1-j < N) {
                PQ.push(House[j][i-1-j]);
            }
        }
    }

    // Print the result p
    std::cout << p << std::endl;

    return 0;
}