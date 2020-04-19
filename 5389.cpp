class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        map<string, int> nameOrders;
        for (int i = 0; i < orders.size(); ++i) {
            if (nameOrders.find(orders[i][2]) == nameOrders.end()) {
                nameOrders[orders[i][2]] = nameOrders.size();
            }
        }
        map<int, vector<int>> orderList;
        for (int i = 0; i < orders.size(); ++i) {
            int tableId = stoi(orders[i][1]);
            string& foodName = orders[i][2];
            if (orderList.find(tableId) == orderList.end()) {
                vector<int> foodCount(nameOrders.size(), 0);
                orderList[tableId] = foodCount;
            }
            orderList[tableId][nameOrders[foodName]] += 1;
        }

        vector<vector<string>> result;
        vector<string> head;
        head.push_back("Table");
        for (map<string, int>::iterator  iter = nameOrders.begin(); iter != nameOrders.end(); ++iter) {
            head.push_back(iter->first);
        }
        result.push_back(head);

        for (auto iter = orderList.begin(); iter != orderList.end(); ++iter) {
            vector<string> tableOrder;
            int tableId = iter->first;
            tableOrder.push_back(to_string(tableId));
            for (map<string, int>::iterator  nameIter = nameOrders.begin(); nameIter != nameOrders.end(); ++nameIter) {
                tableOrder.push_back(to_string(iter->second[nameIter->second]));
            }
            result.push_back(tableOrder);
        }
        return result;
    }
};