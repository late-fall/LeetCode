class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    # from leetcode solution
    
        visited = set()
        emails_accounts_map = {}
        res = []
        
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] not in emails_accounts_map:
                    emails_accounts_map[account[j]] = [i]
                else:
                    emails_accounts_map[account[j]].append(i)
                    
        # DFS code for traversing accounts.
        def dfs(i, emails):
            if i in visited:
                return
            visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
                    
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if i in visited:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
        
        
#         <doesn't work>

#         names = set()
#         res = []
        
#         for account in accounts:
#             name = account[0]
#             emails = account[1:]
            
#             if name not in names:
#                 res.append(account)
#                 names.add(name)
#             else:
#                 temp2 =[]
#                 for acc in res:
#                     same = False
#                     temp = []
#                     for email in emails:
#                         if email in acc[1:]:
#                             same = True
#                         else:
#                             temp.append(email)
#                     if same:
#                         acc.extend(temp)
#                     else:
#                         temp2 = [name] + temp
#                 if len(temp2) > 0 and temp2[0] not in names:
#                     res.append(temp2)
        
#         result = []
        
#         for item in res:
#             result.append(sorted(list(set(item))))
        
#         return sorted(result)