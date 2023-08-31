#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Define the Activity structure
struct Activity {
    int start, finish;
};

// A utility function that sorts activities based on finish time
bool activityCompare(Activity s1, Activity s2) {
    return (s1.finish < s2.finish);
}

void printMaxActivities(vector<Activity> &arr) {
    // Sort Activities in increasing order of finish time
    sort(arr.begin(), arr.end(), activityCompare);

    // The first activity is always selected
    int count = 1;
    int i = 0;

    for (int j = 1; j < arr.size(); j++) {
        if (arr[j].start > arr[i].finish) {
            count++;
            i = j;
        }


    }
    cout << count << endl;
}

int main() {
    int N;
    cin >> N;

    vector<Activity> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i].start >> arr[i].finish;
    }
    printMaxActivities(arr);
    return 0;
}
