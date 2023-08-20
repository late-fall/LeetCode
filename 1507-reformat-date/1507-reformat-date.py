class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(' ')
        print(date)
        
        def convertDate(date):
            if len(date) == 3:
                return "0" + date[0]
            else:
                return date[:2]
        
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct":10, "Nov":11, "Dec":12}
        
        return date[2] + "-" + str(months[date[1]]) + "-" + convertDate(date[0])