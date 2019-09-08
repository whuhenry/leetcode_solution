#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
	bool wordBreak(string s, vector<string>& wordDict)
	{
		int wordCount = wordDict.size();
		int length = s.length();
		vector<bool> flag;
		flag.resize(length);
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
					break;
				}
				else if (prelocation >= 0) {
					if (flag[prelocation] && wordDict[j] == s.substr(prelocation + 1, wordDict[j].length()))
					{
						flag[i] = true;
						break;
					}
				}
					
			}
		}

		return flag[length - 1];
	}
};