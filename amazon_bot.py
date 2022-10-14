import scrapy 
import pandas as pd
#from items import SrrapyyyItem 


class AmazonBotSpider(scrapy.Spider):
    name = 'amazon-bot'
    #count=1
    #allowed_domains = ['exam.com']
    start_urls = ['https://www.amazon.com/s?k=headphones&crid=2Q4A9SNKRD3QW&sprefix=headphone%2Caps%2C732&ref=nb_sb_noss_2']

    def parse(self, response):
        # product=SrrapyyyItem()
        data=[]
        name_li=response.css(".a-size-medium.a-color-base.a-text-normal::text").extract()
        #no_reviews=response.css(".a-size-base.s-underline-text").css("::text").extract()
        no_reviews_li=response.css(".a-size-base.s-underline-text").css("::text").extract()
        price_li=response.css(".a-price.a-text-price").css("::text").extract()
        image_url_li=response.css(".s-image").css("::attr(src)").extract() 
        for name, no_reviews, price, image_url in zip(name_li,no_reviews_li,price_li,image_url_li): 
        
            data.append([name, no_reviews, price, image_url]) 
        print(data)
        df=pd.DataFrame(data)
        df.to_csv('hhh.csv')
        #return df
        
    
        # product["p_name"]=name 
        # product["p_reviews"]=no_reviews
        # product["p_price"]=price
        # product["p_image_url"]=image_url
        
        
        # yield product 
       # AmazonBotSpider.count+=1 
        
        #nxt_page="https://www.amazon.in/s?k=headphones&page="+ \ str(AmazonBotSpider.count)+"&qid=1664861322&sprefix=head%2Caps%2C426&ref=sr_pg_3" 
        #if AmazonBotSpider.count<6:
            #yield response.follow(nxt_page,callback=self.parse)
        
      
