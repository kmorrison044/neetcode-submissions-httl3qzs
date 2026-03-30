class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> closedToOpen = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        stack<char> stack;

        for (char c : s)
        {
            if (closedToOpen.find(c) != closedToOpen.end())
            {
                if (stack.empty() || stack.top() != closedToOpen[c])
                {
                    return false;
                }

                stack.pop();
            }
            else
            {
                stack.push(c);
            }
        }

        return stack.empty();
    }
};
