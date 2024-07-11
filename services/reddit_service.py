import enum
import requests

class RedditService:
    
    def __init__(self, subreddit:str, typeof_listing:str, format:str, params:dict) -> None:
        self.base_url = "https://www.reddit.com/"
        
        self.subreddit = f"{subreddit}/" if subreddit else None
        self.typeof_listing =  f"{typeof_listing}." if typeof_listing else "hot."
        self.format = f"{format}" if format else "json"
        self.params = params
        
        
    def get_reddit_posts(self):
        
        request_url_no_parameters = f"{self.base_url}{self.subreddit}{self.typeof_listing}{self.format}"
        
        
        request_parameters_list = [] 
        for param, value in self.params:
            request_parameter = f"?{param}={value}" 
            request_parameters_list.append(request_parameter)
            
        request_parameters = "".join(request_parameters_list)
        
        request_url = f"{request_url_no_parameters}{request_parameters}"
        return requests.get(request_url)
        
        
    def __call__(self):
        return self.get_reddit_posts()
        
        
            
            

    
    
    