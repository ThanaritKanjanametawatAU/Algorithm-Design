#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double Total = 0;

bool ComparePairs(pair<int, int> p1, pair<int, int> p2) {
    return p1.first > p2.first && p1.second < p2.second;
}

void merge(vector<pair<int, int>> &A, int left, int middle, int right) {
    vector<pair<int, int>> B;
    int i = left, j = middle + 1;

    while (i <= middle && j <= right) {
        if (ComparePairs(A[i], A[j]) || ComparePairs(A[j], A[i])) {
            for (int k = i; k <= middle; ++k) {
                Total += A[k].first + A[j].first;
            }
            B.push_back(A[j]);
            ++j;
        } else {
            B.push_back(A[i]);
            ++i;
        }
    }

    while (i <= middle) {
        B.push_back(A[i]);
        ++i;
    }
    while (j <= right) {
        B.push_back(A[j]);
        ++j;
    }

    for (int k = left; k <= right; ++k) {
        A[k] = B[k - left];
    }
}

void mergesort(vector<pair<int, int>> &A, int left, int right) {
    if (left < right) {
        int middle = (left + right) / 2;
        mergesort(A, left, middle);
        mergesort(A, middle + 1, right);
        merge(A, left, middle, right);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<int, int>> y;
    for (int i = 0; i < n; ++i) {
        int x1, x2;
        cin >> x1 >> x2;
        y.push_back({x1, x2});
    }

    sort(y.begin(), y.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        return a.first == b.first ? a.second < b.second : a.first > b.first;
    });

    mergesort(y, 0, y.size() - 1);

    cout << static_cast<long long>(Total) << endl;

    return 0;
}