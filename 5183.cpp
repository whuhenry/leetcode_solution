#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        vector<string> week = {"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};
        int daySum = 0;
        for (int i = 1971; i < year; ++i) {
            if((i % 4 == 0 && i % 100 != 0) || i % 400 == 0) {
                daySum +=366;
            } else {
                daySum += 365;
            }
        }

        for (int i = 1; i < month; ++i) {
            if (1 == i || 3 == i || 5 == i || 7 ==i || 8 ==i || 10 == i || 12 == i) {
                daySum += 31;
            } else if (2 == i) {
                if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                    daySum += 29;
                } else {
                    daySum += 28;
                }
            } else {
                daySum += 30;
            }
        }

        daySum += day;
        return week[daySum % 7];
    }
};