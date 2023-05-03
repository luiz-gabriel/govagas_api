from Models.Search import SearchModel

class SearchController:
    def getJobs(title, state, city, page):
        skip = page * 9
        
        if title is not None and state is not None and city is not None: 
            sql = f"SELECT `title`, `resume`, `type`, `slug`, `date` FROM `jobs` WHERE (title LIKE '{title}%') AND state='{state}' AND city='{city}' LIMIT 10 OFFSET {skip}"
            return SearchModel.getJobs(sql, page)
        elif state is not None and city is not None:
            sql = f"SELECT `title`, `resume`, `type`, `slug`, `date` FROM `jobs` WHERE state='{state}' AND city='{city}' LIMIT 10 OFFSET {skip}"
            return SearchModel.getJobs(sql, page)
        elif title is not None and state is None and city is None:
             sql = f"SELECT `title`, `resume`, `type`, `slug`, `date` FROM `jobs` WHERE title LIKE '{title}%' LIMIT 10 OFFSET {skip}"
             return SearchModel.getJobs(sql, page)
        elif title is not None and state is not None and city is None:
            print(state)
            sql = f"SELECT `title`, `resume`, `type`, `slug`, `date` FROM `jobs` WHERE (title LIKE '%{title}%') AND state='{state}' LIMIT 10 OFFSET {skip}"
            return SearchModel.getJobs(sql, page)
        else:
            sql = f"SELECT `title`, `resume`, `type`, `slug`, `date` FROM `jobs` LIMIT 10 OFFSET {skip}"
            return SearchModel.getJobs(sql, page)
        