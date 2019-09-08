#include <string>
#include <vector>
#include <sstream>

using namespace std;

class Solution {
public:
    void constructString(vector<string>& result, vector<string>& wordDict, 
                     vector<int>& path, vector<vector<int>>& possiblePreLocation,
                     int curPos)
    {
        if (-1 == curPos) {
            stringstream ss;
            for (int i = path.size() - 1; i >= 0 ; --i) {            
                ss << wordDict[path[i]] << " ";
            }
            ss << wordDict[path[path.size() - 1]];
            result.push_back(ss.str());
        } else {
            for (int i = 0; i < possiblePreLocation[curPos].size(); ++i) {
                path.push_back(possiblePreLocation[curPos][i]);
                constructString(result, wordDict, path, possiblePreLocation, possiblePreLocation[curPos][i]);
            }
        }

        path.pop_back();
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int wordCount = wordDict.size();
		int length = s.length();
		vector<bool> flag;
        vector<vector<int>> possiblePreLocation;
		flag.resize(length);
        possiblePreLocation.resize(length);
		for (int i = 0; i < length; ++i)
		{
			flag[length] = false;
		}
		for (int i = 0; i < length; ++i)
		{
			for (int j = 0; j < wordCount; ++j)
			{
				int prelocation = i - wordDict[j].length();
				if (-1 == prelocation && wordDict[j] == s.substr(0, wordDict[j].length()))
				{
					flag[i] = true;
					possiblePreLocation[i].push_back[prelocation];
				}
				else if (prelocation >= 0) {
					if (flag[prelocation] && wordDict[j] == s.substr(prelocation + 1, wordDict[j].length()))
					{
						flag[i] = true;
						possiblePreLocation[i].push_back[prelocation];
					}
				}
					
			}
		}

        vector<string> result;
        vector<int> path;

        constructString(result, wordDict, path, possiblePreLocation, length - 1);

		return result;
    }
};