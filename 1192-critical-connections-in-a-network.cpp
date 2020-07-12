#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<vector<int>> neightbor;
    vector<vector<int>> result;
    int index;
    vector<int> v_index;
    vector<int> v_lowlink;

    void strongConnect(int v){
        v_index[v] = index;
        ++index;
        v_lowlink[v] = index;

        for(int k = 0; k < neightbor[v].size(); ++k) {
            int w = neightbor[v][k];
            if (v_index[w] < 0) {
                strongConnect(w);
                if (v_lowlink[w] > v_lowlink[v]) {
                    result.push_back({v, w});
                }
                v_lowlink[v] = min(v_lowlink[v], v_lowlink[w]);
            } else {
                v_lowlink[v] = min(v_lowlink[v], v_index[w]);
            }
        }
    }

    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        //建立邻接表
        neightbor.resize(n);
        for (int i = 0; i < connections.size(); ++i) {
            neightbor[connections[i][0]].push_back(connections[i][1]);
            neightbor[connections[i][1]].push_back(connections[i][0]);
        }

        v_index.resize(n);
        v_lowlink.resize(n);
        for (int i = 0; i < n; ++i) {
            v_index[i] = -1;
            v_lowlink[i] = -1;
        }
        index = 0;

        strongConnect(0);

        return result;
    }
};